"""
simulate_percolation.py

Monte-Carlo simulation framework for blockchain consensus percolation.
Evaluates giant connected component emergence under stochastic link degradation.
"""

import networkx as nx
import numpy as np
import pandas as pd
from tqdm import tqdm

def generate_er_graph(n_nodes, mean_degree):
    p = mean_degree / (n_nodes - 1)
    return nx.erdos_renyi_graph(n_nodes, p)

def bond_percolation(G, link_retention_prob, seed=None):
    rng = np.random.default_rng(seed)
    G_perc = G.copy()
    for u, v in list(G.edges()):
        if rng.random() > link_retention_prob:
            G_perc.remove_edge(u, v)
    return G_perc

def compute_gcc_fraction(G):
    gcc = max(nx.connected_components(G), key=len)
    return len(gcc) / G.number_of_nodes()

def monte_carlo_simulation(n_nodes, mean_degree, link_probs, n_trials=500, seed=None):
    results = []
    for link_prob in tqdm(link_probs, desc="Link Retention Sweep"):
        gcc_fractions = []
        for trial in range(n_trials):
            G = generate_er_graph(n_nodes, mean_degree)
            G_perc = bond_percolation(G, link_prob, seed=seed)
            gcc_frac = compute_gcc_fraction(G_perc)
            gcc_fractions.append(gcc_frac)
        results.append({
            "link_retention_prob": link_prob,
            "mean_gcc_fraction": np.mean(gcc_fractions),
            "std_gcc_fraction": np.std(gcc_fractions)
        })
    return pd.DataFrame(results)

if __name__ == "__main__":
    n_nodes = 1000
    mean_degree = 2.5
    link_probs = np.linspace(0.2, 1.0, 17)
    df_results = monte_carlo_simulation(n_nodes, mean_degree, link_probs, n_trials=100)
    df_results.to_csv("../data/processed/simulation_results.csv", index=False)
    print("Simulation complete. Results saved to data/processed/simulation_results.csv")
