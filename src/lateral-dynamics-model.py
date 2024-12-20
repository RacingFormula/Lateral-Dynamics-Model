import numpy as np
import matplotlib.pyplot as plt

class LateralDynamicsModel:
    def __init__(self, config):
        self.vehicle_mass = config.get("vehicle_mass", 800)  # kg
        self.tyre_grip_coefficient = config.get("tyre_grip_coefficient", 1.2)  # Coefficient of friction
        self.corner_radius = config.get("corner_radius", 50)  # metres
        self.suspension_stiffness = config.get("suspension_stiffness", 15000)  # N/m
        self.cg_height = config.get("cg_height", 0.5)  # metres
        self.track_width = config.get("track_width", 1.6)  # metres

    def calculate_lateral_force(self, speed):
        # Calculate lateral force: F = mv^2 / r
        return (self.vehicle_mass * speed**2) / self.corner_radius

    def calculate_weight_transfer(self, lateral_force):
        # Calculate weight transfer: ΔW = (F * h) / t
        return (lateral_force * self.cg_height) / self.track_width

    def simulate_dynamics(self, speeds):
        lateral_forces = []
        weight_transfers = []

        for speed in speeds:
            lat_force = self.calculate_lateral_force(speed)
            weight_transfer = self.calculate_weight_transfer(lat_force)

            lateral_forces.append(lat_force)
            weight_transfers.append(weight_transfer)

        return {
            "speeds": speeds,
            "lateral_forces": lateral_forces,
            "weight_transfers": weight_transfers
        }

    def plot_results(self, results):
        speeds = results["speeds"]
        lateral_forces = results["lateral_forces"]
        weight_transfers = results["weight_transfers"]

        plt.figure(figsize=(12, 6))

        # Plot lateral forces
        plt.subplot(2, 1, 1)
        plt.plot(speeds, lateral_forces, label="Lateral Force", color="blue")
        plt.title("Lateral Force vs Speed")
        plt.xlabel("Speed (m/s)")
        plt.ylabel("Lateral Force (N)")
        plt.legend()
        plt.grid(True)

        # Plot weight transfer
        plt.subplot(2, 1, 2)
        plt.plot(speeds, weight_transfers, label="Weight Transfer", color="red")
        plt.title("Weight Transfer vs Speed")
        plt.xlabel("Speed (m/s)")
        plt.ylabel("Weight Transfer (N)")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    config = {
        "vehicle_mass": 800,
        "tyre_grip_coefficient": 1.2,
        "corner_radius": 50,
        "suspension_stiffness": 15000,
        "cg_height": 0.5,
        "track_width": 1.6
    }

    model = LateralDynamicsModel(config)
    speeds = np.linspace(10, 50, 100)  # Speeds from 10 m/s to 50 m/s
    results = model.simulate_dynamics(speeds)
    model.plot_results(results)