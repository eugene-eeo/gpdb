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

The simulations are best run in PyPy and a multi-core machine where it
will work it's JIT magic and make the code run hopefully faster.
However I will still optimise the code from time to time. Currently
the results (50 iterations on a 4-core machine, will improve once
I get to run it on a more powerful machine) can be found in the
``results.txt`` file.
