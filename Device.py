class Device:

    def __init__(self, demand=None):
        self.demand = demand
        self.serves = False

    def service_demand(self, demand):
        self.demand = demand

    def get_demand(self):
        return self.demand

    def to_occupy(self):
        self.serves = True

    def to_free(self):
        self.serves = False
