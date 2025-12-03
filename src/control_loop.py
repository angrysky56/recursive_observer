import numpy as np
from abc import ABC, abstractmethod


class ControlLoop(ABC):
    @abstractmethod
    def process(self, signal: float) -> float:
        pass


class ReactiveLoop(ControlLoop):
    """
    Layer 3: The First Sine (Reactive Loop).

    This loop scales the response proportional to the stimulus.
    It represents the immediate, energetic reaction to input (Fight/Flight).

    Formula: y = sin(gain * x)
    """

    def __init__(self, gain: float = 1.0):
        self.gain = gain

    def process(self, stimulus: float) -> float:
        return np.sin(stimulus * self.gain)


class DampingLoop(ControlLoop):
    """
    Layer 4: The Second Sine (Damping Loop).

    This loop monitors the output of Layer 3 and applies a non-linear
    restoring force to prevent the system from spiraling into infinite energy.
    It represents the 'Theory of Mind' turned inward—observing the self.

    Formula: z = sin(damping_factor * y)
    """

    def __init__(self, damping_factor: float = 1.0):
        self.damping_factor = damping_factor

    def process(self, reactive_output: float) -> float:
        return np.sin(reactive_output * self.damping_factor)
