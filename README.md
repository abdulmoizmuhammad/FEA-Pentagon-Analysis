TABLE OF CONTENTS
1.	ABSTRACT ..................................................................................................... 2
2.	INTRODUCTION ..................................................................................................... 2
3.	PROBLEM STATEMENT ..................................................................................................... 2
3.1 Material Properties .................................................................................. 2 3.2 Loading Conditions .................................................................................. 2 3.3 Boundary Conditions ............................................................................... 2
4.	GEOMETRY MODELING 
.....................................................................................................3
5.	MATERIALPROPERTIES
.....................................................................................................3
6.	BOUNDARY CONDITIONS (STATIC) .....................................................................................................3
7.	MESHING & CONVERGENCE .....................................................................................................4
8.	STATIC STRUCTURAL SIMULATION .....................................................................................................5
9.	TRANSIENT STRUCTURAL SIMULATION .....................................................................................................6
9.1 Simulation Settings .................................................................................6 
9.2 Boundary Conditions (Transient) ...........................................................6
10.	COMPARISON & CONCLUSION .....................................................................................................8 
10.1 Comparison of Results .......................................................................... 8 10.2 Conclusion .............................................................................................. 8






1. Abstract
This project presents a finite element analysis (FEA) of a regular pentagon structure using Static Structural and Transient Structural simulation techniques. The material properties were derived from the student roll number (ME-1902), resulting in a Young’s Modulus of 2,000 MPa and a Poisson’s Ratio of 0.28.
The static analysis utilized a load of 2,020 N (calculated from the date of birth), while the transient simulation applied a time-dependent load of 281.5 N (based on the USD to PKR exchange rate). One face of the pentagon was fixed, and a remote force was applied at one-third of the face length. The analysis compares the deformation and stress results between the static equilibrium and the time-dependent transient response.
2. Introduction
Finite Element Analysis (FEA) is a numerical method used to predict how a part behaves under physical conditions. In this project, a regular pentagon geometry was analyzed under two distinct conditions:
1.	Static Structural: Assumes the load is applied slowly, ignoring inertial and damping effects.
2.	Transient Structural: Analyzes the dynamic response of the structure over a defined time period (time-dependent), considering inertia and damping.
The goal is to observe how the pentagon deforms when a remote force is applied at a specific offset location on the fixed face.
3. Problem Statement
The objective is to analyze a regular pentagon structure under custom-defined constraints based on personal data.
3.1 Material Properties (Derived from Roll No. 1902)
•	Young’s Modulus (E):
E = (Last two digits) x 103 = 02 x  1,000 = 2,000  MPa
•	Poisson’s Ratio:
ν = 0.28
3.2 Loading Conditions
•	Static Load : Calculated from Date of Birth (04-Dec-2004).
FStatic = 4 + 12 + 2004 = 2,020 N
•	Transient Load: Based on the USD to PKR exchange rate.
FTransient = 281.5 N


3.3 Boundary Conditions
•	Support: One face is fully Fixed.
•	Load Application: Remote Force applied at 1/3rd distance of the fixed face.
•	Time Step (Transient): 0.2 seconds.
4. Geometry Modeling
The geometry consists of a regular pentagon extruded to a specified thickness. The model was generated using the DesignModeler/SpaceClaim interface within Ansys.

  
Figure 1: 3D Geometry of the extruded pentagon model.
5. Material Properties
A custom material named "Pentagon Moiz" was defined in Engineering Data with the calculated stiffness values.
 
Figure 2: Engineering Data showing Young's Modulus of 2000 MPa.
6. Boundary Conditions
To simulate the physical bending and shear, specific constraints were applied:
1.	Fixed Support: Applied to one side face of the pentagon.
2.	Remote Force: Applied to the same face but offset to 1/3rd of the length. This creates a moment arm, inducing rotation/bending in addition to the linear force.
 
Figure 3: Fixed Support applied to the face.

 
Figure 4: Remote Force applied at 1/3rd offset location. 
7. Meshing & Convergence
A mesh convergence study was conducted to ensure the accuracy of the results. The mesh was refined in three iterations to observe the stability of the Equivalent Stress.
  
Figure 5: Meshed model of the pentagon with element Quality.
 
Figure 6: Mesh Convergence Graph (Nodes vs. Stress).
8. Static Structural Simulation
In the static analysis, the load of 2,020 N was applied. The solver calculated the final equilibrium state.
    
Figure 7: Total Deformation (Static).

   
Figure 8: Equivalent (von-Mises) Stress (Static).
Results: The static results show the maximum deflection occurring at the tip of the pentagon opposite the fixed face.
9. Transient Structural Simulation
The Transient Structural analysis was performed to determine the time-dependent response. Unlike Explicit Dynamics (used for high-speed impact), Transient Structural is used here for a standard dynamic load over a duration of 1 second.
9.1 Simulation Settings:
•	Load: 281.5 N (USD Rate).
•	Step End Time: 1.0 s.
•	Time Step: 0.2 s.
  
Figure 9: Transient setup showing time steps of 0.2s and tabular data of force 3 with graph.
9.2 Boundary Conditions (Transient)
For dynamic behavior, the boundary conditions are demonestrated blow.
 
Figure 10: Figure 10: Fixed Support(face A) and Remote Force(B,C,D,E,F) applied in the Transient environment.
  
 
Figure 11: Total Deformation at t=0.842 = Total Deformation at 1.0s (Transient).
  
t=0.21053 sec                                                   t=0.42105 sec  
                                t=0.57895 sec                                                   t=0.78947 sec
Figure 12: Equivalent Stress at different values of t (Transient).
Results
The transient response shows how the stress evolves over the 1-second interval. Because the load (281.5 N) is significantly lower than the static load (2020 N), the resulting deformation is smaller.

11.	Comparison & Conclusion

10.1 Comparison of Results
Parameter	Static Structural	Transient Structural
Load Magnitude	2,020 N	281.5 N
Time Dependency	None (Equilibrium)	Time-Dependent (0.2s steps)
Deformation Trend	Higher (due to higher load)	Lower (due to lower load)

Table 1: Comparison of Results
10.2 Conclusion
The project successfully demonstrated the application of FEA on a pentagon model using personal data for boundary conditions. The Static Structural analysis provided the maximum stress limits under a heavy load (Date of Birth derived), while the Transient Structural simulation visualized the system's behavior under a lighter, time-stepped load (USD Rate derived). The use of a Remote Force at 1/3rd distance introduced realistic moment effects on the fixed face.
![Uploading image.png…]()
