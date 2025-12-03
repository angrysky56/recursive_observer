from .control_loop import ReactiveLoop, DampingLoop
from .catastrophe import CuspCatastrophe


class RecursiveObserver:
    """
    The Recursive Observer Agent.

    Integrates the Double-Sine Control Loop and the Cusp Catastrophe Model.

    - Layer 3 (Reactive): Generates energy from stimulus.
    - Layer 4 (Damping): Regulates the energy.
    - Cusp Model: Maps the net stress (a) and duration/complexity (b) to the
      state (x) to simulate trauma and hysteresis.
    """

    def __init__(self):
        self.reactive = ReactiveLoop(gain=1.0)
        self.damping = DampingLoop(damping_factor=0.8)
        self.catastrophe = CuspCatastrophe()

        self.duration_stress = 0.0

    def step(self, stimulus: float, dt: float = 0.1) -> dict:
        """
        Advance the simulation by one time step.

        Args:
            stimulus: External input intensity.
            dt: Time step size.

        Returns:
            Dictionary containing the current state of the system.
        """
        # Layer 3: Reactive Loop (The First Sine)
        reaction = self.reactive.process(stimulus)

        # Layer 4: Damping Loop (The Second Sine)
        # It observes the reaction, not the stimulus directly.
        regulation = self.damping.process(reaction)

        # Mapping to Cusp Parameters
        # a (Normal Factor) = Net Stress = Reaction - Regulation
        # If regulation fails to dampen reaction, 'a' increases.
        a = reaction - regulation

        # b (Splitting Factor) = Accumulation of Stress over Time (Duration)
        # If 'a' is high, 'b' grows. If 'a' is low, 'b' decays.
        if abs(a) > 0.2:
            self.duration_stress += dt * 0.5
        else:
            self.duration_stress = max(0, self.duration_stress - dt * 0.5)

        b = self.duration_stress

        # Update Catastrophe State
        self.catastrophe.update(a, b, dt)

        return {"stimulus": stimulus, "reaction": reaction, "regulation": regulation, "net_stress_a": a, "splitting_b": b, "state_x": self.catastrophe.state, "is_trapped": self.catastrophe.is_trapped(a, b)}

    def reset(self):
        """Orthogonal Perturbation: Reset the system."""
        self.duration_stress = 0.0
        self.catastrophe.state = 0.0
