#!/usr/bin/env python

import sys
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.backends.backend_pdf import PdfPages
from statistics import median


def main():
    tbl = defaultdict(dict)
    sys.stdin.readline()
    for line in sys.stdin:
        M, B, ticks = json.loads(line)
        ticks.sort()
        tbl[B][M] = median(ticks), (max(ticks) - min(ticks)) / 2.0


    with PdfPages('results.pdf') as pdf:
        for i, B in enumerate(sorted(tbl)):
            row = tbl[B]
            plt.title('Bandwidth (B): %d messages' % (B,))
            plt.xlabel('messages per node (M)')
            plt.ylabel('ticks')
            plt.errorbar(
                list(row.keys()),
                [y for y, _ in row.values()],
                fmt='bo',
                yerr=[err for _, err in row.values()])
            plt.grid(True)
            pdf.savefig()
            plt.close()


if __name__ == '__main__':
    main()
