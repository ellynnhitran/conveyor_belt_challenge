class Worker:
    """
    Represents a worker in the conveyor belt simulation.
    
    Workers pick up components ('A' or 'B'), assemble products if both components are held, 
    and place finished products on the conveyor.
    """
    
    def __init__(self):
        """
        Initializes a worker with empty hands and no ongoing assembly.
        """
        self.hand_A = False  # Indicates if worker is holding component 'A'
        self.hand_B = False  # Indicates if worker is holding component 'B'
        self.assembling = 0  # Countdown timer for assembly completion
        self.holding_product = False  # True if worker has a completed product but cannot place it yet
        self.placing = False  # True if worker is currently placing a product on the conveyor

    def reset(self):
        """
        Resets worker's state after placing a product.
        """
        self.hand_A = False
        self.hand_B = False
        self.holding_product = False
        self.placing = False

    def pick_item(self, item):
        """
        Allows the worker to pick up a component ('A' or 'B') if they are not already holding it.
        
        :param item: Component to pick ('A' or 'B')
        :return: True if the worker successfully picks the item, False otherwise
        """
        if item == 'A' and not self.hand_A:
            self.hand_A = True
            return True
        elif item == 'B' and not self.hand_B:
            self.hand_B = True
            return True
        return False

    def start_assembling(self, assembly_time):
        """
        Starts the assembly process if the worker has both required components ('A' and 'B').
        
        :param assembly_time: Number of steps required to complete assembly
        """
        if self.hand_A and self.hand_B:
            self.assembling = assembly_time

    def work_on_assembly(self):
        """
        Decrements the assembly timer if the worker is assembling a product.
        """
        if self.assembling > 0:
            self.assembling -= 1

    def is_ready_to_place(self):
        """
        Checks if the worker has completed assembling a product and is ready to place it on the conveyor.
        
        :return: True if the worker has a finished product ready for placement
        """
        return self.assembling == 0 and self.hand_A and self.hand_B
