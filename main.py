import tkinter as tk
import subprocess
import sys
import os
import signal

from ui import SecureMessengerApp
from sms import generate_otp, send_otp_via_sms
from client import send_secure_message_to_peer, read_secure_message_from_local

class SecureMessengerController:
    def __init__(self, root):
        self.root = root
        self.server_process = None
        self.app = SecureMessengerApp(
            root,
            self.send_secure_message,
            self.read_secure_message,
            self.start_server,
            self.stop_server,
            self.on_close
        )

    def start_server(self):
        if self.server_process is None:
            self.server_process = subprocess.Popen([sys.executable, "server.py"])
            self.app.set_server_buttons(True)
            self.app.show_info("Server", "Local server started. Ready to receive messages.")

    def stop_server(self):
        if self.server_process is not None:
            if sys.platform == "win32":
                self.server_process.terminate()
            else:
                os.kill(self.server_process.pid, signal.SIGTERM)
            self.server_process.wait()
            self.server_process = None
            self.app.set_server_buttons(False)
            self.app.show_info("Server", "Local server stopped.")

    def send_secure_message(self):
        message = self.app.get_message()
        phone = self.app.get_phone()
        peer_ip = self.app.get_peer_ip()

        if not message or not phone or not peer_ip:
            self.app.show_error("Error", "Please fill in all fields.")
            return

        otp = generate_otp()
        send_otp_via_sms(phone, otp)

        try:
            status = send_secure_message_to_peer(message, otp, peer_ip)
            if status == 200:
                self.app.show_info("Success", "Encrypted message sent and OTP delivered!")
            else:
                self.app.show_error("Error", f"Failed to send message. Status code: {status}")
        except Exception as e:
            self.app.show_error("Error", f"Failed to send message: {e}")

    def read_secure_message(self):
        otp = self.app.ask_otp()
        if not otp:
            return
        try:
            decrypted_msg = read_secure_message_from_local(otp)
            if decrypted_msg is None:
                self.app.show_error("Error", "No message received yet.")
                return
            self.app.show_info("Decrypted Message", decrypted_msg)
        except Exception as e:
            self.app.show_error("Error", f"Failed to decrypt: {e}")

    def on_close(self):
        self.stop_server()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    controller = SecureMessengerController(root)
    root.mainloop()