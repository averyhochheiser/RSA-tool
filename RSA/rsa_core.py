from rsa_util import extended_euclid, generate_pq
from rsa_messages import text_to_int, int_to_text, split_blocks, join_blocks, encrypt_block, decrypt_block
import random

def generate_keys():
    p, q = generate_pq()
    
    # for 2 primes p, q, phi(p*q) = (p-1)(q-1) = phi(n) 
    phi = (p-1) * (q-1)
    n = p*q

    # public key
    # a is random st gcd(a, phi) = 1 & 1 < a < phi
    while True:
        a = random.randint(2, phi-1)
        gcd, _, _ = extended_euclid(a, phi)
        if gcd == 1:
            break

    # private key
    # b is exp st ab ≡ 1 mod phi
    # a * priv + phi * k = gcd
    # for RSA since gcd 1, a * priv ≡ 1 mod(phi)
    # priv is modular inverse of a mod(phi)
    gcd, priv, _ = extended_euclid(a, phi)
    assert(abs(gcd) == 1)
    # extended euclid can return neg value
    # this turns possibly neg solution into pos one
    b = priv % phi

    return (a, n), (b, n)

def encryption(x, a, n):
    is_text = isinstance(x, str)
    if is_text:
        message = text_to_int(x)
    else:
        message = x

    # split message into blocks and encrypt
    # x value cannot be > n, if so multiple values lead to the same encryption
    blocks = split_blocks(message, n)
    encrypted_blocks =[encrypt_block(block, a, n) for block in blocks]

    return encrypted_blocks, is_text
    
def decryption(b, n, encrypted_blocks, is_text):
    # decrypt and recombine
    decrypted_blocks = [decrypt_block(block, b, n) for block in encrypted_blocks]
    num = join_blocks(decrypted_blocks, n)

    if is_text:
        return int_to_text(num)
    return num











    
    
    
