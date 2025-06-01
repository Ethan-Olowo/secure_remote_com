from flask import Flask, request

app = Flask(__name__)
# TODO: Switch to using a database or persistent storage
message_store = ""

@app.route('/receive', methods=['POST'])
def receive():
    global message_store
    data = request.get_json()
    message_store = data.get('encrypted_msg', '')
    return 'Received', 200

@app.route('/get_message', methods=['GET'])
def get_message():
    return {'encrypted_msg': message_store}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)