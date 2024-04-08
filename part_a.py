import matplotlib.pyplot as plt

class GravitationalForceCalculator:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.G = 6.674 * 10**-11

    def calculate_force(self, distance):
        return (self.G * self.m1 * self.m2) / (distance ** 2)

def plot_force_vs_distance(calculator, start=100, end=1000, interval=50):
    distances = list(range(start, end + 1, interval))
    forces = [calculator.calculate_force(d) for d in distances]
    
    plt.figure(figsize=(10, 6))
    plt.plot(distances, forces, '-o', label='Gravitational Force')
    plt.title('Gravitational Force vs. Distance')
    plt.xlabel('Distance (m)')
    plt.ylabel('Force (N)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    m1 = float(input("Enter m1 (kg): ").strip() or 0.5)
    m2 = float(input("Enter m2 (kg): ").strip() or 1.5)

    calculator = GravitationalForceCalculator(m1, m2)

    # Plot gravitational force from 100m to 1000m with intervals of 50m
    plot_force_vs_distance(calculator)
