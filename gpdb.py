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
    knows = {start}

    while True:
        quota = bandwidth
        T = {node: messages for node in knows}
        while T and quota > 0:
            node, count = T.popitem()
            if count == 0:
                continue
            peer, ok = node.tell()
            if not ok:
                continue
            knows.add(peer)
            T[node] = count - 1
            quota -= 1

        k = len(knows)
        yield k
        if k == size:
            break
