import hashlib
import os
import time

Alice = input("Alice Message: ")
time.sleep(2)
os.system("clear")

# Compute the SHA-256 hash of the message
hash_object = hashlib.sha256(Alice.encode())
Alice_hash = hash_object.hexdigest()

# Alice sends the message and the hash to Bob
print("Alice message:", Alice)
print("Alice hash: ", Alice_hash)
time.sleep(2)
os.system("clear")

# Bob receives the message and the hash
received_message = input("Received message: ")
received_hash = Alice_hash

# Compute the SHA-256 hash of the received message
hash_object = hashlib.sha256(received_message.encode())
computed_hash = hash_object.hexdigest()

# Verify
if computed_hash == received_hash:
    print("Not tampered")
else:
    print("Tampered")
