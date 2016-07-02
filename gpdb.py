from itertools import islice
from random import choice, shuffle


class Node:
    __slots__ = ('told', 'has_knowledge', 'peers')

    def __init__(self):
        self.told = set()
        self.has_knowledge = False
        self.peers = None

    def tell(self):
        if not self.has_knowledge:
            return
        peers = self.peers - self.told
        peers.remove(self)
        if peers:
            some = choice(list(peers))
            some.send(self)
            self.told.add(some)
            return some
        return

    def send(self, sender):
        self.told.add(sender)
        self.has_knowledge = True


def allocate(size):
    peers = [Node() for _ in range(size)]
    P = set(peers)
    for node in peers:
        node.peers = P

    start = peers[0]
    start.has_knowledge = True
    return peers, start


def simulate(size, bandwidth, messages):
    peers, start = allocate(size)
    K = [start]
    knows = {start}

    while True:
        quota = bandwidth
        for p in K:
            for _ in range(min(quota, messages)):
                node = p.tell()
                if not node:
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
        shuffle(K)
