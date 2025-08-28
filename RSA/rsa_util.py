import random

def generate_prime(start, end):
    while True: 
        num = random.randint(start, end)
        if is_prime(num):
            return num
    
def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    for i in range(3, int(num**.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_pq():
    # if you wanted to not encrypt by blocks, make p and q larger to account for the bit length of n
    p = generate_prime(100, 500)
    q = generate_prime(100, 500)
    while p == q or abs(p-q) < 50: # make sure p, q aren't too similar in value
        q = generate_prime(100, 500) 
    return p, q


def extended_euclid(a, b):
    # ax + by = gcd(a, b)
    # ab ≡ 1 mod(phi)
    # ab + phiy = 1
    if a == 0:
        return (b, 0, 1)
    
    gcd, x, y = extended_euclid(b%a, a)

    # b%a = b - (b//a) * a
    return gcd, y-(b//a)*x, x