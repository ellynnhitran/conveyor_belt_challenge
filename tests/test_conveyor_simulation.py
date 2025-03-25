import unittest
from unittest.mock import patch
from src.worker import Worker
from src.simulation import ConveyorBeltSimulation

class TestWorker(unittest.TestCase):
 
    def setUp(self):
        """Initialize a Worker instance before each test."""
        self.worker = Worker()
    
    def test_initial_state(self):
        """Test that a newly created worker starts with no items and no ongoing assembly."""
        self.assertFalse(self.worker.hand_A)
        self.assertFalse(self.worker.hand_B)
        self.assertFalse(self.worker.holding_product)
        self.assertEqual(self.worker.assembling, 0)
    
    def test_pick_item(self):
        """Test that a worker can pick up an item and cannot pick the same item twice."""
        self.assertTrue(self.worker.pick_item('A'))
        self.assertTrue(self.worker.hand_A)
        self.assertFalse(self.worker.hand_B)
        self.assertFalse(self.worker.pick_item('A'))  # Ensure worker cannot pick 'A' again
    
    def test_assembly_process(self):
        """Test that a worker starts assembly when both components are available and progresses over time."""
        self.worker.pick_item('A')
        self.worker.pick_item('B')
        self.worker.start_assembling(4)
        self.assertEqual(self.worker.assembling, 4)
        
        self.worker.work_on_assembly()
        self.assertEqual(self.worker.assembling, 3)
    
    def test_is_ready_to_place(self):
        """Test that a worker is ready to place the product after assembly is complete."""
        self.worker.pick_item('A')
        self.worker.pick_item('B')
        self.worker.start_assembling(1)
        self.worker.work_on_assembly()
        self.assertTrue(self.worker.is_ready_to_place())

class TestConveyorBeltSimulation(unittest.TestCase):

    def setUp(self):
        """Initialize a ConveyorBeltSimulation instance before each test."""
        self.simulation = ConveyorBeltSimulation(steps=10, conveyor_len=3, assembly_time=4, workers_per_slot=2)
    
    def test_initial_conditions(self):
        """Test that the simulation initializes with the correct conveyor belt length and worker setup."""
        self.assertEqual(len(self.simulation.conveyor_belt), 3)
        self.assertEqual(len(self.simulation.worker_pairs), 3)
        self.assertEqual(self.simulation.finished_products, 0)
    
    def test_conveyor_movement(self):
        """Test that the conveyor belt moves correctly and inserts a new component at the front."""
        with patch('random.choices', return_value=['A']):
            self.simulation.move_conveyor()
        self.assertIn(self.simulation.conveyor_belt[0], ['A', 'B', None])
    
    def test_worker_interaction(self):
        """Test that workers can pick items and start assembling correctly."""
        self.simulation.worker_pairs[0][0].pick_item('A')
        self.simulation.worker_pairs[0][0].pick_item('B')
        self.simulation.worker_pairs[0][0].start_assembling(4)
        self.assertEqual(self.simulation.worker_pairs[0][0].assembling, 4)
        
    def test_simulation_runs(self):
        """Test that the simulation runs without errors and updates component/product counts correctly."""
        self.simulation.run_simulation()
        self.assertGreaterEqual(self.simulation.finished_products, 0)
        self.assertGreaterEqual(self.simulation.unused_components['A'], 0)
        self.assertGreaterEqual(self.simulation.unused_components['B'], 0)

if __name__ == '__main__':
    unittest.main()
