# 2026 - 2027 Season
**1. One year is a surprisingly short time**
**2. Test before committing & make testing easy**
**3. KISS: Keep it simple, Stupid**

## Priorities
- Sponsors
    - Connectors / harnesses
    - PCB manufacturing
- Migration to KiCad & GitHub (LV)
    - Centralized library for shared components
- Finish Accumulator
- Improved HV Boards
- New LV Architecture

## High Voltage

## Low Voltage

### Gen 2 System Architecture

![LV Architecture Diagram](LV_Architecture_Diagram.png)

#### CAN Buses
- **CAN 1:** PCU -> Cascadia -> BMS -> IMD
- **CAN 2:** PCU -> Dash -> CTU

### Improved practices
- Test points
- 2nd power input path or power over USB on every board

### Project 1: STM32 Core Board
- [STM32G474RET6](https://jlcpcb.com/partdetail/STMicroelectronics-STM32G474RET6/C521608)
    - 512kB Flash, 128kB RAM, all peripherals we could possibly need
- CAN Transceivers
    - Protection
    - Termination jumper / switch
- Oscillator
- 3V3 (and 5V) Power + Protection
- SWD header
- SD-Adapter
- Status LEDs
- Reset and bootmode control
- USB-C (+alt power path)
- Board-to-Board connectors

### Project 2: Development / Testing Board
- All the peripherals we have in screw or header terminals

### Project 3: Central Telemetry Unit
- Add headers and test modules on breadboard
- PCB
    - STM Core
    - SMD modules (same modules as in current design)
    - Connector
        - Power (2), CANs (4), extra (4) = 10 pin
- Enclosure

### Project 4: PCU Gen 2
- STM Core
- Split connector
    - Brake (6 pin)
    - Accelerator (6 pin)
    - Wheel Speed Sensors (3x4 or maybe 2x6)
    - Power (2), Regen (2), RTDS (2), RTDB (2) = 8
    - CANs (4), Brake Pressure Sensors (4)
    - Extra Signals (4)
- LEDs actually this time
- New Enclosure
    - Transparent lid

### Project 5: Dash
- STM Core
- Display
    - https://newhavendisplay.com/7-0-inch-ips-eve-tft-lcd-module-without-touchscreen/
    - Get them to sponsor with sample(s)
- Connectors
    - Display (20 pin latching box header)
    - Power (2)
    - CANs (4)
    - Steering Wheel Board (10)
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
