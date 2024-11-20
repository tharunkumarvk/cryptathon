CAN Bus Security: Anomaly Detection and Prevention Using AES-128 and HMAC
This project implements security measures for the Controller Area Network (CAN) Bus used in modern vehicular networks. The system utilizes AES-128 encryption and HMAC (Hash-based Message Authentication Code) for securing communication and preventing malicious activities within the network. The goal is to provide confidentiality, integrity, and real-time anomaly detection in CAN Bus communication to enhance automotive cybersecurity.

Table of Contents
Project Overview
Technologies Used
Problem Statement
Objectives
How It Works
Installation
Usage
File Structure
License
Acknowledgments
Project Overview
In modern vehicular systems, CAN Bus plays a critical role in communication between Electronic Control Units (ECUs). However, its open architecture has made it vulnerable to cyberattacks. This project focuses on enhancing CAN Bus security by implementing encryption and authentication techniques using AES-128 for confidentiality and HMAC for message integrity. Additionally, the project includes an anomaly detection system to identify abnormal CAN Bus behavior and protect against attacks like spoofing, message injection, and replay attacks.

Technologies Used
AES-128 Encryption: Used for encrypting the CAN messages to ensure the confidentiality of sensitive data being transmitted between ECUs.
HMAC (Hash-based Message Authentication Code): Utilized for message authentication and integrity checking to ensure that the messages have not been tampered with or altered during transmission.
CAN Bus Simulation: A simulated CAN Bus environment used to model real-time vehicular network communication.
Python: The primary programming language used for implementing cryptographic algorithms and anomaly detection mechanisms.
Flask: A lightweight web framework used for building a simple API for simulating CAN Bus communication and interaction.
Problem Statement
The Controller Area Network (CAN) Bus, widely used in automotive communication systems, is susceptible to various cyber threats due to its open and non-secure design. Unauthorized access, message alteration, and replay attacks pose significant risks to vehicular networks, potentially leading to compromised vehicle functionality and safety. There is an urgent need to implement a robust security system to detect and prevent such attacks in CAN Bus communication.

Objectives
Implement AES-128 encryption for secure communication between ECUs on the CAN Bus network.
Use HMAC for message authentication to verify the integrity and authenticity of transmitted messages.
Detect anomalies in CAN Bus messages to identify potential security breaches or malicious activity.
Develop a real-time security solution that ensures continuous monitoring and immediate response to detected threats.
Benchmark the system to evaluate the performance and effectiveness of the cryptographic measures in securing the CAN Bus network.
How It Works
AES-128 Encryption:

AES-128 is used to encrypt the CAN messages to ensure that even if the data is intercepted, it cannot be read by unauthorized entities.
The key for AES encryption is shared securely between the ECUs at the time of network initialization.
HMAC:

An HMAC is generated for each message sent on the CAN Bus to verify the authenticity of the message.
HMAC uses a cryptographic hash function (e.g., SHA-256) combined with a secret key to produce a unique tag for each message.
If the HMAC tag does not match the expected value on the receiving end, the message is considered tampered or invalid.
Anomaly Detection:

The system analyzes incoming CAN messages to detect patterns that deviate from the expected normal behavior.
Any anomaly triggers an alert, which helps to identify potential cyberattacks like replay or injection attacks.
Installation
Prerequisites:
Python 3.6 or later
Flask (for API simulation)
PyCryptodome (for AES and HMAC)

Usage
Submit Input Data: Provide 9 comma-separated features (e.g., CAN ID, Data values) for prediction.
View Results: The system will display:
Prediction Result: Based on encrypted and authenticated data.
Encrypted Data: Displaying the AES-encrypted message.
HMAC: Showing the generated HMAC for message integrity.
The web interface will show the predicted results, encrypted data, and HMAC information when the data is submitted.

File Structure
graphql
Copy code
can-bus-security/
│
├── app.py              # Main Flask application for CAN Bus simulation
├── requirements.txt    # Python dependencies
├── aes_hmac.py         # Implementation of AES and HMAC
├── can_data_simulator.py  # Simulated CAN Bus data generation
├── static/             # Contains static files for web interface
│   ├── style.css
│   └── script.js
└── templates/          # HTML templates for the web interface
    └── index.html

Acknowledgments
Special thanks to the contributors of the PyCryptodome library for their AES and HMAC implementations.
The project was inspired by the need to improve automotive network security, especially for in-vehicle communication systems like CAN Bus.
Thanks to the open-source community for providing resources and tutorials on cryptography and anomaly detection.
