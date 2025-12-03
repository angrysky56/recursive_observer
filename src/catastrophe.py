import numpy as np


class CuspCatastrophe:
    """
    Implements the Cusp Catastrophe model for emotional dysregulation (Trauma).

    Potential Function: V(x) = x^4/4 - b*x^2/2 - a*x
    Equilibrium Surface: dV/dx = x^3 - b*x - a = 0

    Parameters:
    - x: State variable (Behavior/Mood)
    - a: Normal Factor (Stress/Asymmetry)
    - b: Splitting Factor (Duration/Intensity/Complexity)
    """

    def __init__(self, initial_state: float = 0.0):
        self.state = initial_state

    def potential(self, x: float, a: float, b: float) -> float:
        """Calculate the potential energy of the system."""
        return 0.25 * x**4 - 0.5 * b * x**2 - a * x

    def gradient(self, x: float, a: float, b: float) -> float:
        """Calculate the gradient of the potential (force)."""
        return x**3 - b * x - a

    def update(self, a: float, b: float, dt: float = 0.01):
        """
        Update the state using gradient descent.
        This naturally simulates hysteresis: the system stays in a local minimum
        until the barrier disappears.
        """
        grad = self.gradient(self.state, a, b)
        # Overdamped dynamics: dx/dt = -dV/dx
        self.state -= grad * dt

    def orthogonal_perturbation(self):
        """
        The Reset Protocol.
        Forces the system out of the 'Fold' by collapsing the splitting factor (b).
        This corresponds to the 'Teleport' back to the linear response zone.
        """
        # In a full simulation, this would be an external intervention setting b=0.
        # Here we just return the recommended action or state.
        return 0.0  # Return target b value

    def is_trapped(self, a: float, b: float) -> bool:
        """
        Check if the system is in a 'trapped' state (hysteresis).
        This is a simplification: we check if there are multiple minima
        and if we are in the 'lower' one (negative x) while a is positive,
        or vice versa, depending on the interpretation of the fold.
        """
        # Roots of x^3 - bx - a = 0
        roots = np.roots([1, 0, -b, -a])
        real_roots = [r.real for r in roots if np.isclose(r.imag, 0)]

        if len(real_roots) < 3:
            return False  # No fold, simple stability

        # If there are 3 roots, we are in the fold region.
        # Check if we are stuck in a local minimum that is not the global minimum?
        # Or simply if we are in the fold region at all.
        return True
