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




