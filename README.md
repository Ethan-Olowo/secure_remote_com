# Secure Remote Communication Using AES Symmetric Encryption

## Introduction

This project implements a secure data transfer system over the internet using the AES symmetric encryption algorithm. The system is designed for secure communication between two remote computers. It encrypts messages on the sender's side and transmits them to the receiver. The encryption key (used as a One-Time Password, OTP) is sent to the receiver's mobile phone via SMS. The receiver must enter this OTP to decrypt and read the message. This approach ensures both confidentiality and secure key transfer.

## Key Objectives

- Implement an encryption system using the AES symmetric algorithm.
- Integrate a key transfer mechanism (OTP via SMS) for secure and automated message transfer.
- Provide a user-friendly interface for sending and receiving encrypted messages.

## Key Features

1. **AES Encryption & Decryption**: Messages are encrypted and decrypted using the AES symmetric algorithm.
2. **OTP Key Transfer via SMS**: The encryption key (OTP) is sent to the receiver's mobile number via SMS.
3. **Secure Message Delivery**: The receiver must enter the OTP to decrypt and read the received message.
4. **Automated Workflow**: The application automates encryption, transmission, OTP delivery, and decryption.

## How It Works

1. **Sender Side**:
   - User enters a message, receiver's phone number, and receiver's IP address.
   - The system generates a 6-digit OTP (encryption key).
   - The message is encrypted using AES with the OTP as the key.
   - The encrypted message is sent to the receiver's server.
   - The OTP is sent to the receiver's phone via SMS.

2. **Receiver Side**:
   - User enters the OTP received via SMS.
   - The application fetches the encrypted message from the server.
   - The message is decrypted using the OTP.

## Project Structure

- `ui.py`: Graphical user interface for sending and receiving messages.
- `crypto.py`: AES encryption and decryption logic.
- `sms.py`: OTP generation and (simulated) SMS sending.
- `client.py`: Sends encrypted messages to the receiver's server.
- `server.py`: Flask server to receive and store encrypted messages.
- `requirements.txt`: Python dependencies.

## Setup & Usage

1. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Start the Receiver's Server**
   ```
   python server.py
   ```

3. **Run the Application**
   ```
   python ui.py
   ```

4. **Send a Secure Message**
   - Enter the message, receiver's phone number, and receiver's IP address.
   - Click "Send Secure Message". The OTP will be sent to the receiver's phone (currently simulated in console).

5. **Read a Received Message**
   - Enter the OTP received via SMS when prompted.
   - The decrypted message will be displayed.

## Features To Add

- Integrate with an actual SMS gateway.
- Use persistent storage.

## Note
- Ensure both sender and receiver are on the same network or the receiver's server is accessible over the internet.





