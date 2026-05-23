"""
plot_figures.py

Generate publication-quality figures for the blockchain consensus percolation study.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_gcc_fraction(df, output_path="../figures/gcc_fraction.png"):
    link_probs = df["link_retention_prob"]
    mean_gcc = df["mean_gcc_fraction"]
    std_gcc = df["std_gcc_fraction"]

    plt.figure(figsize=(6,4))
    plt.errorbar(link_probs, mean_gcc, yerr=std_gcc, fmt='o-', capsize=3)
    plt.xlabel("Link Retention Probability")
    plt.ylabel("Mean GCC Fraction")
    plt.title("Giant Connected Component Fraction")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_finite_size_scaling(df, p_inf, alpha, output_path="../figures/finite_size_scaling.png"):
    network_sizes = df["network_size"]
    thresholds = df["critical_threshold"]
    plt.figure(figsize=(6,4))
    plt.scatter(network_sizes, thresholds, label="Simulated thresholds")
    N_fit = np.linspace(min(network_sizes), max(network_sizes), 100)
    plt.plot(N_fit, p_inf + N_fit**(-alpha), color='red', label=f"Fit: p_inf={p_inf:.3f}, alpha={alpha:.3f}")
    plt.xlabel("Network Size")
    plt.ylabel("Critical Consensus Threshold")
    plt.title("Finite-Size Scaling of Critical Thresholds")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_susceptibility(link_probs, susceptibility, output_path="../figures/susceptibility_curve.png"):
    plt.figure(figsize=(6,4))
    plt.plot(link_probs, susceptibility, marker='o')
    plt.xlabel("Link Retention Probability")
    plt.ylabel("Susceptibility")
    plt.title("Consensus Susceptibility Near Critical Threshold")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    # GCC fraction figure
    df_gcc = pd.read_csv("../data/processed/simulation_results.csv")
    plot_gcc_fraction(df_gcc)

    # Finite-size scaling figure
    df_fs = pd.read_csv("../data/processed/critical_thresholds.csv")
    p_inf, alpha = 0.80, 0.25  # example fit; replace with real fit values
    plot_finite_size_scaling(df_fs, p_inf, alpha)

    # Susceptibility figure
    df_susc = pd.read_csv("../data/processed/simulation_results.csv")
    link_probs = df_susc["link_retention_prob"]
    # Example susceptibility: replace with real computed values
    susceptibility = np.random.random(len(link_probs)) * 0.05
    plot_susceptibility(link_probs, susceptibility)
