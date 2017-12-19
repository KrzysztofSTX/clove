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

btc_nodes = ['https://insight.bitpay.com/tx/send',
			'https://blockchain.info/pushtx',
			'https://blockexplorer.com/tx/send',
			'https://btc.com/tools/tx/publish',
			'https://coinb.in/#broadcast',
			'https://chain.localbitcoins.com/tx/send',
			'http://webbtc.com/relay_tx',
			'https://www.smartbit.com.au/txs/pushtx',
			'https://live.blockcypher.com/btc/pushtx/',
			'https://pool.viabtc.com/tools/BTC/broadcast/',
			'https://chainquery.com/bitcoin-api/sendrawtransaction']

bcc_nodes = ['https://bcc.zupago.pe/tx/send',
			'https://bitcoincash.blockexplorer.com/tx/send',
			'https://blockdozer.com/insight/tx/send',
			'https://bch-insight.bitpay.com/tx/send']

dash_nodes = ['http://insight.masternode.io:3000/tx/send',
				'https://insight.dash.org/insight/tx/send',
				'https://live.blockcypher.com/dash/pushtx/',
				'https://insight.dash.siampm.com/tx/send']

ltc_nodes = ['https://live.blockcypher.com/ltc/pushtx/',
			'https://insight.litecore.io/tx/send']

zcash_nodes = ['https://zcash.blockexplorer.com/tx/send']

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