import random
from src.worker import Worker

class ConveyorBeltSimulation:
    def __init__(self, steps=100, conveyor_len=3, assembly_time=4, workers_per_slot=2):
        self.steps = steps
        self.conveyor_len = conveyor_len
        self.assembly_time = assembly_time
        self.workers_per_slot = workers_per_slot
        self.conveyor_belt = [None] * conveyor_len
        self.worker_pairs = [[Worker() for _ in range(workers_per_slot)] for _ in range(conveyor_len)]
        self.finished_products = 0
        self.unused_components = {'A': 0, 'B': 0}
        self.recipe = {'C': {'A': 1, 'B': 1}}
        self.component_probabilities = {'A': 1/3, 'B': 1/3, None: 1/3}

    def generate_random_component(self):
        return random.choices(list(self.component_probabilities.keys()), weights=self.component_probabilities.values())[0]

    def move_conveyor(self):
        removed_component = self.conveyor_belt.pop()
        self.conveyor_belt.insert(0, self.generate_random_component())
        if removed_component in ['A', 'B']:
            self.unused_components[removed_component] += 1

    def worker_action(self, slot_index):
        workers = sorted(self.worker_pairs[slot_index], key=lambda w: w.assembling)

        for worker in workers:
            if worker.assembling > 0:
                worker.work_on_assembly()
                continue

            if worker.is_ready_to_place():
                continue

            if any(w.placing for w in workers if w != worker):
                continue

            if self.conveyor_belt[slot_index] and worker.pick_item(self.conveyor_belt[slot_index]):
                self.conveyor_belt[slot_index] = None
                if worker.hand_A and worker.hand_B:
                    worker.start_assembling(self.assembly_time)

    def place_product(self, slot_index):
        workers = self.worker_pairs[slot_index]
        placing_workers = [worker for worker in workers if worker.is_ready_to_place()]

        if len(placing_workers) > 1:
            placing_workers = [placing_workers[0]]

        for worker in placing_workers:
            if self.conveyor_belt[slot_index] is None:
                worker.placing = True
                self.conveyor_belt[slot_index] = 'C'
                worker.reset()
                self.finished_products += 1
                worker.placing = False
            else:
                worker.holding_product = True

    def run_simulation(self):
        for _ in range(self.steps):
            self.move_conveyor()
            for i in range(self.conveyor_len):
                self.worker_action(i)
            for i in range(self.conveyor_len):
                self.place_product(i)

        for workers in self.worker_pairs:
            for worker in workers:
                if worker.holding_product:
                    self.finished_products += 1

        self.display_results()

    def display_results(self):
        print(f'Finished Products: {self.finished_products}')
        print(f'Unused Components: {self.unused_components}')
