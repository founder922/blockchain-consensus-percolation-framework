"""
susceptibility_analysis.py

Compute susceptibility and critical fluctuations in blockchain consensus simulations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_susceptibility(gcc_samples):
    """
    Compute susceptibility: variance scaled by number of nodes.
    """
    n_nodes = gcc_samples.shape[1] if len(gcc_samples.shape) > 1 else len(gcc_samples[0])
    mean_gcc = np.mean(gcc_samples, axis=0)
    var_gcc = np.var(gcc_samples, axis=0)
    susceptibility = n_nodes * var_gcc
    return susceptibility

if __name__ == "__main__":
    # Load simulation results: CSV should contain columns 'link_retention_prob', 'gcc_trial_1', 'gcc_trial_2', ...
    df = pd.read_csv("../data/processed/simulation_results.csv")
    
    # Extract GCC samples (all trials)
    gcc_samples = df.iloc[:, 1:].values  # assume first column is link probability

    # Compute susceptibility
    susceptibility = compute_susceptibility(gcc_samples)
    
    # Plot susceptibility curve
    link_probs = df.iloc[:, 0].values
    plt.figure(figsize=(6,4))
    plt.plot(link_probs, susceptibility, marker='o')
    plt.xlabel("Link Retention Probability")
    plt.ylabel("Susceptibility")
    plt.title("Consensus Susceptibility Near Critical Threshold")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../figures/susceptibility_curve.png", dpi=300)
    plt.show()
