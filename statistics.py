from dataclasses import dataclass

from demand import Demand


@dataclass
class Statistics:
    average_time: float = 0
    leaving_count: int = 0

    def update(self, demand: Demand) -> None:
        self.average_time += demand.leaving_time - demand.arrival_time
        self.leaving_count += 1
