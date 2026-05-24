import streamlit as st

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

st.title("CRISPR-Cas9 Gene Editing Simulation Dashboard")

st.write("Interactive simulation of CRISPR-Cas9 gene editing dynamics.")

# Add interactive sliders for key parameters

p_cut = st.slider(
    "Cut Probability",
    0.0,
    1.0,
    0.7)

p_hdr = st.slider(
    "HDR Probability",
    0.0,
    1.0,
    0.3)

p_off_target = st.slider(
    "Off-Target Probability",
    0.0,
    0.2,
    0.02)

# Build the parameters dictionary based on user input

params = {
    "num_cells": 1000,
    "timesteps": 100,

    "p_delivery": 0.8,
    "p_cut": p_cut,
    "p_hdr": p_hdr,

    "p_off_target": p_off_target,

    "off_target_penalty": 0.03,
    "mutation_threshold": 10,

    "base_growth_rate": 0.2,
    "carrying_capacity": 10000,

    "fitness_unedited": 1.0,
    "fitness_hdr": 1.2,
    "fitness_nhej": 0.7,
}

# Connect to the simulation module and run the simulation with the provided parameters

from src.simulation import run_simulation

history, population = run_simulation(params)

# Display the results using the plotting module

import matplotlib.pyplot as plt

# Population size over time

fig, ax = plt.subplots()

ax.plot(history["population_size"])

ax.set_title("Population Size")
ax.set_xlabel("Timesteps")
ax.set_ylabel("Number of Cells")

st.pyplot(fig)

# Average mutations over time

fig2, ax2 = plt.subplots()

ax2.plot(history["avg_mutations"])

ax2.set_title("Average Off-Target Mutations")

st.pyplot(fig2)

# Cell fractions

fig3, ax3 = plt.subplots()

ax3.plot(
    history["hdr_fraction"],
    label="HDR (precise edit)"
)

ax3.plot(
    history["nhej_fraction"],
    label="NHEJ (mutations)"
)

ax3.plot(
    history["unedited_fraction"],
    label="Unedited"
)

ax3.legend()

st.pyplot(fig3)

if st.button("High Precision Editing"):
    # Adjust parameters for high precision editing
    params["p_cut"] = 0.9
    params["p_hdr"] = 0.8
    params["p_off_target"] = 0.005

    history, population = run_simulation(params)

    st.write("High Precision Editing Simulation Results")

    fig4, ax4 = plt.subplots()

    ax4.plot(history["population_size"])
    ax4.set_title("Population Size (High Precision)")
    ax4.set_xlabel("Timesteps")
    ax4.set_ylabel("Number of Cells")

    st.pyplot(fig4)

if st.button("Aggressive Editing"):
    # Adjust parameters for aggressive editing
    params["p_cut"] = 0.95
    params["p_hdr"] = 0.5
    params["p_off_target"] = 0.05

    history, population = run_simulation(params)

    st.write("Aggressive Editing Simulation Results")

    fig5, ax5 = plt.subplots()

    ax5.plot(history["population_size"])
    ax5.set_title("Population Size (Aggressive Editing)")
    ax5.set_xlabel("Timesteps")
    ax5.set_ylabel("Number of Cells")

    st.pyplot(fig5)

if st.button("Cancer Therapy"):
    # Adjust parameters for cancer therapy simulation
    params["p_cut"] = 0.85
    params["p_hdr"] = 0.4
    params["p_off_target"] = 0.02

    history, population = run_simulation(params)

    st.write("Cancer Therapy Simulation Results")

    fig6, ax6 = plt.subplots()

    ax6.plot(history["population_size"])
    ax6.set_title("Population Size (Cancer Therapy)")
    ax6.set_xlabel("Timesteps")
    ax6.set_ylabel("Number of Cells")

    st.pyplot(fig6)

if st.button("High Mutation Rate"):
    # Adjust parameters for high mutation rate simulation
    params["p_cut"] = 0.8
    params["p_hdr"] = 0.2
    params["p_off_target"] = 0.1

    history, population = run_simulation(params)

    st.write("High Mutation Rate Simulation Results")

    fig7, ax7 = plt.subplots()

    ax7.plot(history["population_size"])
    ax7.set_title("Population Size (High Mutation Rate)")
    ax7.set_xlabel("Timesteps")
    ax7.set_ylabel("Number of Cells")

    st.pyplot(fig7)
    