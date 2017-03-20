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
    with nlj.open(sys.stdin) as src:
        cols = next(src)
        print(tabulate(
            src,
            tablefmt=args['--fmt'],
            headers=cols))


if __name__ == '__main__':
    main()
