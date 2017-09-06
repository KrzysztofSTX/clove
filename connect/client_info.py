from web3 import Web3
from . import connection_tools

# Client information class

class client:
    def __init__(self, client_type,
                 connection_type, connection_address,
                 send_address = None, receive_address = None,
                 amount = 0, token_contract_address = None):
        if client_type in ['sender', 'receiver']:
            self.type = client_type
        else:
            print('Incorrect input client type')

        # The following are to be checked in the client_connection class
        self.ct = connection_type
        self.ca = connection_address
        
        if web3.isAddress( send_address ):
            self.send = send_address
        if web3.isAddress( receive_address ):
            self.receive = receive_address

        if type(amount) == int: #TODO: create separate client/transaction class
            self.amount = amount
        if type(token_contract_address) == str:
            self.tca = token_contract_address
        


        
class transaction:

    # write in RECEIVER, SENDER order (can be fixed for arbitrary order)
    # receiver reffers to first client in transaction example of whitepaper
    
    def verify_status( obj, obj_it_should_be ):
        return obj == obj_it_should_be
    
    def __init__(self,client1,client2): 
        if verify_status( client1.type, 'receiver' ) and
            verify_status( client2.type, 'sender' ):
            pass
        else:
            print('Incorrect client order')
            break
        self.rec_send_address = client1.send
        self.rec_rec_address = client1.receive
        self.rec_amt = client1.amount
        self.rec_tca = client1.tca

        self.rec_send_address = client2.send
        self.rec_amt = client2.amount
        self.rec_tca = client2.tca

        #TODO: verifiy two amounts along with transaction costs are compatible

        
        
        
        
        
