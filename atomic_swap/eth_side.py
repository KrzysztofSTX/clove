from web3 import Web3, IPCProvider, contract, HHTPProvider
import time


# Ethereum Side


'''
Atomic swap contracts

Bob side
~~~~~~~~~
1. wants to send B bitcoin to Alice's wallet
2. creates secret S, sends its hash to Alice
3. Sends B to his contract which will execute if he withdraws Alice's contract

Alice side
~~~~~~~~~~~
1. wants to send A alicecoin to Bob's wallet on her chain
2. creates a contract knowing the hash of Bob's secret
3. Sends A to her contract, which will send funds when the secret hash matches
    the one given by Bob

'''



# Local Geth Chain Setup for Example
# For this example assume Bob is running the chain

web3 = Web3(IPCProvider()) # web3 is just the object name here, can be Bob or Alice
web3.personal.newAccount('password') # enter password

web3.miner.start(1)

add0 = web3.personal.listAccounts[0] 

# Bob unlocks his account 
web3.personal.unlockAccount( add0,'password_0')
web3.miner.start(1)




# TRANSACTION

B = 808 # tokens from Bob


eth_bob = '0xe5e57a4069ad2847f7968872fd0bb6e3d0bdf6b1'
eth_alice = '0xb1716e1c4aeeb3bec250e3ebc8d5f2d19defd717'


# TODO: Replace with RPC
chain_1_ip = '255.140.22.1'
# chain_2_ip = '255.141.22.1' # Later for BTC


# connect to chain

# Web3 objects
eth_bob = Web3(HTTPProvider( chain_1_ip )) 
eth_alice = Web3(HTTPProvider( chain_1_ip ))




# get balance of each account
balance_bob = web3.eth.getBalance( eth_bob )
print( 'Bob Account balance:', balance_bob )


# Alice can do the same on her wallet
balance_alice = web3.eth.getBalance( eth_alice )
print( 'Bob Account balance:', balance_alice )




# transaction 1: Bob -> Alice on ethereum
bob2alice = {'from': eth_bob,
       'to' : eth_alice
       'value': B,
       }

gastimate = web3.eth.estimateGas( bob2alice )

if balance_0 <= gastimate:
    print( 'Not enough ETH to cover gas cost' )
    web3.miner.start(1)


bob2alice = web3.eth.sendTransaction( bob2alice )

# Wait to receive transaction verification
wait = 0
while clove_bob.eth.getTransactionReceipt( bob2alice ) == None:
    print( 'Waiting for Bob 2 Clove transaction to mine' + wait * '.' )
    wait += 1
    time.sleep(1)


print( 'Transaction mined!' )
print( 'Account balances:\n', web3.eth.getBalance( eth_bob ) )
    
print( 'Receipt:\n', web3.eth.getTransactionReceipt( a ))



a = eth_alice.eth.sendTransaction( bob2alice ) # Alice checks
b = eth_bob.eth.sendTransaction( bob2alice ) # Bob checks


print( 'Bob Receipt:\n', b )
print( 'Alice Receipt:\n', a )
