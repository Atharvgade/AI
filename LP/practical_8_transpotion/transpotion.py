# Program: Transposition Cipher Encryption and Decryption (Ignoring spaces during encryption)
# Subject: AI / Computer Science 3rd Year Practical

def encrypt_transposition(plaintext):
    """Encrypt using simple transposition cipher, ignoring spaces."""
    plaintext_nospace = plaintext.replace(" ", "")
    even_chars = plaintext_nospace[::2]
    odd_chars = plaintext_nospace[1::2]
    return even_chars + odd_chars

def decrypt_transposition(ciphertext, original_plaintext):
    """Decrypt the transposition cipher and restore spaces."""
    # Find positions of spaces in original plaintext
    space_positions = [i for i, ch in enumerate(original_plaintext) if ch == ' ']
    
    half = (len(ciphertext) + 1) // 2
    even_chars = ciphertext[:half]
    odd_chars = ciphertext[half:]
    
    # Merge even and odd characters
    plaintext_nospace = ""
    for i in range(half):
        plaintext_nospace += even_chars[i]
        if i < len(odd_chars):
            plaintext_nospace += odd_chars[i]
    
    # Now restore spaces
    final_plaintext = ""
    j = 0  # Pointer for characters from decrypted nospace text
    for i in range(len(original_plaintext)):
        if i in space_positions:
            final_plaintext += ' '
        else:
            final_plaintext += plaintext_nospace[j]
            j += 1
    
    return final_plaintext

def main():
    """Main function to take input and perform encryption/decryption."""
    plaintext = input("Enter the message: ")
    
    encrypted = encrypt_transposition(plaintext)
    print("\nEncrypted Message (no spaces):", encrypted)
    
    decrypted = decrypt_transposition(encrypted, plaintext)
    print("Decrypted Message (spaces restored):", decrypted)

if __name__ == "__main__":
    main()

