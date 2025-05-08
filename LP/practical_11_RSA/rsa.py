import random

# Function to find GCD (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find Multiplicative Inverse (for private key d)
def multiplicative_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate RSA key pair
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    if p == q:
        raise ValueError('p and q cannot be equal.')

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate d, the modular inverse of e mod phi
    d = multiplicative_inverse(e, phi)
    if d is None:
        raise Exception('Failed to find the modular inverse.')

    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

# Function to decrypt a message
def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main function
def main():
    print("RSA Algorithm Implementation\n")

    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))

    # Generate RSA keys
    public, private = generate_keypair(p, q)

    print(f"\nPublic Key: {public}")
    print(f"Private Key: {private}")

    message = input("\nEnter message to encrypt: ")
    
    # Encrypt and then decrypt the message
    encrypted_msg = encrypt(public, message)
    decrypted_msg = decrypt(private, encrypted_msg)

    print(f"\nEncrypted message: {encrypted_msg}")
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()

