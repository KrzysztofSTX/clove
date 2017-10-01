import zmq
import time
import sys
from  multiprocessing import Process

# UNDER CONSTRUCTION

'''
Miner duties:
~~~~~~~~~~~~~~
1. receive info from contractors
    - this gives them ( contractor_address,
                        source_code )
2. Compile contract into bytecode
    - this gives them (bytecode,
                       ABI )
3. Propagate their and others' bytecode / ABI
    - to avoid needing brokers or intermediary routers,
      miners can be their own brokers as part of their mining
      duty. This includes:
        1 managing ports at which bytecode per contract is
          published
        2 managing ports at which miners listen for sources
        3 managing ports and accounts of current miners online,
          to be published on a few separate administrative ports
    - the above can be accomplished by 'Listen, Poll, Send':
        - miners poll: (4 things)
            - bytecode variations
            - ports used for listening, pulling, and pushing
        - miners keep track of:
            - specific initial contract addresses they keep
              from the first initialization in order to filter
              incoming messages, limiting each to working with
              a certain number of contracts at a time.
            - other miners who consent to a bytecode variation
'''



def source_listener( ports = ['5556'],
                     message_limit = 10,
                     frequency = 1
                     delimiter = '///'
                     ):
    '''
    Listens at all given ports in a list for new source code
    published by contract creators.
    
    Input arguments:
    ~~~~~~~~~~~~~~~~
    - list of ports, ports as strings
    - limit of messages to listen for
    - frequency of time to receive messages
    - delimiter used in parsing messages
    '''
    context = zmq.Context()
    socket = context.socket(zmq.SUB )

    # connect this socket to all ports. 
    for port in ports:
        socket.connect("tcp://*:%s" % port)

    # listen at the given ports until the specified number of
    # messages is received for further processing.
    messages = []

    while len(messages) < message_limit:
        message = socket.recv()

        # assert message is the correct format,
        # or parse it here:
        # so far it is [ contractor_address /// source_code ]
        message = message.split( delimiter )
        try:
            assert len(message) == 2
            message[0] = message[0].lstrip().rstrip()
            message[1] = message[1].lstrip().rstrip()
            messages.append(message)
        else:
            pass
        
        time.sleep( frequency )

    return messages
        
        
        
def miner_listener(  ports = ['5556'],
                     message_limit = 10,
                     frequency = 1
                     delimiter = '///'
                     ):
    '''
    The format of the messages miners are assumed ot send each other:
    At mining ports, miners push bytecode, variations,
    and consensus polls.
    '''


def router():
    '''
    '''
    pass

