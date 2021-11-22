from binascii import unhexlify

text = "25091b01060948050d0948091a0d480e091a1d1a01480b000107091a0d"

def bxor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

def solve(dehextext):
    best = None
    for i in range(2**8):
        key = i.to_bytes(1, byteorder='big')
        keystream = key*len(dehextext)
        candidate_message = bxor(dehextext, keystream)
        nr_let = sum([x in ascii_chars for x in candidate_message])
        if best == None or nr_let > best['nr_let']:
            best = {'message': candidate_message, 'key': key, 'nr_let': nr_let}
    return best


text = unhexlify(text)
ascii_chars = list(range(97, 122)) + [32]

res = solve(text)

print('key: ', res['key'])
print('message: ', res['message'])
print('nr_letters: ', res['nr_let'])
