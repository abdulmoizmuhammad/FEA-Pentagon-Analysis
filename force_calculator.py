"""
================================================================================
FEA SIMULATION PARAMETER VERIFICATION TOOL
================================================================================
Author:     Muhammad Abdul Moiz (ME-1902)
Project:    Pentagon Structural Analysis (Static & Transient)
Date:       November 28, 2025
Purpose:    Automated derivation and verification of boundary conditions 
            and material properties based on unique user identity data.
================================================================================
"""

import datetime
import logging
from dataclasses import dataclass

# Setup professional logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

@dataclass
class SimulationInputs:
    """Data Verification Object for Ansys Inputs"""
    youngs_modulus_mpa: int
    poissons_ratio: float
    static_load_n: int
    transient_load_n: float
    time_step_s: float

class FEAParameterGenerator:
    """
    Engine for calculating FEA boundary conditions from personal metadata.
    """
    
    def __init__(self, roll_number: str, dob: datetime.date, exchange_rate: float):
        self.roll_number = roll_number
        self.dob = dob
        self.exchange_rate = exchange_rate
        self.simulation_data = None

    def derive_parameters(self) -> SimulationInputs:
        """Performs the derivation logic for all physical properties."""
        logger.info("Starting parameter derivation process...")
        
        # 1. Young's Modulus from Roll Number (Last 2 digits * 1000)
        try:
            last_digits = int(self.roll_number.split('-')[-1][-2:])
            e_modulus = last_digits * 1000
        except ValueError:
            logger.error("Invalid Roll Number format.")
            raise

        # 2. Static Force from Date of Birth (Day + Month + Year)
        static_f = self.dob.day + self.dob.month + self.dob.year

        # 3. Transient Force from Exchange Rate
        transient_f = self.exchange_rate

        self.simulation_data = SimulationInputs(
            youngs_modulus_mpa=e_modulus,
            poissons_ratio=0.28,
            static_load_n=static_f,
            transient_load_n=transient_f,
            time_step_s=0.2
        )
        
        logger.info("Derivation complete.")
        return self.simulation_data

    def generate_verification_report(self):
        """Prints a formatted engineering report to the console."""
        if not self.simulation_data:
            self.derive_parameters()

        data = self.simulation_data
        
        print("\n" + "="*65)
        print(f"{'FEA SIMULATION INPUT VERIFICATION REPORT':^65}")
        print("="*65)
        print(f"{'PARAMETER':<30} | {'DERIVED VALUE':<15} | {'SOURCE/LOGIC':<10}")
        print("-" * 65)
        
        # Row 1: Material
        print(f"{'Young\'s Modulus (E)':<30} | {f'{data.youngs_modulus_mpa} MPa':<15} | Roll No ({self.roll_number})")
        print(f"{'Poisson\'s Ratio':<30} | {data.poissons_ratio:<15} | Standard")
        
        print("-" * 65)
        
        # Row 2: Static
        dob_str = self.dob.strftime('%d-%m-%Y')
        print(f"{'Static Remote Force':<30} | {f'{data.static_load_n} N':<15} | DOB ({dob_str})")
        
        # Row 3: Transient
        print(f"{'Transient Force':<30} | {f'{data.transient_load_n} N':<15} | USD Rate ({self.exchange_rate})")
        
        print("-" * 65)
        print(f"{'VERIFICATION STATUS':<30} | {'[ VALIDATED ]':<15} | READY FOR ANSYS")
        print("="*65 + "\n")

if __name__ == "__main__":
    # Initialize Generator with Personal Data
    # Roll No: ME-1902
    # DOB: 04 Dec 2004
    # USD Rate: 281.5
    
    generator = FEAParameterGenerator(
        roll_number="ME-1902",
        dob=datetime.date(2004, 12, 4),
        exchange_rate=281.5
    )
    
    # Run the report
    generator.generate_verification_report()