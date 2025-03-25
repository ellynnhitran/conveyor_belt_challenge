from src.simulation import ConveyorBeltSimulation

def main():
    """
    Entry point for running the conveyor belt simulation.
    Displays the final results after completion.
    """
    print("Starting Conveyor Belt Simulation...")
    simulation = ConveyorBeltSimulation()
    simulation.run_simulation()

if __name__ == "__main__":
    main()
