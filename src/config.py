# Provide initial parameters for the model

PARAMS = {
    "num_cells": 10000,
    "timesteps": 100,

    # Minimum ideal probabilities of CRISPR-Cas9 delivery
    "p_delivery": 0.7,
    "p_cut": 0.6,
    "p_hdr": 0.3,
    "p_nhej": 0.7,
}

# Define an update to the parameters, modeling the fitness & competition of living cells
PARAMS.update({
    "fitness_unedited": 1.0,
    "fitness_hdr": 1.2,
    "fitness_nhej": 0.8,

    "base_growth_rate": 0.3,
    "carrying_capacity": 200000,

    "death_unedited": 0.01,
    "death_hdr": 0.005,
    "death_nhej": 0.05,

    "p_off_target": 0.02,
    "off_target_penalty": 0.03,
    "mutation_threshold": 10,
})
