"""
Text file encryption: -
    1. It's better to work with binary data for encryption.
"""


from cryptography.fernet import Fernet
import string
import random
import time
from datetime import datetime

class CipherPol(object):
    def __init__(self):
        self.data_file = None
        self.data = None
        self.key = None
        self.key_file = None
        self.cipher_instance = None

    def set_cipher_instance(self):
        self.cipher_instance = Fernet(self.key)
    def set_data_file(self):
        self.data_file = input("File: ")

    def set_data(self):
        with open(self.data_file, 'r') as f:
            self.data = f.read()

    def random_name(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(10))

    def random_file(self):
        timestamp = time.time()
        formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%d %m %Y %H %M %S')
        return 'Key ' + formatted_timestamp + self.random_name() + ' .txt'

class Agency_Encryption(CipherPol):
    def __init__(self):
        super().__init__()

    def set_key(self):
        self.key = Fernet.generate_key()

    def store_key(self):
        # get a valid file name to store key in it.
        while True:
            try:
                # create the file
                self.key_file = self.random_file()
                # finally, store the key in obtained valid file.
                # since, key itself is binary, therefore open file in binary mode.
                # A new key_file is created for every encryption operation
                with open(self.key_file, 'wb') as f:
                    f.write(self.key)
                break
            except FileExistsError as e:
                pass

    # final act
    def encrypt_data(self):
        # convert the data into byte
        byte_data = self.data.encode('utf-8')
        # encrypt the data to encrypt it, as in Fernet cryptography works on byte data only.
        cipher_data = self.cipher_instance.encrypt(byte_data).decode('utf-8')
        with open(self.data_file, 'w') as f:
            f.write(cipher_data)


class Agency_Decryption(CipherPol):
    def __init__(self):
        super().__init__()

    def set_key_file(self):
        self.key_file = input("Key File: ")

    def set_key(self):
        with open(self.key_file, 'rb') as f:
            self.key = f.read()

    def decrypt_data(self):
        # data to be decrypted must be encoded not a string.
        deciphered_data = self.cipher_instance.decrypt(self.data.encode('utf-8')).decode('utf-8')
        with open(self.data_file, 'w') as f:
            f.write(deciphered_data)


def main():
    print("MENU:")
    print("1. Encryption")
    print("2. Decryption")

    choice = int(input("Choice: "))
    if choice == 1 or choice == 2:
        if choice == 1:
            agent_cipher = Agency_Encryption()
            agent_cipher.set_data_file()
            agent_cipher.set_data()
            agent_cipher.set_key()
            agent_cipher.store_key()
            agent_cipher.set_cipher_instance()
            agent_cipher.encrypt_data() # final act
            print(f"File: {agent_cipher.data_file} encrypted successfully!")
            print(f"Key: {agent_cipher.key_file}")
        elif choice == 2:
            agent_decipher = Agency_Decryption()
            agent_decipher.set_data_file()
            agent_decipher.set_data()
            agent_decipher.set_key_file()
            agent_decipher.set_key()
            agent_decipher.set_cipher_instance()
            agent_decipher.decrypt_data()
            print(f"File: {agent_decipher.data_file} decrypted successfully!")
    else:
        print("Exit")


main()
