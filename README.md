# Secure Remote Communication Using AES Symmetric Encryption

## Introduction

This project implements a secure data transfer system over the internet using the AES symmetric encryption algorithm. The system is designed for secure communication between two remote computers. It encrypts messages on the sender's side and transmits them to the receiver. The encryption key (used as a One-Time Password, OTP) is sent to the receiver's mobile phone via SMS (currently simulated in the console). The receiver must enter this OTP to decrypt and read the message. This approach ensures both confidentiality and secure key transfer.

## Key Objectives

- Implement an encryption system using the AES symmetric algorithm.
- Integrate a key transfer mechanism (OTP via SMS) for secure and automated message transfer.
- Provide a user-friendly interface for sending and receiving encrypted messages.

## Key Features

1. **AES Encryption & Decryption**: Messages are encrypted and decrypted using the AES symmetric algorithm (ECB mode, with padding).
2. **OTP Key Transfer via SMS**: The encryption key (OTP) is sent to the receiver's mobile number via SMS (simulated).
3. **Secure Message Delivery**: The receiver must enter the OTP to decrypt and read the received message.
4. **Automated Workflow**: The application automates encryption, transmission, OTP delivery, and decryption.
5. **Network Device Discovery**: The sender can scan the local network for available receiver devices running the server.
6. **GUI Application**: Built with PyQt6, providing pages for sending, receiving, and viewing information about the app.
7. **Server Control**: The GUI allows starting and stopping the local Flask server.

## How It Works

### Sender Side

- User enters a message, receiver's phone number, and selects the receiver's device from a scanned list.
- The system generates a 6-digit OTP (encryption key).
- The message is encrypted using AES with the OTP as the key.
- The encrypted message is sent to the receiver's server.
- The OTP is sent to the receiver's phone via SMS (simulated in the console).

### Receiver Side

- User enters the OTP received via SMS.
- The application fetches the encrypted message from the local server.
- The message is decrypted using the OTP and displayed.

## Project Structure

- `main.py`: Application entry point, launches the PyQt6 GUI.
- `controller.py`: Handles logic between the GUI and backend (encryption, network, server control).
- `ui/`: Contains PyQt6 GUI components:
  - `main_window.py`: Main window and navigation.
  - `send_window.py`: Send message page.
  - `receive_window.py`: Receive message page.
  - `about_page.py`: About/info page.
- `crypto.py`: AES encryption and decryption logic.
- `sms.py`: OTP generation and (simulated) SMS sending.
- `client.py`: Sends encrypted messages to the receiver's server and reads messages from the local server.
- `server.py`: Flask server to receive and store encrypted messages.
- `network_scan.py`: Scans the local network for available servers/devices.
- `requirements.txt`: Python dependencies.

## Setup & Usage

1. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Start the Receiver's Server**
   - You can start the server from the GUI ("Start Server" button), or manually:
   ```
   python server.py
   ```

3. **Run the Application**
   ```
   python main.py
   ```

4. **Send a Secure Message**
   - Enter the message, receiver's phone number, and select the receiver's device (or enter IP).
   - Click "Send Secure Message". The OTP will be sent to the receiver's phone (simulated in console).

5. **Read a Received Message**
   - Enter the OTP received via SMS when prompted.
   - The decrypted message will be displayed.

## Features To Add

- Integrate with an actual SMS gateway.
- Use persistent storage for messages.

## Notes

- Ensure both sender and receiver are on the same network or the receiver's server is accessible over the internet.
- Phone number validation is currently set for Kenyan numbers (e.g., 0712345678 or +254712345678).
- The SMS sending is simulated; no real SMS is sent.






