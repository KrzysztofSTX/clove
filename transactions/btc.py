from op_codes import *

from bitcoin import base58
import secrets
from datetime import datetime, timedelta, time

def push_data(d):
	return hex(len(d))[2:]

def address_to_raw_tx_data(a):
	assert len(a) == 34
	a_hex = base58.decode(a).hex()
	return push_data(a_hex) + a_hex

def atomic_swap(secret_hash, bob_address, alice_address):
	# set the expiration one day 
	timelock = hex(int((datetime.now() + timedelta(hours=24)).timestamp()))[2:]
	timelock_raw_tx_data = push_data(timelock) + timelock

	push_secret_hash = hex(len(secret))[2:]
	secret_raw_tx_data = push_secret_hash + secret

	return "".join([OP_IF,
			OP_RIPEMD160,
			secret_raw_tx_data,
			OP_EQUALVERIFY,
			OP_DUP,
			OP_HASH160,
			address_to_raw_tx_data(bob_address),
			OP_ELSE,
			timelock_raw_tx_data,
			OP_CHECKLOCKTIMEVERIFY,
			OP_DROP,
			OP_DUP,
			OP_HASH160,
			address_to_raw_tx_data(bob_address),
			OP_ENDIF])

def redeem(signature, pub_key, secret, contract):
	return Script.compile('{} {} {} {} {} {} OP_1 {} {}'.format(
		push_data(signature),
		signature,
		push_data(pub_key),
		pub_key,
		push_data(secret),
		secret,
		push_data(contract),
		contract
	))

alice = '16UFUyyQ5qxkiSFhsGVrAPKDyjUr5u4MRv'
bob = '18LhCMLzDbh1c5xp2zgLH2WWcmvchMgCEV'
secret = secrets.token_hex(8)

print(atomic_swap(secret, bob, alice))