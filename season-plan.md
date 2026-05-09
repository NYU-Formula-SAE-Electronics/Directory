# 2026 - 2027 Season
**1. One year is a surprisingly short time**
**2. Test before committing & make testing easy**
**3. KISS: Keep it simple, Stupid**

## Priorities
### Technical
- Migration to KiCad & GitHub (LV)
    - Centralized library for shared components & Designs
- New LV Architecture
- Wiring CAD
- Finish Accumulator
- Improved HV Boards
### Other
- Early Submits for ESFs etc. [Deadlines](https://www.formula-hybrid.org/deadlines)
- Pre-Event Eletrical Review [Only info found](https://www.formula-hybrid.org/volunteer)
- Sponsors
    - Connectors / harnesses
    - PCB manufacturing

## High Voltage
### Module Assembly
- **Fuses:** Figure out a new fuse situation. We will have to do a lot of testing on what material to use (copper) and then endurance testing to see if they will become undone under different forces. 
    - In order to test fuses we also need to fix our fuse rig.
- **Thermistors:** Done — they just need to be glued to each module.
- **Spotwelding:** Once we find new fuses, spotweld them to busbars, then spotweld the segment to the cells.
- **Busbars:**
    - Create new thin busbars?
    - We have the materials for thick busbars — just need to bend them and put them into the modules.
- **Thermal bonding:** Bond the thermistors to the thin busbars once they are spotwelded on.
- **BMS testing:** Once the modules are complete, test that we can read temperature data from the Orion BMS 2. Readings were already obtained with code on the BMS expansion boards — we just need to confirm they are accurate for each module.

### Finish the Mid-Box
- **Fix two errors on the TSSI and Precharge boards:**
    - TSSI components need to be galvanically isolated (the connector going from the board to the TSSI lights).
    - Precharge has a logic error that needs to be resolved.
- **TSSI Lights:** Make TSSI lights that actually work.
- **Wiring & documentation:** Finish wiring everything up, then create a schematic of the entire mid-box wiring for documentation purposes.

### Finish Top Cover / Rest of Box
- **Nomex insulation:** Already cut — just need to epoxy it to the walls of the accumulator housing.
- **Top cover insulation:** Either get more insulation paper for the top cover or use polycarbonate (the top cover also needs to be insulated).
- **Top cover components:** A few more things need to be added (HVD, TSMP, etc.). 

## Low Voltage

### Gen 2 System Architecture

<img src="LV_Architecture_Diagram.png" alt="LV Architecture Diagram" width="700" />

#### CAN Buses
- **CAN 1:** PCU — Cascadia — BMS — IMD
- **CAN 2:** PCU — Dash — CTU

### Improved practices
- Test points
- 2nd power input path or power over USB on every board
- Central Library Structure
```
FSAE/
├── fsae-kicad-lib/
├── CTU-PCB/
├── PCU-PCB/
├── STM-PCB/
├── Dash-PCB/
└── Steering-PCB/
```

- Firmware updates over CAN (no enclosure opening)
    - Single CAN diag connector on Dash → flashes and sniffs PCU, Dash, CTU from one plug
    - Custom application bootloader on every STM board
        - `BL_ENTER` CAN msg → writes magic value to RTC backup register → `NVIC_SystemReset()` → bootloader sees magic, stays in update mode until flash success or `BL_EXIT` CAN msg.
        - Backup: on every reset, bootloader listens on CAN for ~300 ms; if `BL_ENTER` heard, stays in update mode. Covers bricked / hung apps via LV master cycle
        - Per-board CAN node ID in shared header (e.g. `0x10 PCU, 0x11 CTU, 0x12 DASH`)
    - First-flash + recovery: USB and SWD
    - [OpenBLT](https://www.feaser.com/openblt/) as starting point, custom Python flasher with `python-can`

### Project 1: STM32 Core Board
- [STM32G474RET6](https://jlcpcb.com/partdetail/STMicroelectronics-STM32G474RET6/C521608)
    - 170MHz, 512KB flash, 128kB RAM, ARM Cortex-M4F, all peripherals we could possibly need
- CAN Transceivers
    - Protection
    - Termination jumper / switch
- Oscillator
- 3V3 (and 5V) Power + Protection
    - 12V to 5V Conversion and 5V to 3V3 conversion
        - 2 x [LMR33630](https://jlcpcb.com/partdetail/TexasInstruments-LMR33630AQRNXRQ1/C1850374)
            - just needs different passive components for different output voltages: [Datasheet](https://www.ti.com/lit/ds/symlink/lmr33630-q1.pdf?ts=1778219527300&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FLMR33630-Q1%252Fpart-details%252FLMR33630AQRNXRQ1)
- SWD header (Tag-Connect TC2030 footprint — pads only, for first-flash + bricked-bootloader recovery without opening enclosures)
- SD-Adapter
- Status LEDs
- Reset and bootmode control (NRST button, BOOT0 pulldown + recovery button — only used until app bootloader is on the chip)
- USB-C 
- Power MUX
    - [TPS2121](https://jlcpcb.com/partdetail/TexasInstruments-TPS2121RUXR/C485916)
- Board-to-Board connectors
    - [Plug - Underside of this board](https://jlcpcb.com/partdetail/HRS_Hirose-DF9_25P_1V_32/C2692087)
    - [Socket - Topside of carrier boards](https://jlcpcb.com/partdetail/HRS_Hirose-DF9_25S_1V_32/C3649128)
- Footprint to use in next boards
- Standoffs

### Project 2: Development / Testing Board
- All the peripherals we have in screw or header terminals

### Project 3: Central Telemetry Unit
- Add headers and test modules on breadboard
- PCB
    - STM Core
    - SMD modules (same modules/ICs as in current design)
        - Except for GPS since no modules with IPEX connector easily available
            - Use this one we bought: [Adafruit Ultimate GPS Breakout](https://www.adafruit.com/product/5440)
            - [Reference Image for making footprint](https://github.com/NYU-Formula-SAE-Electronics/CTU-PCB/blob/main/Ref%20Images/gps-module.png)
        - Lora: [RAK3172-9-SM-I](https://jlcpcb.com/partdetail/RAKwireless-RAK3172_9_SMI/C19723905)
        - IMU: [BMI088](https://jlcpcb.com/partdetail/BoschSensortec-BMI088/C194919)
    - Connector
        - Power (2), CAN (2) = 4 pin
        - Connectors for suspension travel sensors (4x3 pins) and Steering angle (6 pins) (probably won't have the sensors in the car until 27-28 season unless there's extra time and money)
- Enclosure

### Project 4: PCU Gen 2
- STM Core
- Split connector
    - Brake (6 pin)
    - Accelerator (6 pin)
    - Wheel Speed Sensors (4x3 or maybe 2x6)
    - Power (2), Regen (2), RTDS (2), RTDB (2) = 8
    - CANs (4), Brake Pressure Sensors (4)
    - Extra Signals (4)
- LEDs actually this time
- Louder RTDS
- Find Brake pressure sensor
- Sensor filter circuit development, see [PCU Gen 2](./pcu-gen-2.md)
- Enclosure

### Project 5: Dash
- STM Core
- Display
    - https://newhavendisplay.com/7-0-inch-ips-eve-tft-lcd-module-without-touchscreen/
    - Get them to sponsor with sample(s)
- Connectors
    - Display (20 pin latching box header)
    - Power (2)
    - CAN (2 in, 2 out?)
    - Steering Wheel Board (10)
    - CAN diag port (CAN2: CAN_H, CAN_L, GND, +12V) — panel mount on enclosure for in-place firmware flashing of PCU / Dash / CTU. 
- On-board buttons
- Radio connector? leave full implementation to next year
- CAD
    - Talk to Mina Shafik and Ray about placement, mounting, allocated space
    - Add LV system control switches, etc. to enclosure front plate

### Project 5.1: Steering Wheel (Dash peripheral, no MCU)
- Radio Button?
- Display navigation buttons
- Regen dial
- Power dial
- Find Waterproof Buttons
    - [One option with multiple colors](https://www.tinysineaudio.com/products/waterproof-momentary-push-button-panel-mount-12mm?variant=51156643414326)
- Connectors
    - Power, button signals (2+8?)
- Quick Release mechanism
    - Ideally, Lemo or Pegasus connector, but we can find cheaper
    - Ask for samples or sponsorship
- Body CAD (talk to Mina Shafik)

### (Project 6: CAN Watchdog)
- Confirm with judges whether needed
- Rules say: "If CAN communication are used for safety functions, a relay controlled by an independent CAN watchdog device that opens if relevant CAN messages are not received. This relay is not required to be latching."
- STM Core
- Watchdog IC

## Timeline
### May:
- Connector companies (sponsor/sample) → move all board designs from dead point
- Contact New Haven Display company
- Confirm allocated space on dashboard and roll hoop
### June:
- STM Core board → first board to make once connectors thing resolved
    - PCBWay Sponsorship
- PCU 
    - filter circuit decision for Gen 2 (can be done without connectors or STM Core)
    - Gen 2 design → after connector + filter circuit decisions
- CTU board design
    - Breadboard testing
    - SMD component sourcing can be done before STM Core
- Dash & Steering wheel Boards
### July:
- Design reviews by Ufuk and Andres
- STM Core & Dev board first to prod (Early July)
- PCU, CTU, Dash ready for prod after Core design locked in (Late July)
### August:
- Wiring 
    - CAD (collaborate with Mechs), Export lengths
    - Lengths & Gauges table
- Enclosure CADs
### Fall Semester:
- Manufacturing
- Testing
- Firmware

