import random
from itertools import islice


class Gossiper:
    __slots__ = ('told', 'has_knowledge')

    def __init__(self, data=None):
        self.told = set()
        self.has_knowledge = False

    def tell(self, peers):
        if not self.has_knowledge:
            return 0
        peers = peers - self.told
        if not peers:
            return 0
        some = random.choice(list(peers))
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
    knows = 1

    while knows != size:
        available = bandwidth
        for p in [p for p in peers if p.has_knowledge]:
            for _ in range(min(available, messages)):
                available -= p.tell(P)
            if available == 0:
                break

        knows = sum(1 for k in peers if k.has_knowledge)
        yield knows
        random.shuffle(peers)
