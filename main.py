from btcpy.setup import setup
from btcpy.structs.script import Script
setup('regtest')

def atomic_swap(hashed_secret, bob_pub_key_hash, timelock, alice_pub_key_hash):
	return Script.compile('OP_IF OP_RIPEMD160 {} OP_EQUALVERIFY OP_DUP OP_HASH160 {} ' \
	'OP_ELSE {} OP_CHECKLOCKTIMEVERIFY OP_DROP OP_DUP OP_HASH160 {} OP_ENDIF ' \
	'OP_EQUALVERIFY OP_CHECKSIG'.format(hashed_secret, bob_pub_key_hash, timelock, alice_pub_key_hash))

def push_data(d):
	return hex(len(d))[2:]

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

import requests

j = '{rawtx: "135235235235"}'

from bitcoin import base58
import secrets
from datetime import datetime, timedelta, time

alice_address = base58.decode('184TDZtb8Nbq8qnLkvw6nDWtHSrWRubeFW').hex()
bob_address   = base58.decode('19jwLMSXsUSZvW7H49KC94H7Zvkx1DUfuU').hex()
secret        = secrets.token_hex(8)
timelock      = hex(int((datetime.now() + timedelta(hours=24)).timestamp()))[2:]

atomic_swap(secret, bob_address, timelock, alice_address)

print(alice_address)
print(timelock)

print(hex(50))