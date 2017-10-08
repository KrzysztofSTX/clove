import zmq
import time

# TODO: process by which to introduce new bytecode variations.
# one solution is to randomly remove one of the established variations,
# which would statistically allow the most agreed upon variation to succeed.


def miner( miner_work = None, # the work that will get incorporated into the consensus
                     my_address = '127.0.0.1', # self or queue device
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
    # TODO: include port changing function,
    # or restart funciton with new port parameter
    # after properly closing the zmq process 
    
    context = zmq.Context()

    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://127.0.0.1:5557")

    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://127.0.0.1:5558")

    #############################################
    my_address = '128.0.0.1' # for example
    # example data
    author = '127.0.0.1'
    author_port = 5556
    author = author + ':' + str(author_port)
    
    source = 'hellllo'
    
    to_publish = { 'bc_variations' : 'v1',
                   'abi_variations' : 'abi1' }
    ##############################################

    start = time.time()                   
    while tiem.time() - start <= 600 # 10 minutes for entire mining process
        # filter port for author name
        work = receiver.recv_json()

        # check if this miner's work is present
        # NOTE: in this version the abi and bytecode are attached simultaneously
        
        if author in work.keys():
            if work[ author ] == source:
                # check if this miner's work is in the consensus.
                if to_publish[ 'bc_variations' ] in work['bc_variations']:
                    bc_index = work['bc_variations'].index(
                        to_publish[ 'bc_variations' ] )
                    
                    # check if this miner voted for that bytecode.
                    if my_address in work['votes'][ bc_index ]:
                        pass
                    
                    # it is implied by the existence of the bc / abi variation
                    # that the votes list exists.
                    else:
                        work['votes'].append( my_address )

                # similarly check for the abi variation.
                # NOTE: in this version the votes count for abi and bytecode.
                if to_publish[ 'abi_variations' ] in work['abi_variations']:
                    abi_index = work['abi_variations'].index(
                        to_publish[ 'abi_variations' ] )                   
                    if my_address in work['votes'][ abi_index ]:
                        pass
                    else:
                        work['votes'].append( my_address )
                        
                else:
                    work['bc_variations'].append( to_publish[ 'bc_variations' ] )
                    work['abi_variations'].append( to_publish[ 'abi_variations' ] )
                    work['votes'].append( [my_address] )
                    # TODO: control size of variations list to be sent,
                    # including how to judge popuarity of new bytecode options
                    # [ possibly use reverse exponential popularity gain method]           
            else:
                pass
        else:
            pass


        # TODO: check if bytecode can be different but ABI the same

        # publish for 1 minute after having received and checked the consensus file.
        scondary_start = time.time()
        while time.time() - secondary_start <= 60:
            
            sender.send_json(result)
            time.sleep(0.05)

        time.sleep(0.5)
    print('done mining')

miner()
