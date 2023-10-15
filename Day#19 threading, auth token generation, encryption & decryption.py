#threading:
print("")
print("Threading:")

import threading
def sample1(num):
    print(f"h1 is {num}")

def sample2(name):
    print(f"my name is {name}")

t1=threading.Thread(target=sample1,args=(9,))
t2=threading.Thread(target=sample2,args=("Kumar",))

print("")
t1.start()
print("")
t2.start()
print("")

#authentication token generation:
print("Authentication Token Generation:")
from uuid import uuid4 #uuid--> universal unique identifier
rand_token=uuid4()
print(f"Token->{rand_token}")
print("")

#python encryption and decryption:
#encryption:
print("Encryption: ")
from cryptography.fernet import Fernet
password="1234"
key=Fernet.generate_key()
fernet=Fernet(key)
enc_password=fernet.encrypt(password.encode())
print(enc_password)
print("")

#decryption:
print("Decryption:")
dec_password=fernet.decrypt(enc_password).decode()
print(f"Original Password-> {dec_password}")