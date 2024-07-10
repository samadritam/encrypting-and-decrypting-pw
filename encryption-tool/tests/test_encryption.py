import unittest
from encryption import encrypt_message, generate_key, load_key

class TestEncryption(unittest.TestCase):

    def setUp(self):
        generate_key()

    def test_encrypt_message(self):
        message = "Test message"
        encrypted_message = encrypt_message(message)
        self.assertIsNotNone(encrypted_message)

if __name__ == '__main__':
    unittest.main()
