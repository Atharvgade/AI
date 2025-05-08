# Python Program to Implement Basic DES Algorithm (Simplified)

# Permutation tables and S-boxes (shortened for clarity)
# Full tables can be added for detailed working

# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansion D-box Table
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# Sample S-box (only one shown for brevity)
SBOX = [
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
]

# Permutation Function
def permute(block, table):
    return [block[x-1] for x in table]

# Left Circular Shift
def shift_left(block, n):
    return block[n:] + block[:n]

# XOR operation
def xor(t1, t2):
    return [a ^ b for a, b in zip(t1, t2)]

# Convert a string to binary
def str_to_bin(s):
    binval = []
    for c in s:
        binval += [int(x) for x in format(ord(c), '08b')]
    return binval

# Convert binary to string
def bin_to_str(b):
    strdata = ''
    for i in range(0, len(b), 8):
        byte = b[i:i+8]
        strdata += chr(int(''.join([str(x) for x in byte]), 2))
    return strdata

# The f function (fixed)
def f(right, key):
    right_expanded = permute(right, E)
    xored = xor(right_expanded, key)
    
    # Only using one S-box for simplicity
    row = (xored[0] << 1) + xored[5]
    col = (xored[1] << 3) + (xored[2] << 2) + (xored[3] << 1) + xored[4]
    value = SBOX[0][row][col]
    bin_value = [int(x) for x in format(value, '04b')]

    return bin_value  # No P permutation here

# Main DES encryption function
def des_encrypt(plaintext, key):
    plaintext = str_to_bin(plaintext)
    key = str_to_bin(key)

    # Initial Permutation
    plaintext = permute(plaintext, IP)

    # Splitting
    left = plaintext[:32]
    right = plaintext[32:]

    # Key schedule (simplified for illustration)
    round_key = key[:48]  # Just take first 48 bits

    # 16 rounds
    for i in range(16):
        right_expanded = f(right, round_key)
        new_right = xor(left[:4], right_expanded) + left[4:]  # Match sizes
        left = right
        right = new_right

    # 32-bit swap
    combined = right + left

    # Final Permutation
    cipher = permute(combined, FP)

    return bin_to_str(cipher)

# Driver Code
def main():
    plaintext = input("Enter the plaintext (8 characters): ")
    key = input("Enter the key (8 characters): ")
    
    if len(plaintext) != 8 or len(key) != 8:
        print("Both plaintext and key must be exactly 8 characters long.")
        return

    cipher = des_encrypt(plaintext, key)
    print("\nEncrypted Cipher Text:", cipher)

if __name__ == "__main__":
    main()

