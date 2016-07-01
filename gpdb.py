from itertools import islice
from random import choice, shuffle


class Gossiper:
    __slots__ = ('told', 'has_knowledge')

    def __init__(self, data=None):
        self.told = set()
        self.has_knowledge = False

    def tell(self, peers):
        if not self.has_knowledge:
            return False
        peers = peers - self.told
        if peers:
            some = choice(list(peers))
            some.send(self)
            self.told.add(some)
            return True
        return False

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
                sent = p.tell(P)
                if not sent:
                    break
                quota -= 1
            if quota == 0:
                break

        K = [p for p in peers if p.has_knowledge]
        k = len(K)
        yield k
        if k == size:
            break
        shuffle(K)
