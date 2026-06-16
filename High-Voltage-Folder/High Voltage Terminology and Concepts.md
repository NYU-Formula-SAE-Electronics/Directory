# High Voltage Terminology and Concepts

**Intro:** This list is a compilation of very important high voltage concepts that I think every new member should try to learn and understand. It will most likely grow and get better as time goes on, but this is just a starting point.

---

**Accumulator** — Large energy <img width="6048" height="8064" alt="IMG_8462" src="https://github.com/user-attachments/assets/287c98f8-c850-4482-a8be-70f875f92fd9" />
storage device that contains smaller accumulator modules (6), each filled with battery cells (84 each) and a team-made BMS Expansion Board.

<img width="1710" height="493" alt="image" src="https://github.com/user-attachments/assets/8b179092-be88-477f-a562-59a209bd6965" />

**Accumulator Segment** — A singular module of the accumulator that contains its own BMS and battery cells. We use Samsung 25R 18650 2500mAh 20A battery cells.

<img width="760" height="772" alt="image" src="https://github.com/user-attachments/assets/82e31a61-87c9-4b98-b925-54bf61b526d3" />

**AMS and BMS** — (Accumulator Management System and Battery Management System; terms are interchangeable.) This is a device that monitors each cell in the accumulator and ensures that they are operating safely below a set temperature, current, and voltage.

**Barrier** — A rigid material that resists a flow of charge. Used to provide a structural barrier and increase distance between two conductors.

**BRB (Big Red Button)** — A large red button on the side of the car that shuts down the electrical systems.

<img width="6048" height="8064" alt="IMG_8462" src="https://github.com/user-attachments/assets/ba5137fe-d12c-4159-9326-59bbc45bc2fa" />

**Creepage Distance** — The minimum required (shortest) distance measured along the surface of the insulating material between two conductors.

<img width="938" height="442" alt="image" src="https://github.com/user-attachments/assets/339a1ea2-1cd0-440d-88da-330976773ace" />

**Drive Motor (Emrax 228)** — A 3-phase AC motor that requires an inverter to convert our DC energy from the accumulator into 3-phase AC. This is what makes the wheels spin by converting electrical energy into mechanical energy.

<img width="696" height="363" alt="image" src="https://github.com/user-attachments/assets/2d19de51-f6e3-4067-ac03-4a42788ed899" />

**Inverter (Cascadia Motion CM200DZ)** — This is our inverter and motor controller for the Emrax 228. This is where DC power from the accumulator is converted to AC. In the precharge circuit, this is modeled as a big capacitor.

<img width="423" height="281" alt="image" src="https://github.com/user-attachments/assets/4e8ab436-e480-4226-b897-ac5859c0bf96" />

**Enclosure** — An insulated housing containing electrical circuitry.

**GLV (Grounded Low Voltage)** — Every conductive part that is not part of the tractive system. Instead of being powered by accumulator power, power is supplied by a 12V LiFePo4 battery.

**GLVMS (Grounded Low Voltage Master Switch)** — This switch is the highest-priority shutdown switch and will shut down power to ALL GLV electrical circuits.

**Ground Fault** — A fault that occurs when electric current bypasses the intended circuit and goes directly to ground. This can happen if an exposed wire comes into contact with a conductive surface. Poses a safety risk. The IMD monitors this.

<img width="646" height="557" alt="image" src="https://github.com/user-attachments/assets/5c7c5821-06ec-466d-a77c-524eaa827ccc" />

**IMD (Insulation Monitoring Device)** — Another safety device located in the accumulator Mid-Box, like the BMS. It monitors for ground faults and will open accumulator relays if tripped.

**Insulation** — Any material that physically resists flow of charge. We use insulation in various situations; for example, in the accumulator we have Nomex Insulation Paper used to cover the interior walls.

**Isolation** — The separation of electrical systems to prevent any conduction. Various methods achieve this, including physical separation of wires and of the electrical systems themselves. On PCB boards this includes keeping certain high voltage components away from the low voltage ones. You can also achieve this with conformal coating: say you have some conductive material that is exposed; applying conformal coating basically encapsulates this material in another material with extremely strong dielectric strength, preventing conductive threats. In short, it is just isolation between two or more electrical conductors that prevents current from flowing if a voltage potential exists between them.

**Separation** — Physical distance between conductors.

**SMD (Segment Maintenance Disconnect)** — A component that is installed on each accumulator module/segment and is used to connect and disconnect each module. This is so we can take out modules to service and do maintenance on the accumulator.

<img width="911" height="533" alt="image" src="https://github.com/user-attachments/assets/9688605c-c439-4e13-b6a3-f6d81f685ab8" />

**Tractive System** — All of the parts of the high voltage system that are outside the accumulator after the main contactors. This includes the drive motors, the accumulator itself, and anything connected to those components.

**TSSI (Tractive System Status Indicator)** — PCB that indicates if the tractive system voltage is greater than 60V.

<img width="713" height="432" alt="image" src="https://github.com/user-attachments/assets/7cd3e1e6-9278-4eaa-ada9-17c93409ddd6" />

**Orion BMS 2** — This is the BMS that we use. It is not team-made; it is made by an outside company.

<img width="542" height="261" alt="image" src="https://github.com/user-attachments/assets/af36448a-52ac-4cdd-a49d-3880005349c8" />


**BMS Expansion Boards** — Our custom PCB made to interface between the cells and the Orion BMS 2. Instead of buying expansion modules, these were made to monitor the temperatures and voltages of cells using thermistors and voltage cell taps.

<img width="780" height="163" alt="image" src="https://github.com/user-attachments/assets/e262fedf-22bc-49f8-bedf-0d1bc4a11e60" />


**Precharge Board** — Circuit designed to prevent damage to tractive system components. When you connect the accumulator to the tractive system components, current will spike and immediately rush to the rest of the system, which can cause damage. This circuitry is designed to prevent that spike and gradually bring the voltage difference up.

<img width="756" height="408" alt="image" src="https://github.com/user-attachments/assets/25cb0d01-1c2e-4c73-884d-737d95526032" />


---
