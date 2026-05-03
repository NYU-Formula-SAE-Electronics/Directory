# 2026 - 2027 Season
**A year is a surprisingly short time**
**Test before committing & make testing easy**

# Priorities
- Sponsors
    - Connectors / harnesses
    - PCB manufacturing
- Migration to KiCad & GitHub
    - Centralized library for shared components

## High Voltage


## Low Voltage

- Shift to STM32
- Improved practices
    - Shared implementations & practices
        - Shared STM core?
        - Power architectures
        - CAN Transceiver design
        - Connector pinouts
        - on-board hardware tied reset buttons
    - Test points
    - Screw terminals / headers for testing & debugging
    - 2nd power input path or power over usb on every board

- CTU: Same architecture, better packaging
    - Add headers and test modules on breadboard
    - STM MCU
    - SMD modules (same modules as in current design)
    - Connector(s)
        - Power (2), CANs (4), extra (4)
    - Buttons
    - Enclosure

- PCU Gen 2.
    - STM core
    - Split connector
        - Brake (6 pin)
        - Accelerator (6 pin)
        - Power (2), Regen (2), RTDS (2), RTDB (2)
        - CANs (4), Brake Pressure Sensors (4)
        - Extra Signals (4)
    - LEDs actually this time 
    - New Enclosure
        - Transparent lid 
    - CAN Watchdogs
        - Source
        - Mounting?

- Dash
    - STM core or copied implementation
    - Connectors
        - Display (FPC)
        - Power (2)
        - CANs (4)
        - Steering Wheel Board (10)
    - On-board buttons
    - Radio connector? leave full implementation to next year
    - CAD
        - Talk to Mina Shafik and Ray about placement, mounting, allocated space
        - Add LV system control switches, etc. to enclosure front plate

- Steering Wheel
    - Radio Button?
    - Display navigation buttons
    - Regen dial
    - Power dial
    - Connectors
        - Power, button signals (2+8)
    - Quick Release mechanism
        - Ideally, Lemo or Pegasus connector, but we can find cheaper
    - Body CAD (talk to Mina Shafik)    
