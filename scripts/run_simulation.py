from src.config import PARAMS
from src.simulation import run_simulation
from src.metrics import compute_fractions
from src.plot import plot_results

def main():
    history, population = run_simulation(PARAMS)

    # Convert to fractions for interp
    fractions = compute_fractions(history, PARAMS['num_cells'])

    print("Final fractions:")
    for key, values in fractions.items():
        print(f"{key}: {values[-1]:.3f}")

    plot_results(history, population)

if __name__ == "__main__":
    main()
    