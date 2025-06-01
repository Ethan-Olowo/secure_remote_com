from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(message):
    return message + (16 - len(message) % 16) * ' '

def encrypt_message(message, key):
    key = key[:32].ljust(32).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message, key):
    key = key[:32].ljust(32).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message.encode()))
    return decrypted.decode().strip()