import numpy as np
from models import calculate_survival_fraction

def run_simulation():
    # Define a range of radiation doses from 0 to 10 Gray (Gy)
    doses = np.linspace(0, 10, 50)
    
    # Tissue 1: Radioresistant Tumor Cells (e.g., Glioblastoma)
    # Typically lower alpha/beta ratio or lower absolute alpha value
    alpha_tumor, beta_tumor = 0.15, 0.05
    
    # Tissue 2: Radiosensitive Healthy Tissue (Late-responding normal tissue)
    alpha_healthy, beta_healthy = 0.25, 0.02
    
    print("Dose(Gy) | Tumor_Survival | Healthy_Survival")
    print("-" * 45)
    
    # Run the math for each dose point
    for d in doses[::5]: # Show a subset of points for the log preview
        s_tumor = calculate_survival_fraction(d, alpha_tumor, beta_tumor)
        s_healthy = calculate_survival_fraction(d, alpha_healthy, beta_healthy)
        print(f"{d:8.1f} | {s_tumor:14.4f} | {s_healthy:16.4f}")

if name == "main":
    run_simulation()
