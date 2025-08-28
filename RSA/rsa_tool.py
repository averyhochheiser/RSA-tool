import argparse
from rsa_core import generate_keys, encryption, decryption

pub, priv = generate_keys()
a, n = pub
b, _ = priv

parser = argparse.ArgumentParser(description='Encrypts and decrypts RSA')
parser.add_argument('message', help='enter the message to use. for strings use ""')
args = parser.parse_args()

message = args.message
print("Original message:", message)

# Encrypt the message
encrypted_blocks, is_text = encryption(message, a, n)
print("Encrypted blocks:", encrypted_blocks)

# If you wanted to decrypt only
# is_text = True
# encrypted_blocks = [encrypted text here]
# b = 
# n = 

# Decrypt the message
decrypted_message = decryption(b, n, encrypted_blocks, is_text)
print("Decrypted message:", decrypted_message)

assert message == decrypted_message, "Decryption failed :("
print("Decrypted :)")