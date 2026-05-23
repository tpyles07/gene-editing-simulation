import numpy as np

from src.metrics import (
    compute_avg_mutations,
    compute_mean_fitness,
    compute_type_fractions,
)

# Initialize the cell population

def initialize_population(num_cells):
    population = []
    for _ in range(num_cells):
        population.append({
            "type": "unedited",
            "off_target_count": 0,
            "fitness": 1.0,
            "alive": True,
        })
    return population

# Apply CRISPR-Cas9 editing to the population

def apply_editing(cell, params):
    if not cell["alive"]:
        return
    p_delivery = params["p_delivery"]
    p_cut = params["p_cut"]
    p_hdr = params["p_hdr"]

    # CRISPR delivery
    if np.random.rand() < p_delivery:
        # DNA cut occurs
        if np.random.rand() < p_cut:
            # Repair pathway
            if np.random.rand() < p_hdr:
                cell["type"] = "hdr"
            else:
                cell["type"] = "nhej"


# Apply off-target effects

def apply_off_target_effects(cell, params):
    if not cell["alive"]:
        return
    p_off_target = params["p_off_target"]
    off_target_penalty = params["off_target_penalty"]

    # Random off-target mutation
    if np.random.rand() < p_off_target:
        cell["off_target_count"] += 1

    # Excessive mutation burden
    if cell["off_target_count"] >= params["mutation_threshold"]:
        # Increased death probability due to high mutation load
        if np.random.rand() < 0.5:
            cell["alive"] = False

# Update cell fitness

def update_fitness(cell, params):
    if not cell["alive"]:
        return
    base_fitness = {
        "unedited": params["fitness_unedited"],
        "hdr": params["fitness_hdr"],
        "nhej": params["fitness_nhej"],
    }
    off_target_penalty = params["off_target_penalty"]
    mutation_penalty = cell["off_target_count"] * off_target_penalty
    fitness = base_fitness[cell["type"]] - mutation_penalty
    
    # Prevent negative fitness
    cell["fitness"] = max(0, fitness)

# Reproduce population

def reproduce_population(population, params):
    growth_rate = params["base_growth_rate"]
    carrying_capacity = params["carrying_capacity"]
    living_population = [cell for cell in population if cell["alive"]]
    current_size = len(living_population)

    # Logistic growth suppression
    capacity_factor = max(
        0,
        1 - (current_size / carrying_capacity)
    )
    new_population = []
    for cell in living_population:
        # Original cell survives
        new_population.append(cell)
        reproduction_probability = (
            growth_rate
            * cell["fitness"]
            * capacity_factor
        )
        reproduction_probability = min(
            1,
            reproduction_probability
        )

        # Stochastic reproduction
        if np.random.rand() < reproduction_probability:
            offspring = cell.copy()
            new_population.append(offspring)
    return new_population

# Main simulation loop

def run_simulation(params):
    population = initialize_population(
        params["num_cells"]
    )
    history = {
        "population_size": [],
        "avg_mutations": [],
        "mean_fitness": [],

        "hdr_fraction": [],
        "nhej_fraction": [],
        "unedited_fraction": [],
    }
    timesteps = params["timesteps"]
    for t in range(timesteps):
        # Cell-level dynamics
        for cell in population:
            if not cell["alive"]:
                continue
            apply_editing(cell, params)
            apply_off_target_effects(cell, params)
            update_fitness(cell, params)

        # Population reproduction
        population = reproduce_population(population, params)

        # Metrics & history tracking
        living_population = [
            cell for cell in population if cell["alive"]
        ]
        history["population_size"].append(
            len(living_population)
        )
        history["avg_mutations"].append(
            compute_avg_mutations(living_population)
        )
        history["mean_fitness"].append(
            compute_mean_fitness(living_population)
        )
        fractions = compute_type_fractions(
            living_population
        )
        history["hdr_fraction"].append(
            fractions["hdr"]
        )
        history["nhej_fraction"].append(
            fractions["nhej"]
        )
        history["unedited_fraction"].append(
            fractions["unedited"]
        )

    return history, population