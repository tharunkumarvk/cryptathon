from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('models/l_r_model.pkl')

# Generate AES and HMAC keys
aes_key = os.urandom(32)  # AES-256 key
hmac_key = os.urandom(32)  # HMAC key

# Function to encrypt data with AES
def encrypt_data(data):
    iv = os.urandom(16)  # 16 bytes for AES-256 CBC IV
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad data to be multiple of block size (16 bytes for AES)
    padded_data = data + ' ' * (16 - len(data) % 16)
    encrypted_data = encryptor.update(padded_data.encode()) + encryptor.finalize()
    return iv + encrypted_data  # Prepend IV for decryption

# Function to create HMAC
def create_hmac(data):
    h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=default_backend())
    h.update(data)
    return h.finalize()

# Home route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data sent in the request
    data = request.json.get('input_data')

    # Check if data is valid
    if not data or len(data) != 9:
        return jsonify({'error': 'Invalid input data. Please provide exactly 9 features.'}), 400

    # Convert input data to numpy array and reshape for the model
    input_array = np.array(data).reshape(1, -1)
    prediction = model.predict(input_array)

    # Logic based on label 1 (Regular) vs. other labels (Attacks)
    if prediction[0] == 1:  # Assuming 1 represents 'regular'
        # Encrypt the data and create HMAC for safe responses
        encrypted_data = encrypt_data("Data is regular and secured")
        data_hmac = create_hmac(encrypted_data)

        # Return encrypted data and HMAC in response
        return jsonify({
            'status': 'safe',
            'message': 'Data is regular and secured',
            'encrypted_data': encrypted_data.hex(),
            'hmac': data_hmac.hex()
        })
    else:
        # Indicate that an attack has been detected
        return jsonify({
            'status': 'blocked',
            'message': 'Attack detected! Source is blocked.'
        })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
