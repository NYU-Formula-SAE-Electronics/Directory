# MCU IO Map (STM32G474RET6)

Centralized view of every signal routed to the MCU, pulled together from
[gen-2-architecture.md](./gen-2-architecture.md) and the STM-Core schematic.

The MCU lives on the shared **STM Core** board. Carrier boards (PCU, CTU, Dash)
mount a Core and route their peripheral IO into the MCU through the
board-to-board connector (3× `AXK530147YG`, 30-pin). So every carrier sees the
**Common Core IO** below *plus* its own board-specific signals.

**Direction** is relative to the MCU: `In` = into MCU, `Out` = out of MCU, `Bi` = bidirectional.

---

## Common Core IO (every board)

| Signal | Interface | Dir | Pins | Notes |
|---|---|---|---|---|
| CANTX_1 / CANRX_1 | FDCAN1 | Out / In | 2 | CAN bus 1 (PCU ↔ Cascadia) |
| CANTX_2 / CANRX_2 | FDCAN2 | Out / In | 2 | CAN bus 2 (PCU ↔ Dash ↔ CTU ↔ IMD ↔ BMS) |
| USB_D+ / USB_D- | USB FS | Bi | 2 | USB-C, flash + USB-to-CAN bridge role |
| SWDIO / SWCLK | SWD | Bi | 2 | Tag-Connect TC2030, first-flash / recovery |
| NRST | Reset | In | 1 | NRST button + SWD |
| BOOT0 | Boot sel | In | 1 | Pulldown + recovery button |
| SCK / MOSI / MISO / CS | SPI | mixed | 4 | microSD card |
| OSC_IN / OSC_OUT | HSE | — | 2 | Oscillator |
| Status LED(s) | GPIO | Out | 1+ | Board status |

> CC1/CC2 and the Power-MUX (TPS2121) are handled in the power section and are not MCU GPIO.

---

## PCU Gen 2

| Signal | Interface | Dir | Ch | Notes |
|---|---|---|---|---|
| Accelerator (APPS) | ADC | In | 2 | 2 analog ch via voltage dividers (redundant pedal) |
| Brake position | ADC | In | 2 | 2 analog ch via voltage dividers |
| Brake pressure | ADC | In | 2 | 2 sensors, analog via voltage dividers |
| Wheel speed | Timer/GPIO | In | 4 | 4 sensors (3-pin each); freq capture |
| Regen / RTDS / RTDB | GPIO | Out | 3 | Digital outputs (RTDS = ready-to-drive sound) |
| Extra signals | GPIO | Bi | 4 | Spare on connector |
| **ADC subtotal** | | | **6** | |

---

## CTU (Central Telemetry Unit)

| Signal | Interface | Dir | Pins | Notes |
|---|---|---|---|---|
| GPS – RX | UART | In | 1 | From Adafruit Ultimate GPS TX, 9600 baud |
| GPS – TX | UART | Out | 1 | To GPS RX |
| GPS – PPS | Timer/GPIO | In | 1 | Pulse-per-second |
| GPS – Fix | GPIO | In | 1 | Fix status |
| LoRa – RX | UART | In | 1 | From RAK3172 TX |
| LoRa – TX | UART | Out | 1 | To RAK3172 RX |
| LoRa – RST | GPIO | Out | 1 | Module reset |
| IMU – SCK | SPI | Out | 1 | BMI088 |
| IMU – MOSI (SDI) | SPI | Out | 1 | BMI088 |
| IMU – MISO (SDO1/2) | SPI | In | 1 | BMI088 |
| IMU – CSB1 | GPIO | Out | 1 | Accel chip-select |
| IMU – CSB2 | GPIO | Out | 1 | Gyro chip-select |
| Suspension travel | ADC | In | 4 | 4 sensors (3-pin each) |
| Steering angle | ADC | In | 1 | 6-pin connector |
| **ADC subtotal** | | | **5** | suspension + steering (likely 27–28 season) |

---

## Dash

| Signal | Interface | Dir | Pins | Notes |
|---|---|---|---|---|
| Display – SCK | SPI | Out | 1 | NHD 7" EVE / FT81x |
| Display – MOSI | SPI | Out | 1 | |
| Display – MISO | SPI | In | 1 | |
| Display – /CS | GPIO | Out | 1 | Active low |
| Display – /INT | GPIO | In | 1 | Interrupt to host, active low |
| Display – /PD | GPIO | Out | 1 | Power-down, active low (10k pull-up) |
| Display – GPIO0–3 / quad | GPIO | Bi | 0–4 | Optional, quad-SPI / GPIO |
| Buttons: UP/DOWN/LEFT/RIGHT/BACK/ENTER | GPIO | In | 6 | Display navigation |
| LED – IMD | GPIO | Out | 1 | |
| LED – BMS | GPIO | Out | 1 | |
| CAN diag (USB-to-CAN bridge) | — | — | 0 | On CAN2 bus, not extra MCU pins |

---

## Steering Wheel (Dash peripheral, no own MCU)

Routes through the Dash 12-pin connector (same pinout as PCU's 12-pin) into the Dash MCU.

| Signal | Interface | Dir | Ch | Notes |
|---|---|---|---|---|
| Regen knob | ADC | In | 1 | Analog |
| Power knob | ADC | In | 1 | Analog |
| Nav buttons | GPIO | In | 6 | UP/DOWN/LEFT/RIGHT/BACK/ENTER (shared with Dash buttons) |
| Radio button | GPIO | In | 0–1 | TBD, defer to next year |

---

## Roll-up by interface type

| Board | ADC | UART | SPI bus | Digital In | Digital Out | CAN |
|---|---|---|---|---|---|---|
| Core (common) | – | – | 1 (SD) | 2 btn | 1+ LED | 2 buses |
| PCU Gen 2 | 6 | – | – | 4 wheel-spd + 4 extra | 3 | shared |
| CTU | 5 | 2 (GPS, LoRa) | 1 (IMU) + GPS/LoRa GPIO | 1 fix | 3 (LoRa RST, 2× IMU CS) | shared |
| Dash | – | – | 1 (display) | 6 btn + INT | /CS, /PD, 2 LED | shared + diag |
| Steering (via Dash) | 2 | – | – | 6 nav | – | – |

> **Open / TBD:** wheel-speed sensor signal type (likely digital Hall), final ADC
> divider ratios, display quad-SPI usage, steering radio button. Pin-level
> assignments to be locked once the STM-Core board-to-board pinout is frozen.
