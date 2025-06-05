import tkinter as tk
from tkinter import simpledialog, messagebox

class SecureMessengerApp:
    def __init__(self, root, send_callback, read_callback, start_server_callback, stop_server_callback, on_close_callback):
        self.root = root
        self.root.title("Secure Messenger (Peer-to-Peer)")

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

        self.send_button = tk.Button(root, text="Send Secure Message", command=send_callback)
        self.send_button.pack(pady=10)

        self.read_button = tk.Button(root, text="Read Received Message", command=read_callback)
        self.read_button.pack(pady=10)

        self.server_start_button = tk.Button(root, text="Start Local Server", command=start_server_callback)
        self.server_start_button.pack(pady=5)

        self.server_stop_button = tk.Button(root, text="Stop Local Server", command=stop_server_callback, state=tk.DISABLED)
        self.server_stop_button.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", on_close_callback)

    def get_message(self):
        return self.message_entry.get()

    def get_phone(self):
        return self.phone_entry.get()

    def get_peer_ip(self):
        return self.peer_ip_entry.get()

    def set_server_buttons(self, started):
        if started:
            self.server_start_button.config(state=tk.DISABLED)
            self.server_stop_button.config(state=tk.NORMAL)
        else:
            self.server_start_button.config(state=tk.NORMAL)
            self.server_stop_button.config(state=tk.DISABLED)

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def ask_otp(self):
        return simpledialog.askstring("OTP Required", "Enter OTP received via SMS")