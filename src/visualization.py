import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .observer import RecursiveObserver


def run_simulation():
    agent = RecursiveObserver()

    # Time vector
    t_max = 100
    dt = 0.1
    steps = int(t_max / dt)
    time = np.linspace(0, t_max, steps)

    # Stimulus profile: Pulse of stress
    stimulus = np.zeros(steps)
    stimulus[200:600] = 2.0  # High stress from t=20 to t=60

    # Data storage
    history = {"t": time, "stimulus": [], "a": [], "b": [], "x": []}

    print("Running simulation...")
    for s in stimulus:
        state = agent.step(s, dt)
        history["stimulus"].append(state["stimulus"])
        history["a"].append(state["net_stress_a"])
        history["b"].append(state["splitting_b"])
        history["x"].append(state["state_x"])

    return history


def plot_results(history):
    print("Plotting results...")

    # 1. Time Series Plot
    fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    ax[0].plot(history["t"], history["stimulus"], label="Stimulus", color="gray", linestyle="--")
    ax[0].plot(history["t"], history["a"], label="Net Stress (a)", color="red")
    ax[0].set_ylabel("Input / Stress")
    ax[0].legend()
    ax[0].set_title("Stimulus and Net Stress")

    ax[1].plot(history["t"], history["b"], label="Splitting Factor (b)", color="purple")
    ax[1].set_ylabel("Duration / Complexity")
    ax[1].legend()
    ax[1].set_title("Splitting Factor (Accumulated Stress)")

    ax[2].plot(history["t"], history["x"], label="State (x)", color="blue")
    ax[2].set_ylabel("Emotional State")
    ax[2].set_xlabel("Time")
    ax[2].legend()
    ax[2].set_title("System State (Hysteresis Check)")

    plt.tight_layout()
    plt.savefig("time_series.png")
    print("Saved time_series.png")

    # 2. Cusp Manifold Trajectory (2D Projection: a vs x)
    plt.figure(figsize=(8, 6))
    plt.scatter(history["a"], history["x"], c=history["t"], cmap="viridis", s=10, alpha=0.5)
    plt.colorbar(label="Time")
    plt.xlabel("Net Stress (a)")
    plt.ylabel("State (x)")
    plt.title("Trajectory on Control Surface (a vs x)")
    plt.grid(True)
    plt.savefig("trajectory_2d.png")
    print("Saved trajectory_2d.png")


if __name__ == "__main__":
    data = run_simulation()
    plot_results(data)
