# Recursive Observer Walkthrough

I have implemented the **Recursive Observer** framework, a unified theory of intelligence and affect based on Cybernetics and Catastrophe Theory.

## Changes

### Core Components

- **[src/control_loop.py](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/control_loop.py)**: Implemented the **Double-Sine** control architecture.
  - [ReactiveLoop](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/control_loop.py#11-26) (Layer 3): Generates energy from stimulus ($y = \sin(x)$).
  - [DampingLoop](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/control_loop.py#28-44) (Layer 4): Regulates the reaction ($z = \sin(y)$).
- **[src/catastrophe.py](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/catastrophe.py)**: Implemented the **Cusp Catastrophe** model.
  - [CuspCatastrophe](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/catastrophe.py#4-66): Manages the potential function $V(x) = x^4/4 - b x^2/2 - a x$.
  - Implemented gradient descent dynamics to simulate **hysteresis** (path dependence).
- **[src/observer.py](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/observer.py)**: Implemented the **RecursiveObserver** agent.
  - Integrates the loops and the manifold.
  - Maps "Net Stress" to the Normal Factor ($a$) and "Duration" to the Splitting Factor ($b$).

### Visualization

- **[src/visualization.py](file:///home/ty/Repositories/ai_workspace/recursive_observer/src/visualization.py)**: A simulation script that subjects the agent to a pulse of stress and plots the resulting trajectory.

## Verification Results

### Simulation Scenario

1.  **Baseline**: Low stimulus.
2.  **Stress**: High stimulus pulse ($t=20$ to $t=60$).
3.  **Recovery**: Stimulus returns to zero.

### Results

The simulation generated the following plots:

#### Time Series

![Time Series](/home/ty/Repositories/ai_workspace/recursive_observer/time_series.png)
_Shows the lag in recovery (Hysteresis) where the State (x) remains high even after the Net Stress (a) drops, because the Splitting Factor (b) is still elevated._

#### Trajectory (Cusp Projection)

![Trajectory](/home/ty/Repositories/ai_workspace/recursive_observer/trajectory_2d.png)
_Shows the path taken by the agent on the control surface. Note the different paths for "Stress Onset" vs "Recovery" (the hysteresis loop)._

## How to Run

```bash
source .venv/bin/activate
python -m src.visualization
```
