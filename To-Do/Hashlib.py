import hashlib # Encrypts password (SHA-256 hashing)
import secrets # Generates secure random numbers (salting method)
import re 

string = "Hello World"
encoded_bytes = string.encode('utf-8')
print(encoded_bytes)

# The b prefix indicates that the variable encoded_bytes now holds a bytes object
# After encoded, we have to hash the bytes
hash_object = hashlib.sha256(encoded_bytes)
hex_digest = hash_object.hexdigest()
# print(hex_digest)

# Salt
salt = secrets.token_hex(32)
pwd_hash = hashlib.sha256((string + salt).encode()).hexdigest()
print(pwd_hash)