import unittest
from decryption import decrypt_message
from encryption import encrypt_message, generate_key

class TestDecryption(unittest.TestCase):

    def setUp(self):
        generate_key()

    def test_decrypt_message(self):
        message = "Test message"
        encrypted_message = encrypt_message(message)
        decrypted_message = decrypt_message(encrypted_message)
        self.assertEqual(message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
