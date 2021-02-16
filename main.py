from simulation import run

if __name__ == '__main__':
    lambd = 1
    mu = 2

    simulation_time = 100000

    run(mu=mu, lambd=lambd, simulation_time=simulation_time)
