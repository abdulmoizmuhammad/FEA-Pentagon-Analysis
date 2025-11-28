📘 FEA Analysis: Pentagon Structure Simulation

This project performs a Finite Element Analysis (FEA) on a regular pentagon model. Using Ansys Workbench, we compared:

Static Structural Analysis: Equilibrium response under high load.

Transient Structural Analysis: Time-dependent response under dynamic loading.

Uniquely, all material properties and boundary conditions were derived from personal data (Roll Number, Date of Birth, and Real-time Currency Rates).

⚙️ Simulation Parameters

Parameter

Value

Derivation Logic

Material

Pentagon Moiz

Custom

Young's Modulus

2,000 MPa

Roll No. (1902)

Poisson's Ratio

0.28

Standard

Static Load

2,020 N

D.O.B (04/12/2004)

Transient Load

281.5 N

USD to PKR Rate

Time Step

0.2 s

Fixed Interval

🖥️ Technology Stack

Simulation: Ansys Workbench 2024 R1

Modeling: SpaceClaim / DesignModeler

Verification: Python (for load calculation)

📊 Results Summary

1. Static Structural

Condition: Fixed Support + Remote Force (1/3rd offset).

Outcome: High stress concentration observed at the fixed edge due to the moment arm.

2. Transient Structural

Condition: Time-dependent load over 1.0 second.

Outcome: Lower deformation magnitude due to significantly reduced load (281.5 N vs 2020 N), but reveals dynamic stress evolution.

📂 Repository Structure

Report/: Full PDF Report of the project.

Simulation_Files/: Archived Ansys Workbench files (.wbpz).

Scripts/: Python script used to verify force calculations.

Images/: High-resolution contour plots and mesh images.

👤 Author

Muhammad Abdul Moiz

Roll No: ME-1902

Department: Mechanical Engineering
