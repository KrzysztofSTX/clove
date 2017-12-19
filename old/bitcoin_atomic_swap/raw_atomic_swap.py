'''UNDER DEVELOPMENT'''

# Raw Atomic Swap

'''~~~~~~~~~PSEUDO CODE FOR ATOMIC SWAP
Bob side
~~~~~~~~
IF
  <Alice PubKey> HASH160 <Bob's Secret>
ELSE
  <Wait N time>
ENDIF

Alice side # COMING SOON
~~~~~~~~~~
IF
  <Bob PubKey> # releases Bob's secret
ELSE
  <Wait M time>
ENDIF



Bitcoin OP_CODE version:
~~~~~~~~~~~~~~~~~~~~~~~~
OP_IF
OP_RIPEMD160
<Bob's secret hash>
OP_EQUALVERIFY
OP_DUP
OP_HASH160
<Alice pubKey>
OP_ELSE
<locktime> # >5e8 is Unix time, else block number
OP_CHECKLOCKTIMEVERIFY
OP_DROP
OP_DUP
OP_HASH160
<Bob's PubKey>
OP_ENDIF
OP_EQUALVERIFY
OP_CHECKSIG


in hex:
~~~~~~~
0x63
0xa6
<Bob's secret hash>
0x88
0x76
0xa9
<Alice PubKey>
0x67
<locktime>
0xb1
0x75
0x76
0xa9
<Bob PubKey>
0x68
0x88
0xac
'''

def raw_atomic_swap(address1, address2, locktime, secret_hash):
	'''
	Generates raw transaction string for an atomic swap on the bitcoin blockchain.
	Assumptions:
	~~~~~~~~~~~~
	Based on the scheme, address1 is that of Bob and address2 is that of Alice.
	'''
	contract = str(0x63)+str(0xa6)
	#TODO: RIPEMD160 method
	contract += secret_hash
	contract += str(0x88)+str(0x76)+str(0xa9)
	#TODO: conversion methods for addresses
	contract += address2
	contract += str(0x67)
	#TODO: assert proper format for nLockTime 
	contract += locktime
	contract += str(0xb1)+str(0x75)+str(0x76)+str(0xa9)
	contract += address1
	contract += str(0x68)+str(0x88)+str(0xac)
	return contract
