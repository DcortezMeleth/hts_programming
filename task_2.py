from PIL import Image

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value: key for key, value in CODE.items()}

im = Image.open('image.png')
pix = im.load()
(x, y) = im.size
print 'x: ', x
print 'y: ', y
counter = 0
encoded = ''
for i in xrange(y):
    for j in xrange(x):
        if pix[j, i]:
            encoded += chr(counter)
            counter = 0
        counter += 1
print encoded
tokens = encoded.split()
print tokens
decoded = ''
for token in tokens:
    if token[0] == '/':
        decoded += ' '
        token = token[1:]
    if token[-1] == '/':
        decoded += ' '
        token = token[:-1]
    if token in CODE_REVERSED:
        decoded += CODE_REVERSED[token]
print decoded.lower()