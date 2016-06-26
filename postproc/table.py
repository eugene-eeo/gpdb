from tabulate import tabulate
import newlinejson as nlj
import sys


def main():
    stdin  = sys.stdin

    with nlj.open(stdin) as src:
        data = [line for line in src]
        print(tabulate(data, tablefmt='rst'))


if __name__ == '__main__':
    main()
