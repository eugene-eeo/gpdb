"""
Usage:
  test.py [-t T] [-B brange] [-M mrange] [--debug]
  test.py (-h | --help)

Options:
  -h --help  show this.
  -t T       no. of iterations          [default: 50].
  -B brange  bandwidth (min,max,step)   [default: 1,100,5].
  -M mrange  messages  (min,max,step)   [default: 1,10,1].
  --debug    show debug info.
"""

from time import time
import sys
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from docopt import docopt

import newlinejson as nlj
from gpdb import simulate


def parse_step(step):
    m, M, s = tuple(int(k) for k in step.split(','))
    return (m, M+1, s)


def task(arg):
    M, B = arg
    return len(list(simulate(100, bandwidth=B, messages=M)))


def run(mrange, brange, executor, times):
    for M in range(*mrange):
        for B in range(*brange):
            if B < M:
                continue
            start = time()
            results = list(executor.map(
                task,
                repeat((M, B), times)
                ))
            end = time()
            dt = end - start
            yield M, B, results, dt


def main():
    args = docopt(__doc__, version='0.1')
    mrange = parse_step(args['-M'])
    brange = parse_step(args['-B'])
    times  = int(args['-t'])
    debug  = args['--debug']
    stderr = sys.stderr

    with nlj.open(sys.stdout, 'w') as dst:
        dst.write(['M', 'B', 'results'])
        with ProcessPoolExecutor() as exe:
            for M, B, R, dt in run(mrange, brange, exe, times):
                if debug:
                    stderr.write('M=%d, B=%d, t=%f\n' % (M, B, dt))
                    stderr.flush()
                dst.write([M, B, R])


if __name__ == '__main__':
    main()
