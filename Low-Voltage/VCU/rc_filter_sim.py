#!/usr/bin/env python3
"""
RC anti-aliasing filter simulator for the Gen 2 pedal sensor chain.

Models the first-order RC low-pass that sits between the sensor voltage
divider and the STM32 ADC, sampled at 100 Hz. Shows, for one or more
R/C variants:

  1. Bode magnitude  -> where the corner (fc) sits vs. the 50 Hz Nyquist line
  2. Time domain     -> noisy analog input vs. filtered output
  3. ADC view        -> what the converter actually grabs at 100 Hz
  4. Spectrum        -> input vs. filtered FFT, i.e. how much noise is killed

Swap the synthetic input for logged bench data with --csv (see CSV MODE).

Deps: numpy, scipy, matplotlib   (python3 rc_filter_sim.py)

Note on the model: this treats R as the Thevenin resistance the cap sees.
For a divider that is R_top || R_bottom (e.g. 10k||15k = 6k). For a divider
followed by a dedicated series R into the ADC pin, use that series R instead.
"""

import argparse
import os
import sys
import tempfile

# Use a writable matplotlib cache dir (the default ~/.matplotlib may be locked),
# in the system temp dir so we don't drop a cache folder into the repo.
os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "mpl-cache-fsae"))

import numpy as np
import matplotlib

# Use the non-interactive backend when we're only saving a PNG (also avoids GUI
# crashes in headless / sandboxed runs). With a window the OS default is kept.
if "--no-show" in sys.argv:
    matplotlib.use("Agg")

import matplotlib.pyplot as plt
from scipy import signal


# ----------------------------------------------------------------------------
# CONFIG -- edit these to explore your design
# ----------------------------------------------------------------------------

# Filter variants to compare. Each is (label, R_ohms, C_farads).
# R = Thevenin resistance the cap sees (divider R_top || R_bottom, or a series R).
VARIANTS = [
    ("10k|15k div, 220nF", 6e3, 220e-9),   # fc ~ 121 Hz  -> above Nyquist, under-filters
    ("10k|15k div, 1uF",   6e3, 1e-6),      # fc ~  27 Hz  -> good default
    ("series 33k, 220nF",  33e3, 220e-9),   # fc ~  22 Hz  -> small/better cap route
]

FS_ADC = 100.0        # ADC sample rate [Hz] -> Nyquist = FS_ADC / 2
FS_SIM = 20_000.0     # high "analog" sim rate to represent the continuous input [Hz]
T_END = 2.0           # sim duration [s]

# Synthetic pedal input + injected noise (ignored in CSV mode).
PEDAL_REST_V = 1.5         # resting output [V]
PEDAL_TRAVEL_V = 1.2       # added at full press [V]
PRESS_START_S = 0.5        # when the press begins [s]
PRESS_DUR_S = 0.20         # how long the press ramp takes [s]
EMI_HZ, EMI_V = 1000.0, 0.15   # inverter / switching pickup
MAINS_HZ, MAINS_V = 60.0, 0.05  # low-freq pickup
WHITE_V = 0.03                  # broadband noise (1-sigma) [V]

ZOOM = (0.50, 0.70)   # x-limits [s] for the time-domain plots
SEED = 0              # RNG seed for repeatable noise
SAVE_PATH = os.path.join(os.path.dirname(__file__), "rc_filter_sim.png")


# ----------------------------------------------------------------------------
# Core helpers
# ----------------------------------------------------------------------------

def lowpass(r, c):
    """First-order RC low-pass H(s) = 1 / (1 + sRC)."""
    return signal.TransferFunction([1.0], [r * c, 1.0])


def fc_of(r, c):
    return 1.0 / (2.0 * np.pi * r * c)


def make_input(t):
    """Synthetic pedal press + injected noise."""
    rng = np.random.default_rng(SEED)
    ramp = np.clip((t - PRESS_START_S) / PRESS_DUR_S, 0.0, 1.0)
    pedal = PEDAL_REST_V + PEDAL_TRAVEL_V * ramp
    noise = (
        EMI_V * np.sin(2 * np.pi * EMI_HZ * t)
        + MAINS_V * np.sin(2 * np.pi * MAINS_HZ * t)
        + WHITE_V * rng.standard_normal(t.size)
    )
    return pedal, pedal + noise


def half_spectrum(x, fs):
    """Single-sided amplitude spectrum."""
    n = x.size
    win = np.hanning(n)
    X = np.fft.rfft((x - x.mean()) * win)
    f = np.fft.rfftfreq(n, 1.0 / fs)
    amp = (2.0 / np.sum(win)) * np.abs(X)
    return f, amp


def load_csv(path):
    """CSV MODE: expects columns time_s,voltage (header optional)."""
    data = np.genfromtxt(path, delimiter=",", names=True)
    cols = data.dtype.names
    t = data[cols[0]].astype(float)
    v = data[cols[1]].astype(float)
    fs = 1.0 / np.median(np.diff(t))
    return t, v, fs


