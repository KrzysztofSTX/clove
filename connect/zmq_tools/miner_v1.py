import zmq
import time


def miner_1( ip_addr = '127.0.0.1', # self or queue device
                     mine_ports = ['5556'],
                     frequency = 1,
                     port_update_frequency = 5, # seconds to wait before checking
                         # whether to update the port
                     time_active = 600
                     ):
    '''
    The miner generates their own variation of the bytecode before adding it
    to the consensus file which includes the top 10 variations and the
    corresponding number of miners that agree with 

    Individual Miner's contribution:
    set of contracts, organized by author & source (later on add contract #,
    since an author may want to execute the same contract multiple times even
    for the same recipients)

    Once miner adds their contribution to an author/contract pair, they only
    need to help propagate the data until it is received back by the client,
    aka reached_consensus = True.

    This can be organized by only propagating information at certain ports,
    while keeping track of what each miner has accomplished in a personal
    hash table that says which ports to connect to for processing and which
    to connect to for just porpagating data.

    Keeps track of how many times the file has been viewed by multiple miners,
    as a form of duration mechanism.
    '''
    
    individual = { 'author':'127.0.0.1',
             'author_source':'''hello''',
             'bytecode':'0x1234',
             'abi':['abi_here'],
                   }
    consensus = { 'author':'127.0.0.1',
                  'author_source':'''hello''',
                  'variations':{
                      'bytecode':{
                          'votes':0,
                          'miners':[],
                          },
                      },
                  }
    individual_hash = {'author':'source'}
    
    bytecode = '0x5555'
    if bytecode in consensus['variations'].keys() :
        consensus['variations'][ bytecode ]['votes'] += 1

    # Ideally, miners would connect to each other's IP addresses
    # but for demonstration, use 2 ports to signify 2 different destinations.
    recv_port = '5556'
    send_port = '5558'
    
    context = zmq.Context()
    pull_socket = context.socket(zmq.PULL)
    pull_socket.connect('tcp://' + ip + ':' + recv_port)

    push_socket = context.socket(zmq.PUSH)
    push_socket.connect('tcp://' + ip + ':' + send_port)

    start = time.time()
    a = start
    while a - start <= time_active :
        consensus_recv = pull_socket.recv()

        # Check if miner contributed to the contracts in the consensus file.
        for author in individual_hash.keys():
            source = individual_hash['author']
            if author in consensus['author'].keys():
                if source in consensus['author_source'].keys():
                    pass
                else:
                    # TODO: function to update consensus
                    update_consensus( (author,source),consensus)
        push_socket.send_json( consensus )
        a = time.time()
