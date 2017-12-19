def atomic_swap(hashed_secret, bob_pub_key_hash, timelock, alice_pub_key_hash):
	return Script.compile('OP_IF OP_RIPEMD160 {} OP_EQUALVERIFY OP_DUP OP_HASH160 {} ' \
	'OP_ELSE {} OP_CHECKLOCKTIMEVERIFY OP_DROP OP_DUP OP_HASH160 {} OP_ENDIF ' \
	'OP_EQUALVERIFY OP_CHECKSIG'.format(hashed_secret, bob_pub_key_hash, timelock, alice_pub_key_hash))

from op_codes import *

script = OP_IF + OP_RIPEMD160

print(script)