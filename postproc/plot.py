import sys
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.backends.backend_pdf import PdfPages


def main():
    tbl = defaultdict(dict)
    sys.stdin.readline()
    for line in sys.stdin:
        M, B, mean, _, _ = json.loads(line)
        tbl[M][B] = mean


    with PdfPages('results.pdf') as pdf:
        for i, M in enumerate(sorted(tbl)):
            row = tbl[M]
            plt.title('%d messages' % (M,))
            plt.xlabel('bandwidth')
            plt.ylabel('mean ticks')
            plt.plot(
                row.keys(),
                row.values(),
                'ro',
                )
            plt.grid(True)
            pdf.savefig()
            plt.close()


if __name__ == '__main__':
    main()
