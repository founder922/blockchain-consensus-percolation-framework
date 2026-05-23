"""
finite_size_scaling.py

Estimate finite-size scaling of critical consensus thresholds in blockchain overlays.
Uses simulation results to fit scaling exponent.
"""

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def scaling_law(N, p_inf, alpha):
    """
    Finite-size scaling function:
    p_c(N) = p_inf + N^(-alpha)
    """
    return p_inf + N**(-alpha)

def fit_finite_size_scaling(network_sizes, thresholds):
    popt, pcov = curve_fit(scaling_law, network_sizes, thresholds)
    p_inf, alpha = popt
    return p_inf, alpha, pcov

if __name__ == "__main__":
    # Load precomputed critical thresholds
    df = pd.read_csv("../data/processed/critical_thresholds.csv")
    network_sizes = df["network_size"].values
    thresholds = df["critical_threshold"].values

    # Fit scaling law
    p_inf, alpha, pcov = fit_finite_size_scaling(network_sizes, thresholds)
    print(f"Asymptotic threshold (p_inf): {p_inf:.3f}")
    print(f"Scaling exponent (alpha): {alpha:.3f}")

    # Plot
    plt.figure(figsize=(6,4))
    plt.scatter(network_sizes, thresholds, label="Simulated thresholds")
    N_fit = np.linspace(min(network_sizes), max(network_sizes), 100)
    plt.plot(N_fit, scaling_law(N_fit, p_inf, alpha), color='red', label=f"Fit: p_inf={p_inf:.3f}, alpha={alpha:.3f}")
    plt.xlabel("Network Size")
    plt.ylabel("Critical Consensus Threshold")
    plt.title("Finite-Size Scaling of Critical Thresholds")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../figures/finite_size_scaling.png", dpi=300)
    plt.show()
