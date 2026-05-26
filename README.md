# RadBioSim-Predictor: Computational Radiobiology & Tissue Kinetics

A biophysical modeling framework designed to simulate cell survival fractions and tissue-specific kinetic responses under various ionizing radiation regimens. 

## Core Capabilities
* Linear-Quadratic (LQ) Model Engine: Simulates single-track and dual-track radiation damage kinetics.
* Biologically Effective Dose (BED) Calculator: Quantifies fractionation variations between healthy and malignant tissue.

## Mathematical Framework
Cell survival tracking is governed by the classic LQ formula:
$$S = e^{-(\alpha D + \beta D^2)}$$

Where $D$ represents the total radiation dose in Grays (Gy), $\alpha$ dictates single-track lethal damage, and $\beta$ accounts for the cumulative effect of sublethal lesions.
