gpdb
====

An experiment in modelling a gossip protocol of **N** peers, subject
to each node sending **M** messages, and a bandwidth of **B** messages
on each tick, i.e. the number of messages sent at each tick is at most
**B**. Assumptions:

- A fully reliable network, where no messages are dropped as long
  as fewer than **B** are sent.
- All messages after **B** messages are sent are dropped.
- Nodes will fire and forget messages.
- Any nodes can send to any other node in the network. In practice
  this is far from the truth, but for simplicity we will make this
  assumption.
- All nodes send messages at specific times.
- Nodes will not send messages to those that they have received
  messages from, or those which they have already sent to.

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
    $ cat stats.jsonl | postproc/table.py # optional


TODO:
-----

- Model network 'partitions', where each nodes belong to evenly
  sized clusters that can only communicate amongst one another,
  and have one link to another cluster. However the messages
  sent within and across clusters are also subject to bandwidth
  **B**. This is more realistic as we tend to have a network
  topology of multiple 'clusters' when we want to use gossip
  protocols.
