import tkinter as tk
from tkinter import simpledialog, messagebox
from sms import generate_otp, send_otp_via_sms
from client import send_secure_message_to_peer, read_secure_message_from_local
import requests
import subprocess
import sys
import os
import signal
import threading
import time

class SecureMessengerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Messenger (Peer-to-Peer)")

        self.server_process = None

        self.message_label = tk.Label(root, text="Enter Message")
        self.message_label.pack()
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack()

        self.phone_label = tk.Label(root, text="Receiver Phone Number")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack()

        self.peer_ip_label = tk.Label(root, text="Peer IP (Receiver)")
        self.peer_ip_label.pack()
        self.peer_ip_entry = tk.Entry(root, width=30)
        self.peer_ip_entry.pack()

        self.send_button = tk.Button(root, text="Send Secure Message", command=self.send_secure_message)
        self.send_button.pack(pady=10)

        self.read_button = tk.Button(root, text="Read Received Message", command=self.read_secure_message)
        self.read_button.pack(pady=10)

        self.server_start_button = tk.Button(root, text="Start Local Server", command=self.start_server)
        self.server_start_button.pack(pady=5)

        self.server_stop_button = tk.Button(root, text="Stop Local Server", command=self.stop_server, state=tk.DISABLED)
        self.server_stop_button.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_server(self):
        if self.server_process is None:
            # Start server.py as a subprocess
            self.server_process = subprocess.Popen([sys.executable, "server.py"])
            self.server_start_button.config(state=tk.DISABLED)
            self.server_stop_button.config(state=tk.NORMAL)
            messagebox.showinfo("Server", "Local server started. Ready to receive messages.")

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
            messagebox.showinfo("Server", "Local server stopped.")

    def send_secure_message(self):
        message = self.message_entry.get()
        phone = self.phone_entry.get()
        peer_ip = self.peer_ip_entry.get()

        if not message or not phone or not peer_ip:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        otp = generate_otp()
        send_otp_via_sms(phone, otp)

        try:
            status = send_secure_message_to_peer(message, otp, peer_ip)
            if status == 200:
                messagebox.showinfo("Success", "Encrypted message sent and OTP delivered!")
            else:
                messagebox.showerror("Error", f"Failed to send message. Status code: {status}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    def read_secure_message(self):
        otp = simpledialog.askstring("OTP Required", "Enter OTP received via SMS")
        if not otp:
            return
        try:
            decrypted_msg = read_secure_message_from_local(otp)
            if decrypted_msg is None:
                messagebox.showerror("Error", "No message received yet.")
                return
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