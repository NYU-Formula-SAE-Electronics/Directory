
# Dev-Test Board

The purpose of the board is to easily interface with the STM Core and test its functionality while also being able to effectively act as the PCU and Dash PCB. 

### Outline
- 100mm x 100mm

### Passive components
- 3 ADC channels need voltage dividers (10k & 15k resistors and 10nF cap by the 15k resistor to ground)
- Dashboard emulation tactile switches
    - There's already a component for these in the library used for boot and reset buttons on the STM Core
    - 4 x arranged in a diamond (for up, down, left, right)
        - Place arrows on the silkscreen somewhere close
    - 2 x placed in a row or column somewhere close (for enter and back)
        - Place silkscreen text for them somewhere close

### I/O
- 8 pin connector: AMPSEAL series https://www.te.com/en/product-776280-1.html
- 12 pin connector: Deutsch DTM series	https://www.te.com/en/product-DTM15-12PA.html
    - Footprints might be able to find from JLC parts and fetched with the easyeda2kicad cli tool. If they're not available, digikey will most likely have them. More complicated to add to shared lib but doable.
- Display Connector (20 pin 2.54mm pitch box connector)
    - Display datasheet for the exact type and pinout: https://newhavendisplay.com/content/specs/NHD-7.0-800480FT-CSXV-T.pdf
    - Double check the orientation is correct for plugging in the display without crashing with the STM Core
    - See the display's mechanical drawings in the datasheet for aligning standoffs correctly. Add M3 mounting holes on the board accordingly.
- Screw terminals
    - 3 x 2 pin connectors for power (12V & GND, 5V & GND, 3.3V & GND)
    - 2 x 2 for can buses

    


