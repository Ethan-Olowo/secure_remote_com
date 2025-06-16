from crypto import encrypt_message, decrypt_message
import requests

def send_secure_message_to_peer(message, otp, peer_ip):
    encrypted = encrypt_message(message, otp)
    response = requests.post(f"http://{peer_ip}:5000/receive", json={'encrypted_msg': encrypted})
    return response.status_code

def read_secure_message_from_local(otp):
    response = requests.get("http://127.0.0.1:5000/get_message")
    encrypted_msg = response.json().get('encrypted_msg', '')
    if not encrypted_msg:
        return None
    return decrypt_message(encrypted_msg, otp)
