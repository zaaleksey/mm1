from dataclasses import dataclass
from queue import Queue

from device import Device


@dataclass
class Configuration:
    mu: float
    lambd: float
    queue: Queue = Queue()
    device: Device = Device()
