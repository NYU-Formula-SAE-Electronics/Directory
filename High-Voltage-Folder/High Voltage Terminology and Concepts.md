# High Voltage Terminology and Concepts

**Intro:** This list is a compilation of very important high voltage concepts that I think every new member should try to learn and understand. It will most likely grow and get better as time goes on, but this is just a starting point.

---

**Accumulator** — Large energy storage device that contains smaller accumulator modules (6), each filled with battery cells (84 each) and a team-made BMS Expansion Board.
<div align="center">
<img width="1633" height="471" alt="image" src="https://github.com/user-attachments/assets/4e917dee-5196-45b2-a3c9-a1561093cfac" />
</div>

**Accumulator Segment** — A singular module of the accumulator that contains its own BMS and battery cells. We use Samsung 25R 18650 2500mAh 20A battery cells.

<div align="center">
<img width="520" height="577" alt="image" src="https://github.com/user-attachments/assets/6a0cea30-ba4f-486f-98f8-5db0af526c77" />
</div>

**AMS and BMS** — (Accumulator Management System and Battery Management System; terms are interchangeable.) This is a device that monitors each cell in the accumulator and ensures that they are operating safely below a set temperature, current, and voltage.

**Barrier** — A rigid material that resists a flow of charge. Used to provide a structural barrier and increase distance between two conductors.

**BRB (Big Red Button)** — A large red button on the side of the car that shuts down the electrical systems.
<div align="center">
<img width="400" height="533" alt="IMG_8462" src="https://github.com/user-attachments/assets/ba5137fe-d12c-4159-9326-59bbc45bc2fa" />
</div>

**Creepage Distance** — The minimum required (shortest) distance measured along the surface of the insulating material between two conductors.
<div align="center">
<img width="730" height="228" alt="image" src="https://github.com/user-attachments/assets/dcc021d9-c2df-4650-9565-da43d29fa43d" />
</div>

**Drive Motor (Emrax 228)** — A 3-phase AC motor that requires an inverter to convert our DC energy from the accumulator into 3-phase AC. This is what makes the wheels spin by converting electrical energy into mechanical energy.
<div align="center">
<img width="552" height="286" alt="image" src="https://github.com/user-attachments/assets/5eb894ed-5d20-4f99-83eb-9519c7ef0df9" />
</div>

**Inverter (Cascadia Motion CM200DZ)** — This is our inverter and motor controller for the Emrax 228. This is where DC power from the accumulator is converted to AC. In the precharge circuit, this is modeled as a big capacitor.
<div align="center">
<img width="325" height="230" alt="image" src="https://github.com/user-attachments/assets/c3b45fc7-12d1-47b2-bf3d-5ad1acc9f5bd" />
</div>

**Enclosure** — An insulated housing containing electrical circuitry.

**GLV (Grounded Low Voltage)** — Every conductive part that is not part of the tractive system. Instead of being powered by accumulator power, power is supplied by a 12V LiFePo4 battery.

**GLVMS (Grounded Low Voltage Master Switch)** — This switch is the highest-priority shutdown switch and will shut down power to ALL GLV electrical circuits.

**Ground Fault** — A fault that occurs when electric current bypasses the intended circuit and goes directly to ground. This can happen if an exposed wire comes into contact with a conductive surface. Poses a safety risk. The IMD monitors this.
<div align="center">
<img width="587" height="438" alt="image" src="https://github.com/user-attachments/assets/ddcb5ce0-b198-457b-bcb1-02351e812ecd" />
</div>

**IMD (Insulation Monitoring Device)** — Another safety device located in the accumulator Mid-Box, like the BMS. It monitors for ground faults and will open accumulator relays if tripped.

**Insulation** — Any material that physically resists flow of charge. We use insulation in various situations; for example, in the accumulator we have Nomex Insulation Paper used to cover the interior walls.

**Isolation** — The separation of electrical systems to prevent any conduction. Various methods achieve this, including physical separation of wires and of the electrical systems themselves. On PCB boards this includes keeping certain high voltage components away from the low voltage ones. You can also achieve this with conformal coating: say you have some conductive material that is exposed; applying conformal coating basically encapsulates this material in another material with extremely strong dielectric strength, preventing conductive threats. In short, it is just isolation between two or more electrical conductors that prevents current from flowing if a voltage potential exists between them.

**Separation** — Physical distance between conductors.

**SMD (Segment Maintenance Disconnect)** — A component that is installed on each accumulator module/segment and is used to connect and disconnect each module. This is so we can take out modules to service and do maintenance on the accumulator.
<div align="center">
<img width="725" height="443" alt="image" src="https://github.com/user-attachments/assets/602c550a-9315-4bd5-9a8e-6b08a895ec92" />
</div>

**Tractive System** — All of the parts of the high voltage system that are outside the accumulator after the main contactors. This includes the drive motors, the accumulator itself, and anything connected to those components.

**TSSI (Tractive System Status Indicator)** — PCB that indicates if the tractive system voltage is greater than 60V.
<div align="center">
<img width="552" height="317" alt="image" src="https://github.com/user-attachments/assets/14664ae7-c4d2-4e5b-9b21-fb1ff628129f" />
</div>


**Orion BMS 2** — This is the BMS that we use. It is not team-made; it is made by an outside company.
<div align="center">
<img width="572" height="307" alt="image" src="https://github.com/user-attachments/assets/dfd67363-4235-4b2c-be2d-1ff03db9420e" />
</div>

**BMS Expansion Boards** — Our custom PCB made to interface between the cells and the Orion BMS 2. Instead of buying expansion modules, these were made to monitor the temperatures and voltages of cells using thermistors and voltage cell taps.
<div align="center">
<img width="891" height="192" alt="image" src="https://github.com/user-attachments/assets/983e9dc1-46bd-49ea-be47-689b9fc9e524" />
</div>

**Precharge Board** — Circuit designed to prevent damage to tractive system components. When you connect the accumulator to the tractive system components, current will spike and immediately rush to the rest of the system, which can cause damage. This circuitry is designed to prevent that spike and gradually bring the voltage difference up.
<div align="center">
<img width="756" height="408" alt="image" src="https://github.com/user-attachments/assets/25cb0d01-1c2e-4c73-884d-737d95526032" />
</div>

---
