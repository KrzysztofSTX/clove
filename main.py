import ecdsa

tx_hash = '3f285f083de7c0acabd9f106a43ec42687ab0bebe2e6f0d529db696794540fea'

def chunk(l, n):
	return [l[i:i + n] for i in range(0, len(l), n)]

def reverse_bytes(b):
	b = chunk(b, 2)
	b = list(reversed(b))
	return "".join(b)

def left_pad(s, n):
	while len(s) < n:
		s = '0' + s
	return s

def btc_to_bytes(btc):
	btc *= 100000000
	return hex(int(btc))[2:]

def float_to_bytes(f, d):
	f *= 10**d
	return hex(int(f))[2:]

def raw_transaction(tx_hash, value):
	version = '01000000'
	input_count = '01'

	previous_output_index = '00000000'

	sequence = 'ffffffff'

	output_count = '01'

	value = float_to_bytes(value, 8)
	value = left_pad(value, 16)
	value = reverse_bytes(value)
	print(value)

	block_lock_time = '00000000'

raw_transaction(tx_hash, 0.00091234)