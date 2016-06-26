import sys
from gpdb import simulate
from concurrent.futures import ProcessPoolExecutor
from tabulate import tabulate
import statistics as stats


def task(T):
    B, M = T
    return len(list(simulate(100, bandwidth=B, messages=M)))


def simulate_big(B, M, executor, times):
    u = []
    for k in executor.map(task, ((B,M) for _ in range(times))):
        u.append(k)
    u.sort()
    return (
        stats.mean(u),
        stats.stdev(u),
        stats.median(u),
        )


def main(M, executor, times):
    for B in range(2, 101):
        yield B, simulate_big(B, M, executor, times)


if __name__ == '__main__':
    times = int(sys.argv[2] if len(sys.argv) >= 2 else 50)

    with ProcessPoolExecutor() as executor:
        for M in range(1, 11):
            print('M =', M)
            table = []
            for B, (mean, stdev, median) in main(M, executor, times):
                table.append([B, mean, stdev, median])
            print(tabulate(
                table,
                headers=["B", "mean", "stdev", "median"],
                tablefmt="rst"
                ))
