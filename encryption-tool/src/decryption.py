from cryptography.fernet import Fernet

def load_key():
    return open('secret.key', 'rb').read()

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')

if __name__ == "__main__":
    encrypted_message = b"...encrypted message..."
    decrypted = decrypt_message(encrypted_message)
    print(f"Decrypted: {decrypted}")
