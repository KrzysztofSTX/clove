import zmq
import time
import sys


# SERVER ( binds to port )
# Queued version. For PAIR zmq types, all messages are received.
_limit = 1000000
port = '5556'
try:
    if sys.arg[1]:
        port = sys.argv[1]
except:
    pass
print( 'Port: %s' % port )


context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)


def heart_beat_s( limit = 20, to_print = True):
    '''
    Server side of heart beat test. Initializes and sends an integer, awaiting
    the client to send an inremented reply.
    limit - number of messages to send
    '''
    beat = 1
    heart_beat = str( beat )

    received_next = False

    socket.send_string( heart_beat ) # this happens only once

    while beat <= limit: 

        # In this scenario the received message is guaranteed to 
        # be higher than the previous heart beat.
        a = int(socket.recv())
        if to_print:
            print( 'Received:', a )
            
        beat += 2
        heart_beat = str( beat )
        socket.send_string( heart_beat )


# part 1 - start broadcasting to future client

client_connected = False

while not client_connected:
    
    socket.send(bytes())
    first_client_msg = socket.recv()
    
    if first_client_msg == bytes():
        client_connected = True
        print( 'Connected to Alice' )
        break
    else:
        pass


# part 2 - connection time test

start = time.time()

heart_beat_s( 1000000, False):

end = time.time()
print('Time Elapsed for %s messages:' % _limit, end - start)


