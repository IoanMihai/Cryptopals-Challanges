from binascii import unhexlify

ascii_chars = list(range(97, 122)) + [32]

class InvalidMessageException(Exception):
    pass

def bxor(a, b):
    return bytes([x^y for (x,y) in zip(a, b)])

def letter_ratio(input_bytes):
    nr_let = sum([x in ascii_chars for x in input_bytes])
    return nr_let / len(input_bytes)

def is_text(input_bytes):
    r = letter_ratio(input_bytes)
    return True if r>0.7 else False

def solve(dehextext):
    best = {'nr_let': 0}
    for i in range(2**8):
        key = i.to_bytes(1, byteorder='big')
        keystream = key*len(dehextext)
        candidate_message = bxor(dehextext, keystream)
        nr_let = sum([x in ascii_chars for x in candidate_message])
        if nr_let > best['nr_let']:
            best = {"message": candidate_message, 'nr_let': nr_let, 'key': key}

    if best['nr_let'] > 0.7 * len(dehextext):
        return best
    else:
        raise InvalidMessageException('best candidate message is: %s' % best['message'])


with open("test.in") as data_file:
    text_list = [unhexlify(line.strip()) for line in data_file]

candidates = list()
for (line_nr, text) in enumerate(text_list):
    try:
        message = solve(text)['message']
    except InvalidMessageException:
        pass
    else:
        candidates.append({
            'line_nr': line_nr,
            'text': text,
            'message': message
        })


if len(candidates) > 1:
    print("Error: more than one candidate")
else:
    for (key, value) in candidates[0].items():
        print(f'{key}: {value}')
