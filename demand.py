class Demand:
    __COUNT = 0

    def __init__(self, arrival_time: float) -> None:
        Demand.__COUNT += 1
        self.id = Demand.__COUNT
        self.arrival_time = arrival_time
        self.service_start_time = None
        self.leaving_time = None

    def set_service_start_time(self, service_start_time: float) -> None:
        self.service_start_time = service_start_time

    def set_leaving_time(self, leaving_time: float) -> None:
        self.leaving_time = leaving_time
