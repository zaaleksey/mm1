class Device:
    def __init__(self):
        self.demand = None
        self.serves = False

    def to_occupy(self, demand):
        self.demand = demand
        self.serves = True

    def to_free(self):
        self.demand = None
        self.serves = False

    def get_demand(self):
        return self.demand
