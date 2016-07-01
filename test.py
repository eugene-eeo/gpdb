"""
Usage:
  test.py [-t T] [-b b] [-B B] [-m m] [-M M] [--debug]
  test.py (-h | --help)

Options:
  -h --help  show this.
  -t T       no. of iterations  [default: 50].
  -b b       starting bandwidth [default: 2].
  -B B       ending bandwidth   [default: 100].
  -m m       starting messages per node [default: 1].
  -M M       ending messages per node   [default: 10].
  --debug    show debug info.
"""

from time import time
import sys
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from docopt import docopt

import newlinejson as nlj
from gpdb import simulate


def task(arg):
    M, B = arg
    return len(list(simulate(100, bandwidth=B, messages=M)))


def run(dst, mrange, brange, executor, times, debug):
    stderr = sys.stderr
    dst.write(['M', 'B', 'results'])
    for M in range(*mrange):
        for B in range(*brange):
            start = time()
            results = list(executor.map(
                task,
                repeat((M, B), times)
                ))
            end = time()
            if debug:
                stderr.write('M=%d, B=%d, t=%f\n' % (M, B, end-start))
                stderr.flush()
            dst.write([M, B, results])


def main():
    args = docopt(__doc__, version='0.1')
    m0, m1 = int(args['-m']), int(args['-M']) + 1
    b0, b1 = int(args['-b']), int(args['-B']) + 1
    times  = int(args['-t'])
    debug  = args['--debug']

    assert m0 < m1
    assert b0 < b1

    mrange = (m0, m1)
    brange = (b0, b1)

    with nlj.open(sys.stdout, 'w') as dst:
        with ProcessPoolExecutor() as exe:
            run(dst, mrange, brange, exe, times, debug)


if __name__ == '__main__':
    main()
