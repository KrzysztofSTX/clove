# ALL INCLUSIVE MINER MODULE
# UNDER CONSTRUCTION


import zmq
import time
import sys
from  multiprocessing import Process


class miner_log:
    def __init__(self,
                 contractor,
                 miner_info,
                 router,
                 ):
        # Contractors includes Bob's address, source, and 
        # a dictionary of votes for different bytecode variations
        # of Bob's contract. [dictionary of # miners agreeing,
        # their bytecode, and addresses]
        self.conractor = contractor

        # miner_info includes the general information of the
        # mining situation, so the ports at which to listen for
        # source code and the ports at which to publish bytecode.

        # ********************************************
        # CONTRACTORS NEEDS TO BE INITIALIZED FIRST
        # SO THAT MINERS CAN FILTER INCOMING MESSAGES
        # ********************************************
        self.miner_info = miner_info

        self.router = router


    class contractor:
        def __init__(self,
                     address,
                     source,
                     consensus_status,
                     limit = 10
                     ):
            self.address = ''
            self.source = ''
            # IDEA: instead of repeating miner data for consensus
            # status, keep a matrix that shows the same info.
            self.consensus_status = consensus_status
            # establish a limit for the number of contractors to
            # keep track of:
            self.limit = limit
            
        def change_limit(self,new_limit):
            self.limit = new_limit
            
        def get_addresses():
            '''
            '''
            pass
        def get_sources():
            '''
            '''
            pass
        def get_consensus_status():
            '''
            '''
            pass
        def compile_contract(self, source):
            assert type(source) == str
            '''
            import [path to solc compile module]
            '''
            bytecode = '0x' # object placeholder
            self.bytecode = bytecode
            
        
            
         

    class miner_info:
        def __init__(self,
                     meta_info,
                     source_ports,
                     pull_ports,
                     push_ports,
                     ):
            # meta_info is a port established for getting info
            # regarding all other types of ports, and future
            # changes in iteself.
            self.meta_info = '5555'
        
            # source_ports are for listening for new source code
            self.source_ports = []

            # pull_ports are for receiving other miners' bytecode
            # and consensus info.
            # Requires for the contractor info to be instantiated
            # as messages at a port are filtered per individual
            # contract.
            self.pull_ports = []

            self.push_ports = []

        def find_peer():
            '''
            Preliminary function for discovering new peers before
            their information is added.
            '''
            pass

        def change_meta_port():
            '''
            '''
            pass           

        def get_source_ports():
            '''
            '''
            pass

        def get_pull_ports():
            '''
            '''
            pass

        def get_push_ports():
            '''
            '''
            pass

    def miner_poll():
        '''
        Polls messages to establish consensus
        '''
        pass
    


    class router:
        '''
        Sends out various types of information to peers.
        Instantiated so that miners can be self-reliant without
        the need for a server-based queue, forwarding, or
        streamer systems.
        miner_log.publisher performs this function because once
        miner_log connects to contractors, compiles contract into
        bytecode, and checks the current state
        '''
        def __init__(self):
            pass


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

    
    def update_consensus( current_log,
                      past_log,
                      ports = ['5556'],
                      ):
    '''
    current_log is the information miners provide for distribution,
    and past_log is the info on the current consensus state.

    To check whether a specific miner has contributed, a list of addresses
    is kept for each compilation version. It also keeps a 'voter list' for
    the different compilations.
    
    Works with a file that keeps track of which contract compilations are
    the mostagreed upon based on miners.
    '''
    
    { 'author' : author_addr,
        'source' : author_source,
        'bytecode' : bytecode,
        'abi' : abi,
        'miner' : ip_ addr, # miner address used to 'sign' a compilation
        'consensus': {
            'compilation_variation' : [ ], #list of supporting miner addresses
            'miner_addresses' : [ ], # list of addresses of miners agreeing to
                # the above compiled bytecode, in order.
        }
    }
    assert current_log['author'] == past_log['author']
    assert current_log['source'] == past_log['source']

    # TODO: either system to randomize miner recipients,
    # or find a way for small-vote compilations to make it
    # IDEA: reverse snow-ball effect, where a variation gains less popularity
    # the more additional people support it as long as others have a form of
    # verification that makes it legitimate (randomized locations, etc)

    # under construction

def miner_listener(  ports = ['5556'],
                     addresses = ['127.0.0.1'],
                     filters = ['Bob', 'Alice'],
                     recv_message_limit = 10,
                     frequency = 1,
                     broadcast_time = 600
                     ):
    '''
    The format of the messages miners are assumed ot send each other:
    At mining ports, miners push author, source, bytecode, abi, miner,
    and the consensus info is an embedded json file with:
    variations, consensus polls, miner addresses for each variation.
    { 'author' : author_addr,
        'source' : author_source,
        'bytecode' : bytecode,
        'abi' : abi,
        'miner' : ip_ addr, # miner address used to 'sign' a compilation
        'consensus': {
            'compilation_variation' : [ ], #list of supporting miner addresses
        }
    }
    the last entry will be a dictionary of variations. To keep its size limited,
    only the top 5 compilation variations will proceed after a miner processes
    it and broadcasts it forward.
    
    Works in conjunction with the update_consensus function to aggregate
    compilation results.
    Filters are used to filter through the messages at the port for specific
    countract authors.
    '''

    context = zmq.Context()
    miner_receiver = context.socket(zmq.PULL)

    # connect sockt to all ports for listening to
    for addr in addresses: 
        miner_receiver.connect('tcp://' + addr + ':5557')

    # socket for sending the updated file
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")

    messages = []
    while len(messages) <= message_limit
        msg = miner_receiver.recv_json()
        messages.append(msg)

    # process all messages with update_consensus function
    consensus = update_consensus( messages )
    
    start = time.time()
    while int(time.time()) - start <= broadcast_time:
        zmq_socket.send_json( message )
        time.sleep( frequency )
        




