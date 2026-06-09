# Gen 2 System Architecture

<img src="LV_Architecture_Diagram.png" alt="LV Architecture Diagram" width="700" />


### Project 1: STM32 Core (Hydra)
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
    - [Plug - Underside of this board](https://jlcpcb.com/partdetail/PANASONIC-AXK530147YG/C6508367)
    - [Socket - Topside of carrier boards](https://jlcpcb.com/partdetail/PANASONIC-AXK630347YG/C3640562)
- Footprint to use in next boards
- Standoffs

### Project 2: Development / Testing Board (Nathan & Altan)
- See [Dev-Test-PCB](dev-test-pcb.md)

### Project 3: Central Telemetry Unit (Kenneth & Porter)
- Add headers and test modules on breadboard
- PCB
    - STM Core
    - SMD modules (same modules/ICs as in current design)
        - Except for GPS since no modules with IPEX connector easily available
            - Use this one we bought: [Adafruit Ultimate GPS Breakout](https://www.adafruit.com/product/5440)
                - Pinout to MCU:
                    - Fix -> 
                    - PPS ->
                    - TX -> 
                    - RX <- (9600 baud)
            - [Reference Image for making footprint](https://github.com/NYU-Formula-SAE-Electronics/CTU-PCB/blob/main/Ref%20Images/gps-module.png)
        - Lora: [RAK3172-9-SM-I](https://jlcpcb.com/partdetail/RAKwireless-RAK3172_9_SMI/C19723905)
            - Pinout to MCU:
                - UART TX ->
                - UART RX <-
                - RST <-
        - IMU: [BMI088](https://jlcpcb.com/partdetail/BoschSensortec-BMI088/C194919)
            - Pinout to MCU:
                - SDI (MOSI) <-
                - SDO1 & SDO2 (MISO) ->
                - SCK <-
                - CSB1 <-
                - CSB2 <-
    - Connector
        - Power (2), CAN (2) = 4 pin (Using the 8 pin)
        - Connectors for suspension travel sensors (4x3 pins) and Steering angle (3 pins) (probably won't have the sensors in the car until 27-28 season unless there's extra time and money)
            - 2 pins for 5V and GND to the front wheel speed
            - 2 pins for 5V and GND to the steering angle
            - 3 data pins to the front
            - 2 pins for 5V and GND to the back
            - 2 data pins to the back
            = 11 (Total 5x ADC channels on MCU)
- Enclosure

### Project 4: PCU Gen 2 (Stacy & Annie) 
- STM Core
- Split connector
    - Pedal box (6 pin): Brake + Accelerator + Brake Pressure Sensors
        - 4x Analog (2x pedal position, 2x brake pressure), 1x GND (shared), 1x 5V (shared)
        - Split near pedal box to all 4 sensors
        - TO STM total: 6x analog through voltage dividers
    - Wheel Speed Sensors (4 sensors x 3 pins) = 12 pins
        - Front: 
    - Power (2), Regen (2), RTDS (2), RTDB (2) = 8 pins
        - To STM total: 3x digital output
    - CANs (4), Extra Signals (4) = 8 pins
- LEDs actually this time
- Louder RTDS
- Find Brake pressure sensor
- Sensor filter circuit development, see [PCU Gen 2](./pcu-gen-2.md)
- Enclosure

### Project 5: Dash (Sasha & Adriella)
- STM Core
- Display
    - https://newhavendisplay.com/content/specs/NHD-7.0-800480FT-CSXP.pdf
- Connectors
    - Display (20 pin latching box header)
        1 VDD Power Supply Input Voltage for TFT and FT81x (3.3V)
        2 GND Power Supply Ground
        3 SCK MCU SPI Clock (Input) <- From STM
        4 MISO/IO1 MCU SPI MISO (Output) -> To STM
        5 MOSI/IO0 MCU SPI MOSI (Input) <- From STM
        6 /CS MCU SPI Chip Select (Input), Active LOW <- From STM
        7 /INT MCU Interrupt to host (Output), Active LOW -> To STM
        8 /PD MCU Power Down control (Input), Active LOW <- From STM (10k pull up)
        9 AUDIO_L Filter/Amplifier Audio PWM out (Output)
        10 N.C. - No Connect
        11 GPIO0/IO2 MCU General Purpose IO0 / SPI Quad mode: SPI data line 2
        12 GPIO1/IO3 MCU General Purpose IO1 / SPI Quad mode: SPI data line 3
        13 GPIO2 MCU General Purpose IO2
        14 GPIO3 MCU General Purpose IO3
        15 - 16 N.C. - No Connect
        17 - 18 VBL Power Supply Input Voltage for LED Backlight Driver (3.3V/5V)
        19 - 20 GND Power Supply Ground
    - Power (2) + CAN2 (2)
    - Steering Wheel Board: Power + CAN3 (4)
- On-board buttons
    - Display controls
        - UP, DOWN, LEFT, RIGHT
        - BACK, ENTER
    - 6 Digital input to STM
- LEDs
    - IMD
    - BMS
    - 2 Digital Output from STM (possibly through mosfets)
- Radio connector? leave full implementation to next year
- CAD
    - Talk to Mina Shafik and Ray about placement, mounting, allocated space

### Project 5.1: Steering Wheel (Sasha)
- Radio Button?
- Display navigation buttons
    - UP, DOWN, LEFT, RIGHT
    - BACK, ENTER
- Regen knob
    - 1 Analog input to STM
- Power knob
    - 1 Analog input to STM
- Find Waterproof Buttons
    - [One option with multiple colors](https://www.tinysineaudio.com/products/waterproof-momentary-push-button-panel-mount-12mm?variant=51156643414326)
- 4 Pin Connector output ovet telephone cord to Dash
    - [One cable option](https://www.aliexpress.us/item/3256808292859358.html?spm=a2g0o.productlist.main.7.142d5TRz5TRz8J)
- Quick Release mechanism same as last seaason
- Body CAD (Mina, Ray, Yazaan)

### (Project 6: CAN Watchdog)
- Confirm with judges whether needed
- Rules say: "If CAN communication are used for safety functions, a relay controlled by an independent CAN watchdog device that opens if relevant CAN messages are not received. This relay is not required to be latching."
- STM Core
- Watchdog IC

### Flashing over CAN
- Waterproof USB-C port on Hydra
- Hydra mounted close to bottom edge of Dash (hole in dash enclosure for connecting to the port)
- USB-to-CAN bridge on the Dash MCU
    - Laptop plugs into the Dash STM's USB controller, write the firmware for it to act as the bridge between the host (USB) and the shared CAN bus
    - Bridge firmware forwards flasher traffic from USB ↔ CAN
    - The bridge board can also flash itself: host commands it over USB to drop into its own bootloader
- Custom application bootloader on every STM board
    - `BL_ENTER` CAN msg → writes magic value to RTC backup register → `NVIC_SystemReset()` → bootloader sees magic, stays in update mode until flash success or `BL_EXIT` CAN msg.
    - Backup: on every reset, bootloader listens on CAN for ~300 ms; if `BL_ENTER` heard, stays in update mode. Covers bricked / hung apps via LV master cycle
    - Per-board CAN node ID in shared header (e.g. `0x10 PCU, 0x11 CTU, 0x12 DASH`)
- First-flash + recovery: USB and SWD on each board directly
- [OpenBLT](https://www.feaser.com/openblt/) as starting point, custom Python flasher with `python-can` talking through the USB-to-CAN bridge