from statistics import mean, median, stdev
import newlinejson as nlj
import sys


def main():
    stdin  = sys.stdin
    stdout = sys.stdout

    with nlj.open(stdin) as src:
        with nlj.open(stdout, 'w') as dst:
            dst.write(['M', 'B', 'mean', 'median', 'stdev'])
            next(src)
            for line in src:
                M, B, R = line
                R.sort()
                dst.write([
                    M,
                    B,
                    mean(R),
                    median(R),
                    stdev(R),
                ])

if __name__ == '__main__':
    main()
