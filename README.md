# 🔐 Caesar Cipher Tool

A simple and interactive Python-based cryptography tool that performs **text encryption and decryption using the Caesar Cipher algorithm**.

## 📌 Overview

The Caesar Cipher is a classical substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

This project provides a command-line interface (CLI) that allows users to:

- Encrypt messages
- Decrypt encrypted messages
- Choose a custom shift value
- Handle uppercase and lowercase letters
- Preserve spaces and special characters

## ✨ Features

- 🔒 Text Encryption
- 🔓 Text Decryption
- 🔢 Custom Shift Value
- 🔠 Uppercase & Lowercase Support
- 📝 Preserves Spaces and Special Characters
- 💻 Simple Command-Line Interface
- ⚡ Lightweight and easy to use

## 🛠️ Technologies Used

- **Python 3**
- **String Manipulation**
- **ASCII / Alphabet Indexing**
- **Command-Line Interface (CLI)**

## 📂 Project Structure

```text
Caesar-Cipher-Tool/
│
├── main.py
└── README.md
⚙️ How It Works

The Caesar Cipher shifts each alphabetic character by a specified number of positions.

For example, with a shift value of 3:

A → D
B → E
C → F

Example:

Plaintext:
HELLO

Shift:
3

Encrypted:
KHOOR

Decryption reverses the same process:

KHOOR → HELLO
🚀 Installation & Usage
1. Clone the repository
git clone https://github.com/ragavi1930-k/casesar-cipher-tool.git
2. Navigate to the project directory
cd casesar-cipher-tool
3. Run the program
python main.py
💻 Example
================================
      CAESAR CIPHER TOOL
================================

1. Encrypt
2. Decrypt
3. Exit

Enter your choice: 1

Enter message: Hello World
Enter shift value: 3

Encrypted Text: Khoor Zruog

Decryption:

Enter your choice: 2

Enter message: Khoor Zruog
Enter shift value: 3

Decrypted Text: Hello World
🔐 Security Note

Caesar Cipher is a classical cryptographic technique and is not considered secure for protecting sensitive or confidential information.

It is mainly useful for:

##Learning cryptography fundamentals
Understanding substitution ciphers
Practicing Python programming
Understanding encryption and decryption concepts
🎯 Learning Outcomes

##Through this project, I practiced:

Python programming
Functions and loops
Conditional statements
String manipulation
Character encoding concepts
Basic cryptography
Encryption and decryption logic
Git and GitHub
🔮 Future Improvements

##Possible future enhancements include:

 Brute-force attack / all-shift decoder
 Frequency analysis
 File encryption support
 Graphical User Interface (GUI)
 Input validation
 Better error handling
 Automatic shift detection
