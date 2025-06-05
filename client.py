import requests
from crypto import encrypt_message

def send_encrypted_message(message, key, receiver_ip):
    encrypted = encrypt_message(message, key)
    response = requests.post(f"http://{receiver_ip}:5000/receive", json={'encrypted_msg': encrypted})
    return response.status_code

# (No longer needed; sending is handled in ui.py for peer-to-peer)
