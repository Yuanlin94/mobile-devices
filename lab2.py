import hashlib
 
def hash_string1(string):

	 return hashlib.sha1(string.encode()).hexdigest() 
def check_string1(hashed_string, user_string):

     return hashed_string == hashlib.sha1(user_string.encode()).hexdigest()
 
def hash_string256(string):
    
    return hashlib.sha256(string.encode()).hexdigest() 

def check_string256(hashed_string, user_string):
 
    return hashed_string == hashlib.sha256(user_string.encode()).hexdigest()

def hash_string512(string):

	 return hashlib.sha512(string.encode()).hexdigest() 
def check_string512(hashed_string, user_string):

     return hashed_string == hashlib.sha512(user_string.encode()).hexdigest()




 
new_string = input('Please enter a string: ')
hashed_string1 = hash_string1(new_string)
hashed_string256 = hash_string256(new_string)
hashed_string512 = hash_string512(new_string)

print('The string to store with SHA-1: ' + hashed_string1)
print('The string to store with SHA-256: ' + hashed_string256)
print('The string to store with SHA-512: ' + hashed_string512)

old_string = input('Now please enter the string again to check: ')
if check_string1(hashed_string1, old_string):
    print('The hash codes by SHA-1 match.')
else:
    print('The hash codes by SHA-1 do not match.')
if check_string256(hashed_string256, old_string):
    print('The hash codes by SHA-256 match.')
else:
    print('The hash codes by SHA-256 do not match.')
if check_string512(hashed_string512, old_string):
    print('The hash codes by SHA-512 match.')
else:
    print('The hash codes by SHA-512 do not match.')