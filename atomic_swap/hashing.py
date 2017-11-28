import hashlib

# Example secret

# secret needs to be encoded, simple add 'b' before string
secret = b'hello'

sec_hash = hashlib.sha256(secret)
print(sec_hash.digest())

