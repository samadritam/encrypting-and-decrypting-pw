from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('secret.key', 'rb').read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

if __name__ == "__main__":
    generate_key()
    message = "This is a secret message"
    encrypted = encrypt_message(message)
    print(f"Encrypted: {encrypted}")
