from itertools import islice
from random import choice, shuffle


class Node:
    __slots__ = ('told', 'has_knowledge', 'peers')

    def __init__(self):
        self.told = set()
        self.has_knowledge = False
        self.peers = None

    def tell(self):
        if self.has_knowledge:
            peers = self.peers - self.told
            if peers:
                some = choice(list(peers))
                some.send(self)
                self.told.add(some)
                return some, True
        return None, False

    def send(self, sender):
        self.told.add(sender)
        self.has_knowledge = True


def allocate(size):
    peers = set(Node() for _ in range(size))
    for node in peers:
        node.peers = peers - {node}

    start = next(iter(peers))
    start.has_knowledge = True
    return start


def simulate(size, bandwidth, messages):
    start = allocate(size)
    K = [start]
    knows = {start}

    while True:
        quota = bandwidth
        shuffle(K)
        for p in K:
            # to make sure we do not send more than B messages
            # we need to check if we have any remaining quota.
            for _ in range(min(quota, messages)):
                node, ok = p.tell()
                if not ok:
                    break
                knows.add(node)
                quota -= 1
            if quota == 0:
                break

        K = list(knows)
        k = len(knows)
        yield k
        if k == size:
            break
