import hashlib
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8

print("SHA1:")
hash_object=hashlib.sha1(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

print("SHA256:")
hash_object=hashlib.sha256(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

print("SHA512:")
hash_object=hashlib.sha512(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)



