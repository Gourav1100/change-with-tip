import os
from cryptography.fernet import Fernet

# initialising fernet
key = os.environ.get("FERNET_KEY")
fernet = Fernet(key)



# Functions to encrypt and decrypt the tips given by user
def encrypt_tip(data):
    return fernet.encrypt(data.encode())

def decrypt_tip(data):
    return fernet.decrypt(data).decode()


def checkdata(data):
    if data:
        return True
    return False       