from demand import Demand


class Device:
    def __init__(self) -> None:
        self.demand = None
        self.serves = False

    def to_occupy(self, demand: Demand) -> None:
        self.demand = demand
        self.serves = True

    def to_free(self) -> None:
        self.demand = None
        self.serves = False

    def get_demand(self) -> Demand:
        return self.demand
