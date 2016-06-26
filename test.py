import sys
from gpdb import simulate
from concurrent.futures import ProcessPoolExecutor
from tabulate import tabulate
import statistics as stats


def simulate_big(N, M, executor, times):
    u = []
    task = lambda _: len(list(simulate(100, bandwidth=N, messages=M)))
    for k in executor.map(task, range(times)):
        u.append(k)
    u.sort()
    return (
        stats.mean(u),
        stats.stdev(u),
        stats.median(u),
        )


def main(M, executor, times):
    for N in range(2, 101):
        yield N, simulate_big(N, M, executor, times)


if __name__ == '__main__':
    times = int(sys.argv[2] if len(sys.argv) >= 2 else 50)

    with ProcessPoolExecutor() as executor:
        for M in range(1, 11):
            print(M, 'message(s) per tick:')
            table = []
            for N, (mean, stdev, median) in main(M, executor, times):
                table.append([N, mean, stdev, median])
            print(tabulate(
                table,
                headers=["bandwidth", "mean", "stdev", "median"],
                tablefmt="rst"
                ))
