from random import expovariate as exp
from queue import Queue

from demand import Demand
from device import Device


def imitation(par=None, time=999999):
    if par is None:
        par = {"la": 0.5, "mu": 1}
    times = {
        "current": 0,
        "arrival": exp(par["la"]),
        "service": float("inf"),
        "leaving": float("inf"),
    }
    stat = {
        "average_time": 0,
        "leaving_count": 0,
    }
    queue = Queue()
    device = Device()
    system = {
        "par": par,
        "queue": queue,
        "device": device,
    }

    loop(time, times, system, stat)


def loop(time, times, system, stat):
    while times["current"] <= time:
        times["current"] = min(times["arrival"], times["service"], times["leaving"])
        if times["current"] == times["arrival"]:
            arrival_demand(times, system)
            continue
        if times["current"] == times["service"]:
            service_demand(times, system)
            continue
        if times["current"] == times["leaving"]:
            leaving_demand(times, system, stat)
            continue
    print(stat["average_time"] / stat["leaving_count"])


def arrival_demand(times, system):
    print("I. Arrival demand", times["current"], end="\t###\t")
    demand = Demand(times["arrival"])
    print("demand ID:", demand.id)
    if system["queue"].empty() and not system["device"].serves:
        times["service"] = times["current"]
    system["queue"].put(demand)
    times["arrival"] += exp(system["par"]["la"])


def service_demand(times, system):
    print("II. Start service demand", times["current"], end="\t###\t")
    service_time = exp(system["par"]["mu"])
    times["leaving"] = times["current"] + service_time
    system["device"].to_occupy(system["queue"].get())
    print("demand ID:", system["device"].demand.id)
    system["device"].demand.service_start_time = times["current"]
    times["service"] = float('inf')


def leaving_demand(times, system, stat):
    print("III. Leaving demand", times["current"], end="\t###\t")
    demand = system["device"].get_demand()
    print("demand ID:", demand.id)
    system["device"].to_free()
    demand.set_leaving_time(times["current"])
    stat["average_time"] += demand.leaving_time - demand.arrival_time
    stat["leaving_count"] += 1
    if not system["queue"].empty():
        times["service"] = times["current"]
    times["leaving"] = float('inf')


if __name__ == '__main__':
    la = 1
    mu = 2
    init = {"la": la, "mu": mu}
    imitation()
