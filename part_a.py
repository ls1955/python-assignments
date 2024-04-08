import matplotlib.pyplot as plt

class GravitationalForceCalculator:
    def __init__(self, m1, m2, G=6.674 * 10**-11):
        self.m1 = m1
        self.m2 = m2
        self.G = G

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
    # Collecting user inputs for masses of the two bodies
    print("Enter the mass of the first body (in kg):")
    m1 = float(input())
    print("Enter the mass of the second body (in kg):")
    m2 = float(input())
    
    # The gravitational constant G is set to a fixed value
    G = 6.674 * 10**-11  # N*m^2/kg^2
    
    calculator = GravitationalForceCalculator(m1, m2, G)
    
    # Plot gravitational force from 100m to 1000m with intervals of 50m
    plot_force_vs_distance(calculator)
