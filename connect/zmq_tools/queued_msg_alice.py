import zmq
import time
import sys


# CLIENT ( connects to port )
# Queued version. For PAIR zmq types, all messages are received.
port = '5556'
try:
    if sys.arg[1]:
        port = sys.argv[1]
except:
    pass
print( 'Port: %s' % port )


context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)


def heart_beat_c( limit = 20, to_print = True ):
    '''
    Connects to server that sends integer, and sends back 
    the message, incremented. Used for connection testing (server counts time)
    
    Options:
    ~~~~~~~~
    limit - sets limit for the integer to send. if set to 0, goes forever
    to_print - prints received message, recommended for finite limits
    '''
    a = 0
    if limit:
        while a <= limit: 
            a = int(socket.recv())
            if to_print:
                print('Received:',a)
            b = str( int(a) + 1 ) # this works even given the 'b' prefix of a
            socket.send_string(b)
    if limit == 0:
        while True: # goes forever, CTRL+C to close
            b = str( int(socket.recv()) +1 )
            socket.send_string(b)


# part 1: check for first contact to server, assuming server is already running

start = time.time() 
first_server_msg = socket.recv()

while type(first_server_msg) == bytes():
    first_server_msg = socket.recv()

print( "Connected to Server" )
socket.send(bytes())

end = time.time()
print( 'Time to connect:', end-start )


# part 2: receive a number of messages and reply to them

heartbeat_c( 1000000, False)

print('Done')



