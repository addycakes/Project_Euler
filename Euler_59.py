'''

Euler Problem 59

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and
the key is made up of random bytes. The user would keep the encrypted message and the
encryption key in different locations, and without both "halves", it is impossible to decrypt the
message.

Unfortunately, this method is impractical for most users, so the modified method is to use a
password as a key. If the password is shorter than the message, which is likely, the key is repeated
cyclically throughout the message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words, decrypt the message
and find the sum of the ASCII values in the original text.

'''

keys = []

for i in range(103,104):
    for j in range(108,120):
        for k in range(97,104):
            char1 = chr(i)
            char2 = chr(j)
            char3 = chr(k)

            keys += [char1+char2+char3]

f = open('/Users/adam/Desktop/cipher.txt','r')
cipher_text = f.read().split(',')
f.close()

def xor(input_bits, k):
    output_bits = []
    i = 20
    x = 1
    for bit in input_bits:

#        if i == 0:
#            break
        
        if x == 1:
            letter = k[0]
        elif x == 2:
            letter = k[1]

        elif x == 3:
            letter = k[2]
            x = 0

        value = ord(letter)
        output_bits += [chr(int(bit)^value)]
        i -= 1
        x += 1
    
    return output_bits

#for key in keys:
#    print "".join(xor(cipher_text, key))

plain_text = xor(cipher_text,'god')
print "".join(plain_text)

ascii_sum = 0
for char in plain_text:
    ascii_sum += ord(char)

print ascii_sum

