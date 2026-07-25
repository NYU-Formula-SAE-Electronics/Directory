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
- Read *entire* relevant sections of datasheets

## High Voltage
- IMD: Bender iso165C-1
- BMS: Orion 

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

<img src="Low-Voltage/LV_Architecture_Diagram.png" alt="LV Architecture Diagram" width="700" />

### [Details of Projects](gen-2-architecture.md)

#### CAN Buses
- **CAN 1:** PCU — Cascadia
- **CAN 2:** PCU — Dash — CTU - IMD - BMS
- **CAN 3** Dash – Steering Wheel

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
- STM Core & Dev board & Steering wheel knob translucent print thingy first to prod (Late June)
-> Dash & Steering wheel CAD to begin
### July:
- PCBs & Prints arrive July ~10th 
- Initial firmware bring up & validation by ~15th
-> PCU, CTU, Dash & Steering wheel ready for prod after Core design validated (Late July)
    - Dash & Steering in particular shouldn't go into prod before CAD is at a mature stage
- Start putting together Wiring Master Schematic (Late July)
    -> Need to know wire sizes & cable types for reaching out to companies for sponsored cables
### August:
- Above PCBs arrive ~Mid-August
- Wiring 
    - Finish Schematic sheet ~Mid to Late August
        - Symbols are boards and sensors
        - Connections between them represent cables
    - CAD with David & Ray
    - Export lengths
    - Lengths & Gauges table
- Enclosure CADs
### September:
- Harnesses
    - PCU -> Pedal sensors
        - Six Pins at PCU end -> Y-split for 5v & Ground & 2 signal lines for each sensor
    - PCU -> Brake pressure sensor & Brake cutoff valve
        - 3 pins both ends
    - PCU -> Front Wheel Speed Sensors
    - PCU -> Rear Wheel Speed Sensors
    - PCU -> Dashboard 
        - CAN2 
            -> Split near dashboard for CTU
    - Dashboard -> Steering Wheel
    - CTU 
        - 12V & GND
        - CAN 2
    - Cascadia logic harness
        - Bunch of cables to motor
        - CAN
What order does it make the most sense to make these?
Order in which we want the low voltage system come to life:
- Core V1 & Dev-Test 
    - Order
    - Testing
    - Initial Feature Development
        - CAN
        - Bootloader
    - Send to NYC
    -  
        - Display Development
        - Rotary Sensor Development
    - 


- As wire harnesses get built
    - Test firmware & harness integrity through bench testing
### October:
- 
### November
-
### December

### January

### February

### March
- 
### April
- Finalize cloud ui
- ~ 25th Competition


Project based view
- HV 
    - Accumulator
        - Modules
            - Fuses
                - Design
                - Validation
                - Manufacturing
                    - Get quote SendCutSend & elsewhere if needed
        - Enclosure
            - CAD
            - Get Aluminum
            - Cut
            - Assemble
    - System Wiring
    - Safety Circuit
    - Firmware
- **LV** 
    - Nodes
        - PCBS
            - Hydra core
                - Order 07/15
            - Dev-test
                - Order 07/15
            - Dash
                - Schematic 07/14
                - PCB 07/31
                - Finalize Panel LEDs
                - Order 08/15 *(Depends on: Enclosure CAD)*
            - Steering Wheel
                - Schematic 07/14
                - PCB 07/31
                - Order 08/15 *(Depends on: Enclosure CAD)*
            - CTU
                - Schematic 07/31
                - PCB 08/15
                - Order 08/31
            - Comms
                - Schematic 07/31
                - PCB 08/15
                - Order 08/31
            - VCU
                - Schematic 07/31
                - PCB 08/15
                - Order 08/31
        - Enclosures
            - Dashboard
                - CAD 09/15
                    - Shape & space allocation 08/01
                    - Front & Back drafts 09/01
                    - Details 09/15
                - FDM V1 10/01
                - MJF V2
                    - Order 10/15 *(Depends on: Final Dash PCB & FDM V1)*
            - Steering Wheel
                - CAD 09/15
                    - Shape & space allocation 08/01
                    - Front & Back drafts 09/01
                    - Details 09/15
                - FDM V1 10/01
                - MJF V2
                    - Order 10/15 *(Depends on: Final SW PCB & FDM V1)*
            - VCU, CTU, Comms
                - CAD 10/01
                    - Shape & space allocation 09/01 *(Depends on: PCB Layouts)*
                    - Front & Back drafts 09/15
                    - Details 10/01 *(Depends on: Final PCBs)*
                - FDM V1 10/15
                - Possibly FDM V2 11/01
    - Sensors
        - Pedal Position
            - Contact Honeywell 07/31
        - Brake pressure
            - Waiting for Haltech sponsorship
        - Suspension travel
            - Find cheaper/sponsored option 08/15
        - Steering Angle
            - Find cheaper/sponsored option 08/15
        - Wheel Speed
            - Contact Littlefuse
    - System Wiring
        - Master Schematic 07/31
        - Spreadsheet 08/05
            - Connectors
                - Part Links
            - Crimps
                - Part links
            - Gauges
            - Lengths *(Depends on: Wiring CAD)*
            - Cables
                - Part Links
        - CAD 10/01
        - Order 09/15
            - Connectors
            - Crimps
            - Cables
            - Heatsink if needed
    - Mounting
        - Nodes
        - Fusebox
        - Battery
    - Software
        - Firmware
            - Common
                - CAN & Bootloader 08/13
                - SD card 08/31
                - Status LED 08/31
            - Dash
                - Basic UI 08/22
                - Button Controls 08/31
                - Fault LEDs 09/07 *(Depends on: Final LED choice)*
            - VCU
                - Rotary sensor read 09/01
        - Backend (Spring)
            - Architecture
            - Setup EC2
            - Setup API Gateway
            - Setup DB
            - Texture CAD
            - Rig CAD
            - Frontend
- Administrative
    - 