#!/usr/bin/env python
"""
Usage:
  table.py [--fmt=<format>]
  table.py (--help | -h)

Options:
  --fmt=<format>   Table format to use. [default:rst]
  --help -h        Shows the current screen.
"""

import docopt
from tabulate import tabulate
import newlinejson as nlj
import sys


def main():
    args = docopt.docopt(__doc__)
    tfmt = args['--fmt']
    stdin = sys.stdin

    with nlj.open(stdin) as src:
        cols = next(src)
        data = [line for line in src]
        print(tabulate(data, tablefmt=tfmt, headers=cols))


if __name__ == '__main__':
    main()
