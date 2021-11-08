
# Solution #1
import codecs

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()

print(b64)


#Solution #2
from base64 import b64encode, b64decode

s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64 = b64encode(bytes.fromhex(s)).decode()
print (b64)
