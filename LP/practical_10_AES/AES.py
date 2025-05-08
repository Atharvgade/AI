# AES Algorithm Implementation in Python
# Easy, Clear, Suitable for 3rd-year Engineering

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    # Padding to make the text a multiple of 16 bytes
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_bytes = cipher.encrypt(padded_text.encode())
    encrypted_text = base64.b64encode(encrypted_bytes).decode()
    return encrypted_text

def decrypt_message(key, encrypted_text):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = decrypted_bytes.decode().rstrip()
    return decrypted_text

def main():
    print("AES Algorithm Implementation\n")

    plaintext = input("Enter message to encrypt: ")

    # AES key must be either 16, 24, or 32 bytes long
    key = get_random_bytes(16)  # 128-bit AES key
    print(f"\nGenerated AES Key (in bytes): {key}")

    encrypted_text = encrypt_message(key, plaintext)
    print(f"\nEncrypted Message: {encrypted_text}")

    decrypted_text = decrypt_message(key, encrypted_text)
    print(f"\nDecrypted Message: {decrypted_text}")

if __name__ == "__main__":
    main()

