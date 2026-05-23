import numpy as np

def compute_fractions(history, total_cells):
    # Compute fractions for easier population interpretation
    fractions = {}

    for key, values in history.items():
        fractions[key] = np.array(values) / total_cells

    return fractions

def compute_total_population(history):
    # Compute total population over time
    return [
        u + h + n
        for u, h, n in zip(
            history["unedited"],
            history["hdr"],
            history["nhej"],
        )
    ]

def compute_avg_mutations(population):
    if len(population) == 0:
        return 0
    total_mutations = sum(cell["off_target_count"] for cell in population)
    return total_mutations / len(population)

def compute_mean_fitness(population):
    if len(population) == 0:
        return 0
    total_fitness = sum(cell["fitness"] for cell in population)
    return total_fitness / len(population)

def compute_type_fractions(population):
    # Compute fractions of each cell type in the population
    total = len(population)
    if total == 0:
        return {"unedited": 0, "hdr": 0, "nhej": 0}

    counts = {"unedited": 0, "hdr": 0, "nhej": 0}
    for cell in population:
        if cell["type"] == "unedited":
            counts["unedited"] += 1
        elif cell["type"] == "hdr":
            counts["hdr"] += 1
        elif cell["type"] == "nhej":
            counts["nhej"] += 1

    return {
        key: count / total
        for key, count in counts.items()
    }

def mutation_distribution(population):
    # Compute distribution of off-target mutations
    return [cell["off_target_count"] for cell in population]