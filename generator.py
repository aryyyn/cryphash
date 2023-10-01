import random

result = []

char = 'a'

while char <= 'z':
    char_result = []
    b = 3
    while(b!=0):
        randomchar = random.randbytes(3)
        char_result.append(randomchar)
        b-=1
    result.append((char,char_result))
    char = chr(ord(char) + 1)

for hm in result:
    print(f"{hm[0]} = {hm[1]}")
