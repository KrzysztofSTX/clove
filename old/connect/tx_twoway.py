from web3 import Web3, HTTPProvider, IPCProvider
import accounts
import tx_oneway
import time


''' MAP
~~~~~~~~~~~~~~
Sender ----
          V
          Clove account
          on sender chain ----
                             V
                             Clove DB
          V------------------V
          Clove account  
          on receiver chain
    V-----V
Receiver
'''


class twoway_tx:
    # takes information from Clove accounts on both chains,
    # plus one-way transaction info
    
    # transaction formula based on whitepaper
    # scheme: call transaction from sender contract address to Clove account
    # on sender chain, then from Clove account on receiver chain send funds
    # to receiver.
    
    def __init__(self, sender_transaction, receiver_transaction,
                 clove_acc_send, clove_acc_recv,
                 status = 'Incomplete',
                 txid = 0,
                 time_limit = 31536000 ):
        self.sendtx = sender_transaction
        self.recvtx = receiver_transaction
        self.clove_send = clove_acc_send #input is the 'account' class object
        self.clove_recv = clove_acc_recv


    # INFORMATION FUNCTIONS

    # Transaction Info on Sender Chain
    def send_tx(self, to_print=True):
        if to_print:
            print( self.sendtx.rinfo() )
        else:
            return self.sendtx.rinfo()        

    # Transaction Info on Recever Chain
    def recv_tx(self, to_print=True):
        if to_print:
            print( self.recvtx.rinfo() )
        else:
            return self.recvtx.rinfo()
        
    # Clove Account Info on Sender Chain
    def send_info(self, to_print=True):
        if to_print:
            print( self.clove_send.rinfo() )
        else:
            return self.clove_send.rinfo()

    # Clove Account Info on Receiver Chain
    def recv_info(self, to_print=True):
        if to_print:
            print( self.clove_recv.rinfo() )
        else:
            return self.clove_recv.rinfo()



    def verify_addresses(self):
        if self.sendtx.recv_addr == self.clove_send.acct_addr:
            if self.clove_recv.acct_addr == self.recvtx.send_addr:
                return True
            else:
                print( 'Receiver addresses do not match' )
        else:
            print( 'Sender addresses do not match' )
            
    # TODO: verify amounts
    # TODO: additional security measures on Clove side

    # TRANSACTION FUNCTIONS
    # 1. establish web3 object
    # 2. unlock Clove account
    # 3. sign transaction
    # 4. transact
