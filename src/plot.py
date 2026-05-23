import matplotlib.pyplot as plt

def plot_results(history, population):

    timesteps = range(len(history["unedited_fraction"]))

    # Cell type fractions
    plt.figure()

    plt.plot(
        timesteps,
        history["unedited_fraction"],
        label="Unedited"
    )

    plt.plot(
        timesteps,
        history["hdr_fraction"],
        label="HDR (precise edit)"
    )

    plt.plot(
        timesteps,
        history["nhej_fraction"],
        label="NHEJ (mutations)"
    )

    plt.xlabel("Timesteps")
    plt.ylabel("Fraction of Population")
    plt.title("CRISPR-Cas9 Gene Editing Outcomes")
    plt.legend()
    plt.tight_layout()

    # Population growth
    plt.figure()

    plt.plot(
        timesteps,
        history["population_size"],
        label="Population Size"
    )

    plt.xlabel("Timesteps")
    plt.ylabel("Number of Cells")
    plt.title("Population Growth Over Time")
    plt.legend()
    plt.tight_layout()

    # Mean fitness
    plt.figure()

    plt.plot(
        timesteps,
        history["mean_fitness"],
        label="Mean Fitness"
    )

    plt.xlabel("Timesteps")
    plt.ylabel("Mean Fitness")
    plt.title("Mean Fitness Over Time")
    plt.legend()
    plt.tight_layout()

    # Average mutations
    plt.figure()

    plt.plot(
        timesteps,
        history["avg_mutations"],
        label="Average Off-Target Mutations"
    )

    plt.xlabel("Timesteps")
    plt.ylabel("Average Mutations")
    plt.title("Mutation Burden Over Time")
    plt.legend()
    plt.tight_layout()

    # Final mutation histogram
    mutation_counts = [
        cell["off_target_count"]
        for cell in population
    ]

    plt.figure()

    plt.hist(mutation_counts, bins=20)

    plt.xlabel("Number of Off-Target Mutations")
    plt.ylabel("Number of Cells")
    plt.title("Distribution of Off-Target Mutations")
    plt.tight_layout()

    plt.show()