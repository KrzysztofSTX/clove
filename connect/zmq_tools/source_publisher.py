import zmq
import time
import sys


if len(sys.argv) > 1:
    source =  sys.argv[1]
if len(sys.argv) == 0:
    print('Please provide contract source code')
    

def source_publisher( source,
                      author_addr = ['127.0.0.1'],
                      send_addresses = ['127.0.0.1'],
                      ports = ['5555'],
                      frequency = 1,
                      publish_time = 600,
                      delimiter = '///',
                      ):
    '''
    Function to publish the contract source from the originator
    to the miners to get compiled into bytecode / ABI.
    Parameters:
    ~~~~~~~~~~~
    source - tsol compiled contract source or a ready contract
    address - of the author
    ports - designated well-known ports for broadcasting source code
    frequency - how often to publish
    publish_time - how long to publish for, 10 minutes default
    delimiter - format for sending author and source as a single string,
        instead of a json file.
    *NOTE: everything except the source should be automated by other functions.
    '''
    send_addresses = get_addresses() #external functions in port manager
    ports = get_ports #same as above, for addresses

    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)

    if type(ports) != list:
        ports = [ports]

    # connect to all IPs and ports
    for port in ports:
        for address in send_addresses:
            if type(port) == int:
                port = str(port)
            zmq_socket.bind('tcp://' + address + ':' + port)
    print('Connected to recipient addresses.')

    message = author_addr + delimiter + source

    start = int( time.time() )
    while int( time.time() ) - start <= publish_time:
        zmg_socket.send_string( message )
        time.sleep( frequency )
    print('Finished publishing source for ',str(publish_time),' seconds.')
