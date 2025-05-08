def and_with_127(ch):
    return chr(ord(ch) & 127)

def xor_with_127(ch):
    return chr(ord(ch) ^ 127)

def main():
    input_string = input("Enter a string: ")
    and_result = ''.join(and_with_127(ch) for ch in input_string)
    xor_result = ''.join(xor_with_127(ch) for ch in input_string)

    print("Original String:", input_string)
    print("String after AND with 127:", and_result)
    print("String after XOR with 127:", xor_result)

