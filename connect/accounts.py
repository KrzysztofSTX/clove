from web3 import Web3, HTTPProvider, IPCProvider

'''
Class Methods
~~~~~~~~~~~~~
-account
    -initialize(account_name, password, chain_addr, balance, transactions
               chain_name=None, status = 'nonexistent', relations = [])
    -info
    -lock
    -unlock(duration)
    -show_rel
    -add_rel(others)
    
Helper Functions
~~~~~~~~~~~~~~~~
1. new_account( password, chain_addr, account_name='Default', chain_name=None )
2. unlock_acct( account_addr, password, chain_addr, duration=1 )
3. lock_acct( account_addr, chain_addr )

Example Usage
~~~~~~~~~~~~~
sender_http = '216.3.128.10'
receiver_http = '216.3.128.11'

send = Web3(HTTPProvider( sender_http )) # web3 object for sender
recv = Web3(HTTPProvider( receiver_http )) # web3 object for receiver
'''

# create middle account

def new_account( password,  chain_addr,
                 account_name='Default',chain_name=None ):
    # create new account on a chain, specify name for recognition
    # address encrypted with password, STORE SAFELY!
    try:
        connect = Web3(HTTPProvider( chain_addr ))
    except:
        print( 'Connection Error' )
        return None
    encrypted_addr = connect.personal.newAccount( password )
    
    print( 'New Account Details:\n--------------------\n',
           'Account Name', account_name,
           'Account Address:', encrypted_addr,
           'Password:', password, # optionally remove
           'Chain Name:', chain_name,
           'Chain Address:', chain_addr)
    
    return {'Account Name', account_name,
           'Account Address:', encrypted_addr,
           'Chain Name:', chain_name,
           'Chain Address:', chain_addr)

           
def unlock_acct( account_addr, password, chain_addr, duration=1 ):
    # set duration to None to remain unlocked indefinitely
    try:
        connect = Web3(HTTPProvider( chain_addr ))
    except:
        print( 'Connection Error' )
        return None
    status = connct.personal.unlockAccount( account_addr,
                                   password)
    if status:
        print( 'Account Unlocked' )
    else:
        print( 'Incorrect Password or Address' )
    return status

    
def lock_acct( account_addr, chain_addr ):
    try:
        connect = Web3(HTTPProvider( chain_addr ))
    except:
        print( 'Connection Error' )
        return None
    connect.lockAccount( account_addr )
    return True
    

class account:
    def __init__(self,
               account_name, password, chain_addr,
               balance, transactions
               chain_name=None, status = 'nonexistent',
               relations = []):
        self.status = status
        if status == 'nonexistent':
            initial = new_account( password,  chain_addr,
                         account_name=account_name, chain_name=chain_name )
            self.status = 'Locked'
        
            self.acct_name = initial[ 'Account Name' ]
            self.acct_addr = initial[ 'Account Address' ]
            self.password = password # optionally remove
            self.chain_addr = initial[ 'Chain Address']
            self.chain_name = initial[ 'Chain Name' ]

            print( 'Account', self.acct_name,
                   'with address', self.acct_addr,
                   'has been created')
        else:
            self.status = status
            self.acct_name = account_name
            self.acct_addr = None
            self.password = password
            self.chain_addr = chain_addr
            self.chain_name = chain_name

        # List of related accounts addresses, for convenience in many TX's
        self.relations = relations 
        if self.acct_addr not in relations:
            self.relations.append( self.acct_addr )

    def info(self):
        print('Account Name:', self.acct_name,
              'Account Address:', self.acct_addr,
              'Status:', self.status,
              'Chain Name:', self.chain_name,
              'Chain Address:', self.chain_addr,
              'Number of related accounts:', len( self.relations ))
              
              

    def lock(self):
        status = lock_acct( self.acct_addr, self.chain_addr )
        if status:
            self.status = 'Locked'
            print( self.status )

    def unlock(self, duration=360):
        status = unlock_acct( self.acct_addr, self.password,
                     self.chain_addr, duration )
        if status:
            self.status = 'Unlocked'
            print( self.status )

    # Show accounts functionally related to this one
    def show_rel(self):
        print( 'Number of related accounts:', len( self.relations ))
        return self.relations

    # Add related account address to the 
    def add_rel(self, others):
        if type(others) == list:
            self.relations += others
        elif type(others) == str:
            self.relations.append(others)
        else:
            print( 'Input needs to be a List of Strings, or a single String' )
            
        






