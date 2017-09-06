
from web3 import Web3, HTTPProvider, IPCProvider



# client class checks for proper format types

class client_connection:
    # inputs: 'HTTP' or 'IPC' , and corresponding address if HTTP
    def __init__(self, connection_type, connection_address): # self.c , self.a
        if type(connection_type) == str:
            self.ct = connection_type
        else:
            print('Input connection_type is not a string')
        if connection_type == 'HTTP':
            if type(connection_address) == str:
                self.ca = connection_address
            else:
                print('Input address is not a string')
        if connection_type == 'IPC':
            self.ca = None
        else:
            print('Input connection_type is not "HTTP" or "IPC"')



# Create Web3 object for an individual address, HTTP or IPC

def connect_http(address):
    web3 = Web3(HTTPProvider(address))
    return web3

def connect_ipc():
    web3 = Web3(IPCProvider())
    return web3

def check_address(chain_address):
    return web3.isAddress( chain_address )



# Convenience function for taking two addresses

def client2web3(client1, client2):
    
    # creates a tuple of two web3 objects
    # types are either 'HTTP' or 'IPC' and address is HTTP address in case it exists.

    if client1.ct == 'HTTP':
        c1 = connect_http( client1.ca )
    elif client1.ct == 'IPC':
        c1 = connect_ipc( client1.ca )

    if client2.ct == 'HTTP':
        c2 = connect_http( client2.ca )
    elif client2.ct == 'IPC':
        c2 = connect_ipc( client2.ca )

    return (c1,c2) 

        




