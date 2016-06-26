from itertools import islice
from fast_prng import uniform


def knuth_shuffle(items):
    L = len(items)
    for i in range(L):
        j = int(uniform(i, L))
        items[i], items[j] = items[j], items[i]


class Gossiper:
    __slots__ = ('told', 'has_knowledge')

    def __init__(self, data=None):
        self.told = set()
        self.has_knowledge = False

    def tell(self, peers):
        if not self.has_knowledge:
            return 0
        peers = list(peers - self.told)
        if not peers:
            return 0
        some = peers[int(uniform(0, len(peers)))]
        some.send(self)
        self.told.add(some)
        return 1

    def send(self, sender):
        self.told.add(sender)
        self.has_knowledge = True


def simulate(size, bandwidth, messages):
    peers = [Gossiper() for _ in range(size)]
    peers[0].has_knowledge = True

    P = frozenset(peers)
    K = [peers[0]]

    while True:
        quota = bandwidth
        for p in K:
            for _ in range(min(quota, messages)):
                quota -= p.tell(P)
            if quota == 0:
                break

        K = [p for p in peers if p.has_knowledge]
        k = len(K)
        yield k
        if k == size:
            break
        knuth_shuffle(K)
