import random

def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def send_otp_via_sms(receiver_phone, otp):
    # TODO: Implement actual SMS sending logic here
    print(f"OTP {otp} sent to {receiver_phone} (simulated)")
    return