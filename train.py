# 1. import the Fernet module from cryptography
from cryptography.fernet import Fernet

# 2. Take text to be encrypted
text = "hello hello name is Ajay Gaurav"

# 3. Generate secret key
key = Fernet.generate_key()

"""
4. * Create an instance of Fernet by passing key as argument.
     This will be used to access Fernet encryption and decryption methods.
"""
cipher_pol = Fernet(key)

"""
    5. Convert the data into bytes
    Use - encode(), decode() & specify the type of encoding
"""
data = text.encode("utf-8")

# 6. Encrypt the data
cipher = cipher_pol.encrypt(data)
# cipher = cipher.decode('utf-8')

print(f"Original data = {text}")
print(f"Encrypted data = {cipher}")

# 7. Decrypt the data
original = cipher_pol.decrypt(cipher).decode('utf-8') # decrypted the data and also decoded it since data will be in bytes.
print(f"Decrypted data = {original}")


