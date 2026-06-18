# PCU Gen 2

## 1. Filter R&D

Take home a pedal sensor + current PCU.
The PCU is currently powered through the 12V line. If you don't have a 12V DC Supply available, the data collection needs to be done at Makergarage. Another option is to remove the 12V to 5V DC Converter from the PCU board and solder the VUSB pad on the underside of the Teensy module to power the whole circuit through Micro USB.

### Steps

1. Write a program that reads both channels of the pedal sensor at >=100 Hz and logs data to the SD card.
    - See [https://github.com/NYU-Formula-SAE-Electronics/pcu-firmware](PCU Firmware Repo) for reference on reading raw data from the sensors.
2. Test both filter circuits in a single take:
   - Plug one channel into the RC filter using the on-board jumper.
   - Plug the other channel into the op-amp filter using the other on-board jumper.
   - Align and overlay the timing of the two graphs.
3. Write a `pyplot` (or similar) script to plot the CSV data as overlaid graphs so the two filter circuits can be directly compared.
4. Based on results, determine which filter circuit will be used for Gen 2.

## 2. Design

### Wheel Speed Sensor Candidates

- https://www.mouser.com/ProductDetail/ZF/GS101205?qs=Hrf4w4jKlWF6kC7FXTzHOg%3D%3D
- https://www.digikey.com/en/products/detail/zf-electronics/GS100502/361998?s=N4IgTCBcDaIOIGUCMAGFBWFEC6BfIA
- https://www.littelfuse.com/products/sensors/speed-sensors/hall-effect-sensors/55505/55505-00

### Open Questions

- Which wheel speed sensor? (needs mech approval)
- Steel vs magnet ring discussion ongoing with Ray.
- Connector sponsor/sample source?