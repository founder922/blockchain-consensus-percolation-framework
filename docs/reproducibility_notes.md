# Reproducibility Notes

## Computational Environment

Recommended environment:

- Python 3.11+
- NetworkX >= 3.2
- NumPy >= 1.26
- SciPy >= 1.11
- pandas >= 2.1
- Matplotlib >= 3.8

## Simulation Framework

The simulations model blockchain communication overlays as stochastic Erdős–Rényi graphs undergoing bond percolation and adversarial connectivity degradation.

The framework evaluates:

- giant connected component emergence
- consensus-feasibility thresholds
- finite-size scaling
- susceptibility amplification
- probabilistic liveness collapse
- targeted attack robustness

## Monte-Carlo Sampling

Each parameter configuration should be evaluated using multiple independent stochastic realisations.

Typical parameters:

- network sizes: 500–5000 nodes
- mean degree range: 0.5–4.0
- link-retention probability: 0.2–1.0
- Monte-Carlo trials: 500

## Statistical Outputs

The framework computes:

- mean GCC fraction
- variance
- percentile distributions
- consensus probability
- susceptibility
- finite-size threshold shifts

## Figure Reproducibility

All publication figures should be generated directly from processed numerical outputs using the plotting scripts contained within the repository.

## Future Extensions

Future work may incorporate:

- scale-free overlays
- temporal network dynamics
- weighted communication edges
- directed propagation structures
- empirical blockchain topology datasets
- latency-aware consensus propagation
