from encryption import encrypt_message
from decryption import decrypt_message

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt?: ").strip().lower()
    if choice == 'e':
        message = input("Enter the message to encrypt: ").strip()
        encrypted_message = encrypt_message(message)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        encrypted_message = input("Enter the encrypted message to decrypt: ").strip()
        encrypted_message = bytes(encrypted_message, 'utf-8')
        try:
            decrypted_message = decrypt_message(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
