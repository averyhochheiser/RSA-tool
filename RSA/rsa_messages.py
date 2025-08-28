# Encode text into integers
def text_to_int(text):
    return int.from_bytes(text.encode(), 'big')

# Reconvert integers into text 
def int_to_text(num):
    byte_len = (num.bit_length() + 7) // 8 # rounds bit length to nearest byte
    return num.to_bytes(byte_len, 'big').decode()

# handle messgaes > n = pq
def split_blocks(num, n):
    block_size = n.bit_length() - 1
    blocks = []
    
    mask = ((1 << block_size) - 1) # mask with 1s
    while num > 0:
        blocks.append(num & mask)
        num >>= block_size # shift for next block

    # reverse so message still reads left to right 
    return list(reversed(blocks))

def join_blocks(blocks, n):
    block_size = n.bit_length() - 1
    num = 0 # mask of 0s

    for block in blocks:
        num = (num << block_size) | block
    return num

# per block encrypt
def encrypt_block(x, a, n):
    return pow(x, a, n)

def decrypt_block(y, b, n):
    return pow(y, b, n)

        

