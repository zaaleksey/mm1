from queue import Queue
import random
import time

from Demand import Demand
from Device import Device


class MM1:

    def __init__(self, la=0.5, mu=1.0):
        self.la = la
        self.mu = mu

        self.current_time = 0
        self.arrival_time = random.expovariate(self.la)
        self.service_start_time = float('inf')
        self.leaving_time = float('inf')

        self.average_time = 0
        self.leaving_count = 0

        self.queue = Queue()
        self.device = Device()

    def receipt_of_demand(self):
        print("Требование поступило", self.current_time, end=" ||| ")
        demand = Demand(self.arrival_time)
        print("Demand ID:", demand.id)
        if self.queue.empty() and not self.device.serves:
            self.service_start_time = self.current_time
        self.queue.put(demand)
        self.arrival_time += random.expovariate(self.la)

    def service_start(self):
        print("Требование начало обслуживаться", self.current_time, end=" ||| ")
        service_time = random.expovariate(self.mu)
        self.leaving_time = self.current_time + service_time
        self.device.service_demand(self.queue.get())
        self.device.to_occupy()
        print("Demand ID:", self.device.demand.id)
        self.device.demand.service_start_time = self.current_time
        self.service_start_time = float('inf')

    def leaving_demand(self):
        print("Требование покинуло систему", self.current_time, end=" ||| ")
        demand = self.device.get_demand()
        print("Demand ID:", demand.id)
        self.device.to_free()
        demand.set_leaving_time(self.current_time)
        self.average_time += demand.leaving_time - demand.arrival_time
        self.leaving_count += 1
        if not self.queue.empty():
            self.service_start_time = self.current_time
        self.leaving_time = float('inf')

    def main(self, time_simulation=1000000  ):
        while self.current_time <= time_simulation:
            self.current_time = min(self.arrival_time, self.service_start_time, self.leaving_time)
            if self.current_time == self.arrival_time:
                self.receipt_of_demand()
                time.sleep(0.5)
                continue
            if self.current_time == self.service_start_time:
                self.service_start()
                time.sleep(0.5)
                continue
            if self.current_time == self.leaving_time:
                self.leaving_demand()
                time.sleep(0.5)
                continue
        print(self.average_time / self.leaving_count)


if __name__ == '__main__':
    system = MM1()
    system.main()
