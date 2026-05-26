import numpy as np

def calculate_survival_fraction(dose: float, alpha: float, beta: float) -> float:
    """
    Calculates the cell survival fraction using the classic Linear-Quadratic model.
    Formula: S = exp(-(alpha*D + beta*D^2))
    """
    if dose < 0 or alpha < 0 or beta < 0:
        raise ValueError("Physical parameters must be non-negative.")
    return float(np.exp(-(alpha * dose + beta * (dose ** 2))))

def calculate_bed(total_dose: float, dose_per_fraction: float, alpha_beta_ratio: float) -> float:
    """
    Calculates the Biologically Effective Dose (BED) for fractionated radiotherapy.
    Formula: BED = TD * (1 + d / (alpha/beta))
    """
    if total_dose < 0 or dose_per_fraction < 0 or alpha_beta_ratio <= 0:
        raise ValueError("Invalid physical or tissue-specific parameters.")
    return float(total_dose * (1 + (dose_per_fraction / alpha_beta_ratio)))
