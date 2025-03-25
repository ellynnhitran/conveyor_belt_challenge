import random
from src.worker import Worker

class ConveyorBeltSimulation:
    """
    Simulates a conveyor belt system where workers pick components, assemble products, 
    and place finished products on the conveyor.
    """
    def __init__(self, steps=100, conveyor_len=3, assembly_time=4, workers_per_slot=2):
        """
        Initializes the simulation parameters.
        
        :param steps: Number of simulation cycles
        :param conveyor_len: Number of slots in the conveyor belt
        :param assembly_time: Time required to assemble a product
        :param workers_per_slot: Number of workers per conveyor slot
        """
        self.steps = steps
        self.conveyor_len = conveyor_len
        self.assembly_time = assembly_time
        self.workers_per_slot = workers_per_slot
        self.conveyor_belt = [None] * conveyor_len  # Initialize conveyor belt with empty slots
        self.worker_pairs = [[Worker() for _ in range(workers_per_slot)] for _ in range(conveyor_len)]  # Assign workers
        self.finished_products = 0  # Counter for completed products
        self.unused_components = {'A': 0, 'B': 0}  # Track unused components
        self.recipe = {'C': {'A': 1, 'B': 1}}  # Define assembly recipe
        self.component_probabilities = {'A': 1/3, 'B': 1/3, None: 1/3}  # Probability distribution for components

    def generate_random_component(self):
        """
        Generates a random component ('A', 'B', or None) based on predefined probabilities.
        
        :return: A randomly selected component
        """
        return random.choices(list(self.component_probabilities.keys()), weights=self.component_probabilities.values())[0]

    def move_conveyor(self):
        """
        Moves the conveyor belt forward by shifting components.
        Tracks and stores unused components if removed from the belt.
        """
        removed_component = self.conveyor_belt.pop()
        self.conveyor_belt.insert(0, self.generate_random_component())
        if removed_component in ['A', 'B']:
            self.unused_components[removed_component] += 1  # Store unused components

    def worker_action(self, slot_index):
        """
        Manages worker actions at a specific conveyor slot.
        Workers pick up components, start assembly, and continue working on products.
        
        :param slot_index: Index of the conveyor slot being processed
        """
        workers = sorted(self.worker_pairs[slot_index], key=lambda w: w.assembling)

        for worker in workers:
            if worker.assembling > 0:
                worker.work_on_assembly()  # Continue assembling if in progress
                continue

            if worker.is_ready_to_place():
                continue  # Skip if worker is ready to place the product

            if any(w.placing for w in workers if w != worker):
                continue  # Prevent multiple workers from placing at the same time

            if self.conveyor_belt[slot_index] and worker.pick_item(self.conveyor_belt[slot_index]):
                self.conveyor_belt[slot_index] = None
                if worker.hand_A and worker.hand_B:
                    worker.start_assembling(self.assembly_time)  # Start assembling if both components are held

    def place_product(self, slot_index):
        """
        Allows workers to place finished products on the conveyor belt.
        Ensures that only one worker places a product at a time.
        
        :param slot_index: Index of the conveyor slot being processed
        """
        workers = self.worker_pairs[slot_index]
        placing_workers = [worker for worker in workers if worker.is_ready_to_place()]

        if len(placing_workers) > 1:
            placing_workers = [placing_workers[0]]  # Allow only one worker to place the product

        for worker in placing_workers:
            if self.conveyor_belt[slot_index] is None:
                worker.placing = True
                self.conveyor_belt[slot_index] = 'C'  # Place finished product
                worker.reset()  # Reset worker's state after placing
                self.finished_products += 1
                worker.placing = False
            else:
                worker.holding_product = True  # Worker holds the product if space is occupied

    def run_simulation(self):
        """
        Runs the conveyor belt simulation for the specified number of steps.
        """
        for _ in range(self.steps):
            self.move_conveyor()
            for i in range(self.conveyor_len):
                self.worker_action(i)
                self.place_product(i)

        # Count remaining products still held by workers
        for workers in self.worker_pairs:
            for worker in workers:
                if worker.holding_product:
                    self.finished_products += 1

        self.display_results()

    def display_results(self):
        """
        Displays the final simulation results, including the total number of finished products
        and unused components.
        """
        print(f'Finished Products: {self.finished_products}')
        print(f'Unused Components: {self.unused_components}')
