import matplotlib.pyplot as plt
import numpy as np

class NewtonLaw:
    def __init__(self) -> None:
        self.G = 6.674 * 10**-11
    
    def gravitational_force(self, m1: float, m2: float, r: int) -> float:
        return (self.G * m1 * m2) / r**2

if __name__ == "__main__":
    m1 = 0.5
    m2 = 1.5

    g_forces = np.array([NewtonLaw().gravitational_force(m1, m2, r) for r in range(100, 1001, 50)])

    plt.plot(g_forces)
    plt.show()
