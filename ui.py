import tkinter as tk
from tkinter import simpledialog, messagebox
from crypto import encrypt_message, decrypt_message
from sms import generate_otp, send_otp_via_sms
from client import send_encrypted_message
import requests
import multiprocessing
import subprocess
import sys
import os
import signal

class SecureMessengerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Messenger")

        self.server_process = None

        self.message_label = tk.Label(root, text="Enter Message")
        self.message_label.pack()
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack()

        self.phone_label = tk.Label(root, text="Receiver Phone Number")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack()

        self.receiver_ip_label = tk.Label(root, text="Receiver IP")
        self.receiver_ip_label.pack()
        self.receiver_ip_entry = tk.Entry(root, width=30)
        self.receiver_ip_entry.pack()

        self.send_button = tk.Button(root, text="Send Secure Message", command=self.send_secure_message)
        self.send_button.pack(pady=10)

        self.read_button = tk.Button(root, text="Read Received Message", command=self.read_secure_message)
        self.read_button.pack(pady=10)

        self.server_start_button = tk.Button(root, text="Start Server", command=self.start_server)
        self.server_start_button.pack(pady=5)

        self.server_stop_button = tk.Button(root, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        self.server_stop_button.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_server(self):
        if self.server_process is None:
            # Start server.py as a subprocess
            self.server_process = subprocess.Popen([sys.executable, "server.py"])
            self.server_start_button.config(state=tk.DISABLED)
            self.server_stop_button.config(state=tk.NORMAL)
            messagebox.showinfo("Server", "Server started.")

    def stop_server(self):
        if self.server_process is not None:
            if sys.platform == "win32":
                self.server_process.terminate()
            else:
                os.kill(self.server_process.pid, signal.SIGTERM)
            self.server_process.wait()
            self.server_process = None
            self.server_start_button.config(state=tk.NORMAL)
            self.server_stop_button.config(state=tk.DISABLED)
            messagebox.showinfo("Server", "Server stopped.")

    def send_secure_message(self):
        message = self.message_entry.get()
        phone = self.phone_entry.get()
        receiver_ip = self.receiver_ip_entry.get()

        otp = generate_otp()
        send_otp_via_sms(phone, otp)

        status = send_encrypted_message(message, otp, receiver_ip)
        if status == 200:
            messagebox.showinfo("Success", "Encrypted message sent and OTP delivered!")
        else:
            messagebox.showerror("Error", "Failed to send message.")

    def read_secure_message(self):
        otp = simpledialog.askstring("OTP Required", "Enter OTP received via SMS")
        receiver_ip = self.receiver_ip_entry.get()
        try:
            response = requests.get(f"http://{receiver_ip}:5000/get_message")
            encrypted_msg = response.json()['encrypted_msg']
            decrypted_msg = decrypt_message(encrypted_msg, otp)
            messagebox.showinfo("Decrypted Message", decrypted_msg)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt: {e}")

    def on_close(self):
        self.stop_server()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = SecureMessengerApp(root)
    root.mainloop()