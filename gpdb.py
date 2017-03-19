from itertools import islice
from random import shuffle, choice


class Node:
    __slots__ = ('has_knowledge', 'peers')

    def __init__(self):
        self.has_knowledge = False
        self.peers = None

    def tell(self):
        if self.has_knowledge and self.peers:
            peer = choice(list(self.peers))
            peer.recv(self)
            self.peers.remove(peer)
            return peer, True
        return None, False

    def recv(self, sender):
        self.peers.remove(sender)
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
