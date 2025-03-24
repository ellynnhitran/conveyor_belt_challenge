class Worker:
    def __init__(self):
        self.hand_A = False
        self.hand_B = False
        self.assembling = 0
        self.holding_product = False
        self.placing = False

    def reset(self):
        self.hand_A = False
        self.hand_B = False
        self.holding_product = False
        self.placing = False

    def pick_item(self, item):
        if item == 'A' and not self.hand_A:
            self.hand_A = True
            return True
        elif item == 'B' and not self.hand_B:
            self.hand_B = True
            return True
        return False

    def start_assembling(self, assembly_time):
        if self.hand_A and self.hand_B:
            self.assembling = assembly_time

    def work_on_assembly(self):
        if self.assembling > 0:
            self.assembling -= 1

    def is_ready_to_place(self):
        return self.assembling == 0 and self.hand_A and self.hand_B
