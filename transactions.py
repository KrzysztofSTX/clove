from op_codes import *

def atomic_swap(hashed_secret, bob_pub_key_hash, timelock, alice_pub_key_hash):
	pass
	
script = "".join([OP_IF,
OP_RIPEMD160,
'xx', # push data
'xx', # data
OP_EQUALVERIFY,
OP_DUP,
OP_HASH160,
'xx',
'xx',
OP_ELSE,
'xx',
'xx',
OP_CHECKLOCKTIMEVERIFY,
OP_DROP,
OP_DUP,
OP_HASH160,
'xx',
'xx',
OP_ENDIF])

print(script)