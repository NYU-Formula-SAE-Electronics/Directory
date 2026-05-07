# Team Practices for PCB Design in KiCad
**Learning from three years and nine PCB projects boiled down to one document.**

## Using the shared component library: [fsae-kicad-lib](https://github.com/NYU-Formula-SAE-Electronics/fsae-kicad-lib)
### Directory Structure
On your local machine, keep team KiCad work under one parent folder, for example:
```
FSAE/
├── fsae-kicad-lib/
├── CTU-PCB/
├── PCU-PCB/
└── ...
```
### Sourcing Components
- In the interest of time, this season we'll try to get everything pre-assembled to maximum extent. Knowing SMD assembly by hand is a good skill to have but takes a huge amount of time and is prone to errors. 
- Component sourcing from Digikey and Mouser is slow and the components are not always available at JLC and PCBWay (our primary manufacturing companies). They have their own inventories and are connected to LCSC (Chinese version of Digikey)

1. Make sure the latest commit of our library is on your machine before adding new parts
    - First time use:
    - `cd FSAE`
    - `git clone fsae-kicad-lib`
    - Otherwise:
    - `cd FSAE/fsae-kicad-lib`
    - `git pull origin main`
2. Source components as much as possible from [JLCPCB.com/parts](https://jlcpcb.com/parts)
    - Choose well-stocked components (ideally 100+ in stock), sort by decreasing stock count
    - Make sure when you click "PCB Footprint or Symbol" there is a symbol and footprint available
3. Once you have your component selected:
    - Install **easyeda2kicad** on the command line:
        - MacOS: `python3 -m pip install easyeda2kicad`
        - check that it got installed with: `easyeda2kicad --help`
    - In the fsae-kicad-lib folder: (`cd FSAE/fsae-kicad-lib`)
        - `easyeda2kicad --full --lcsc_id=C123456 --output ./fsae` (the part id (starts with C) marked as JLCPCB Part # in jlcpcb.com/parts)
4. Commit to the repo sooner rather than later so you don't forget
    - `git add .`
    - `git commit -m "added CAN Transceiver IC`
    - `git push origin main`
5. In the KiCad project the `fsae` needs to be added as a project specific library. That's why it's important the Kicad project file and library paths stay unchanged. 
    - When you choose Place Symbol (A) in KiCad Schematic Editor and look for the library called fsae, the part should be visible there.

If we'll have a situation with a lot of people working on projects at the same time, we'll switch to a more robust branching system but that's an overkill currently.

## Standard Design Practices
- Board shape and size
    - Do your best to keep it under 100x100mm. They're quite a bit cheaper to make under that threshold. (How doable this is depends on how big the STM Core Board and our connectors will be, so we'll see)
    - Round corner with 6mm radius.
- Mounting Holes
    - M3 (3.2mm) Non plated holes (available in default KiCad library)
    - Place near corners if possible in a way that center point is the same as with rounded edge-cut arc. This way the distance from hole edge to board edge in the corner is consistent.
- Standard Layer Stackup (4 Layer boards)
    - Top Layer (Signals, Components, Ground Pour at the end)
    - GND
    - Power
    - Bottom Layer (Signals, Ground Pour at the end).
        - Avoid placing components on the bottom side, except for through hole components that we know we'll solder ourselves. Bottom layer assembly can get costly.
- Vias
    - Minimum size: 0.2/0.45mm
    - Standard size: 0.3/0.6mm
    - For 500mA+ currents use 0.4/0.8mm or 0.5/1.0mm. Place multiple if space permits and current demand is high. 
    - For 2A+ currents use [Via Current Calculator](https://camptechii.com/tools-pcb-via-calculator/) to make sure your design is sound.
- Traces
    - No unnecessary turns, curves, etc. Keep it clean.
    - No sharp 90 degree turns.
    - Widths:
        - Absolute minimum: 0.15mm (We shouldn't need this)
            - If an IC has 0.15mm width pads then it's ok but switch to a wider trace once there's space.
        - Standard for signals: 0.2mm and up. Go for 0.3mm if you can. 
        - Increase as needed for high current traces
            - Use [Trace Width Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-pcb-trace-width)
                - 1 oz layer thickness
                - I usually use 10C temperature rise and 20C ambient temperature (depends on case)
            - As a rule of thumb, just opt for thicker traces where current will be high. We have the space, this isn't consumer electronics we're building.
- Passive Component Packages
    - 0603 for small capacitors and resistors, it's big enough to replace by hand and place probes on easily. 
    - 0805 and up for big capacitors and if smaller packages are expensive or unavailable.
    - Opt away from 0402 and smaller. Again, we have the space for bigger ones.
- Connectors
    - Until we have a connector sponsor locked in use generic X pin connector schematic symbols from KiCad's own library.
    - Keep on one edge of the board and the faces that touch the inner wall of enclosure aligned. This makes enclosure design much easier.
        - For USB-C connectors put them on the opposite edge from all other connectors.
- Clearances
    - Absolute Minimum: 0.1mm (stay away from this)
    - Preferred: 0.2mm and up.
    - Keep spacing even and consistent: If you have a trace going between two pads and the distance to the other one is 0.15mm and 0.65m to the other one, you're doing it wrong.
    - Component to board edge: 0.5mm absolute minimum, 2mm+ preferred
    - Refer to [JLCPCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities) or [PCBWay Capabilities](https://www.pcbway.com/capabilities.html) when needed.
- Silkscreen
    - Include the text NYU FSAE and the logo on every board
    - Board name and generation
    - Check that there are no overlapping silkscreens with one another or with any pads

## Design Reviews
- Make sure your design follows the practices laid out above.
- Also recommended to (re)watch the [PCB Design Tips](https://www.youtube.com/watch?v=kkc8BxL5Eo0) and [PCB Design Mistakes](https://www.youtube.com/watch?v=D0X76Kbf8fQ) at least when working on your first board.
- Submit your project for review in four stages (just push to Github and DM/text Veikko asking to review)
    - Schematic done
    - Board shape, stackup, and component layout done
    - Routing done
    - Via stiching, silkscreen, etc. final shit before manufacturing
        - Also before this review export gerbers, drill files, component placement file, and BOM from KiCad and upload to JLCPCB to make sure everything looks good there as well.
- It's many reviews but this will save you from having to worst-case redo the whole board. Once you're trusted that you know what you're doing, we'll just do a final review before sending to production.
