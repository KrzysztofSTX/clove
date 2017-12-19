import zmq
import time

# TODO: set authors to listen by
# TODO: filter changes once an author's message is received
    
def source_listener( ports = ['5556'],
                     addresses = ['127.0.0.1'],
                     message_limit = 10,
                     frequency = 1,
                     delimiter = '///',
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
        for address in addresses:
            socket.connect('tcp://'+address+':'+port)
            print( 'Successfully connected to %s' % address + ':' + port )

    # listen at the given ports until the specified number of
    # messages is received for further processing.
    messages = []

    # This part is necessary for a subscriber, otherwise it won't function.
    author = '127.0.0.1'
    socket.setsockopt_string(zmq.SUBSCRIBE, author)

    while len(messages) < message_limit:
        print('receiving...')
        message = socket.recv()
        
        # assert message is the correct format,
        # or parse it here:
        # so far it is [ contractor_address /// source_code ]
        message = str(message)
        message = message.split( delimiter )
        try:
            assert len(message) == 2
            message[0] = message[0].lstrip().rstrip()[2:] # to get rid of b'
            message[1] = message[1].lstrip().rstrip()[:-1] # to get rid of last '
            messages.append(message)
        except:
            pass

        print( 'Received message %s at time ' % message, str(int(time.time())))
        time.sleep( frequency )
        messages.append(message)

    print( messages )
    return messages


source_listener()
