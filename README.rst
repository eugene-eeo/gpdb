gpdb
====

An experiment in modelling a gossip protocol of **N** peers,
subject to each node sending **M** messages, and a bandwidth
of **B** messages on each tick. Assumptions:

- A fully reliable network, where no messages are dropped as long
  as fewer than **B** messages are sent.
- All messages after **B** messages are sent are dropped.
- Any node can send to any other node in the network.
- All nodes send messages at specific times.
- At each tick random nodes will communicate with at most **M**
  random, distinct nodes that they have not sent to/received from.

What is being measured is the number of iterations/ticks required
in order to make every node aware of the message. Typically the
lower the number of ticks, the better. But this comes with a cost
in **B** and **M**.

Default simulation parameters:

- **N = 100**
- **50 ≤ B ≤ 500**
- **1 ≤ M ≤ 20**

Instructions
------------

To run the simulations and plot the results::

    $ pip install statistics # pypy or python2
    $ make install
    $ make


TODO:
-----

- Model network 'partitions', where each nodes belong to evenly
  sized clusters that can only communicate amongst one another,
  and have a 'leader' which can communicate with leaders from any
  other clusters. However the messages sent within and across
  clusters are also subject to bandwidth **B**.
