gpdb
====

An experiment in modelling a gossip protocol of **N** peers, subject
to each node sending **M** messages, and a bandwidth of **B** messages
on each tick, i.e. the number of messages sent at each tick is at most
**B**. Assumptions:

- A fully reliable network, where no messages are dropped as long
  as fewer than **B** messages are sent.
- All messages after **B** messages are sent are dropped.
- Any nodes can send to any other node in the network.
- All nodes send messages at specific times.
- Nodes will fire and forget messages.
- At each tick they will randomly pick at most **M** distinct nodes
  that they have not communicated with (sent to/received from) and
  send messages to them.

What is being measured is the number of iterations/ticks required in
order to make every peer/node aware of the message.

Default simulation parameters:

- **N = 100**
- **2 ≤ B ≤ 100**
- **1 ≤ M ≤ 20**

Instructions
------------

To run the simulations::

    $ pip install statistics # pypy or python2
    $ make install
    $ make
    # optional, needs framework python.
    $ cat stats.jsonl | postproc/plot.py


TODO:
-----

- Model network 'partitions', where each nodes belong to evenly
  sized clusters that can only communicate amongst one another,
  and have a 'leader' which can communicate with leaders from any
  other clusters. However the messages sent within and across
  clusters are also subject to bandwidth **B**.