# ----------------------------------------------------------------------------
# Plotting
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", help="log file with columns time_s,voltage to filter instead of synthetic input")
    ap.add_argument("--no-show", action="store_true", help="save PNG only, don't open a window")
    args = ap.parse_args()

    nyq = FS_ADC / 2.0

    if args.csv:
        t, vin, fs_sim = load_csv(args.csv)
        clean = None
        title_src = os.path.basename(args.csv)
    else:
        fs_sim = FS_SIM
        t = np.arange(0.0, T_END, 1.0 / fs_sim)
        clean, vin = make_input(t)
        title_src = "synthetic pedal + noise"

    print(f"{'variant':24s} {'R':>8s} {'C':>8s} {'fc':>9s}")
    for label, r, c in VARIANTS:
        print(f"{label:24s} {r/1e3:6.1f}k {c*1e9:6.0f}n {fc_of(r, c):7.1f} Hz")
    print(f"\nADC fs = {FS_ADC:.0f} Hz  ->  Nyquist = {nyq:.0f} Hz")

    fig, ax = plt.subplots(2, 2, figsize=(13, 8))
    ax_bode, ax_time, ax_adc, ax_fft = ax[0, 0], ax[0, 1], ax[1, 0], ax[1, 1]

    # 1) Bode magnitude for every variant.
    w = 2 * np.pi * np.logspace(0, 4, 3000)
    for label, r, c in VARIANTS:
        _, mag, _ = signal.bode(lowpass(r, c), w=w)
        line, = ax_bode.semilogx(w / (2 * np.pi), mag, lw=1.6, label=label)
        ax_bode.axvline(fc_of(r, c), color=line.get_color(), ls="--", lw=0.8, alpha=0.7)
    ax_bode.axvline(nyq, color="k", ls=":", lw=1.4, label=f"Nyquist {nyq:.0f} Hz")
    ax_bode.axhline(-3, color="gray", ls=":", lw=0.8)
    ax_bode.set(title="RC low-pass magnitude", xlabel="frequency [Hz]", ylabel="gain [dB]",
                ylim=(-60, 5))
    ax_bode.grid(True, which="both", alpha=0.3)
    ax_bode.legend(fontsize=8)

    # 2) Time domain: noisy input vs filtered output (per variant).
    ax_time.plot(t, vin, color="0.7", lw=0.4, label="noisy input")
    if clean is not None:
        ax_time.plot(t, clean, "k--", lw=1.0, label="true pedal")
    filtered = {}
    for label, r, c in VARIANTS:
        _, vout, _ = signal.lsim(lowpass(r, c), U=vin, T=t)
        filtered[label] = vout
        ax_time.plot(t, vout, lw=1.4, label=label)
    ax_time.set(title=f"time domain ({title_src})", xlabel="time [s]", ylabel="voltage [V]",
                xlim=ZOOM)
    ax_time.grid(True, alpha=0.3)
    ax_time.legend(fontsize=8)

    # 3) ADC view: what the converter samples at 100 Hz, for every variant.
    ts = np.arange(t[0], t[-1], 1.0 / FS_ADC)
    for i, (label, r, c) in enumerate(VARIANTS):
        color = f"C{i}"
        vout = filtered[label]
        vsamp = np.interp(ts, t, vout)
        ax_adc.plot(t, vout, lw=0.8, color=color, alpha=0.5)
        ax_adc.plot(ts, vsamp, "o-", ms=3, lw=1.0, color=color, label=f"{label} @ {FS_ADC:.0f} Hz")
    ax_adc.set(title="what the ADC actually grabs", xlabel="time [s]", ylabel="voltage [V]",
               xlim=ZOOM)
    ax_adc.grid(True, alpha=0.3)
    ax_adc.legend(fontsize=8)

    # 4) Spectrum: input vs filtered (first variant) -> noise rejection.
    ref_label = VARIANTS[0][0]
    f_in, a_in = half_spectrum(vin, fs_sim)
    f_out, a_out = half_spectrum(filtered[ref_label], fs_sim)
    ax_fft.semilogx(f_in, a_in, color="0.7", lw=0.8, label="input")
    ax_fft.semilogx(f_out, a_out, color="C0", lw=1.2, label=f"filtered ({ref_label})")
    ax_fft.axvline(nyq, color="k", ls=":", lw=1.4, label=f"Nyquist {nyq:.0f} Hz")
    ax_fft.set(title="amplitude spectrum", xlabel="frequency [Hz]", ylabel="amplitude [V]",
               xlim=(1, fs_sim / 2))
    ax_fft.grid(True, which="both", alpha=0.3)
    ax_fft.legend(fontsize=8)

    fig.suptitle("Gen 2 pedal-sensor RC anti-aliasing filter", fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(SAVE_PATH, dpi=120)
    print(f"\nsaved plot -> {SAVE_PATH}")
    if not args.no_show:
        plt.show()


if __name__ == "__main__":
    main()
