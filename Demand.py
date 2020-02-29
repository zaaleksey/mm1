class Demand:
    count = 0

    def __init__(self, arrival_time):
        Demand.count += 1
        self.id = Demand.count
        self.arrival_time = arrival_time
        self.service_start_time = None
        self.leaving_time = None

    def set_service_start_time(self, service_start_time):
        self.service_start_time = service_start_time

    def set_leaving_time(self, leaving_time):
        self.leaving_time = leaving_time
