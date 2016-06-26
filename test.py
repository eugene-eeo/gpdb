"""
Usage:
  test.py [-t T] [-b b] [-B B] [-m m] [-M M]
  test.py (-h | --help)

Options:
  -h --help  show this.
  -t T       no. of iterations  [default: 50].
  -b b       starting bandwidth [default: 2].
  -B B       ending bandwidth   [default: 100].
  -m m       starting messages per node [default: 1].
  -M M       ending messages per node   [default: 10].
"""

import sys
import json
from docopt import docopt
from gpdb import simulate
from concurrent.futures import ProcessPoolExecutor
from statistics import mean, stdev, median


def emit(D):
    print(json.dumps(D))


def task(T):
    B, M = T
    return len(list(simulate(100, bandwidth=B, messages=M)))


def simulate_big(B, M, executor, times):
    arg = (B, M)
    u = sorted(executor.map(
        task,
        (arg for _ in range(times))
        ))
    return mean(u), stdev(u), median(u)


def gensim(M, brange, executor, times):
    for b in range(*brange):
        yield b, simulate_big(b, M, executor, times)


def main():
    args = docopt(__doc__, version='0.1')
    m0, m1 = int(args['-m']), int(args['-M']) + 1
    b0, b1 = int(args['-b']), int(args['-B']) + 1
    T      = int(args['-t'])

    assert m0 < m1
    assert b0 < b1

    brange = (b0, b1)

    emit(['M', 'B', 'mean', 'stdev', 'median'])
    with ProcessPoolExecutor() as executor:
        for M in range(m0, m1):
            for B, (avg, std, q2) in gensim(M, brange, executor, T):
                emit([
                    M, B,
                    avg,
                    std,
                    q2,
                ])


if __name__ == '__main__':
    main()
