#!/usr/bin/env python

from tabulate import tabulate
import newlinejson as nlj
import sys


def main():
    stdin  = sys.stdin

    with nlj.open(stdin) as src:
        cols = next(src)
        data = [line for line in src]
        print(tabulate(data, tablefmt='rst', headers=cols))


if __name__ == '__main__':
    main()
