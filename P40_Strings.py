import re

wort = 'hallo'

# Substring
print(wort[0:3])
print(wort[::2])

bild = 'test.jpg'
print(bild[-4:])

# Start:End:Interval
print(bild[:-4])

# charAt
print(bild[1])

# SUchen (indexOf)
print(bild.find('.'))
print(bild.find('test'))


print(bild.find('asdf'))

# Ersetzen
print('hallo welt'.replace('welt', 'python'))

# Replace unterstützt so keine Regular Expressions
print('hallo welt'.replace('w.*t', 'python'))

# print('hallo welt'.)

print(re.findall('w.*t', 'hallo welt'))
print(re.subn('w.*t', 'python', 'hallo welt')[0])

funde = re.findall('w.*t', 'hallo welt')

for fund in funde:
    print('hallo welt'.replace(fund, 'python'))

# Großbuchstaben
print(wort.upper())
print(wort.lower())

wort += ' neues Wort'
print(wort)

trim = ' eine blöde Eingabe\n '

print(trim.strip())
print('hallo'.capitalize())

print('hallo'.startswith('hallo'))
print('hallo.jpg'.endswith('.jpg'))

# .isnumeric() .is_numeric() -
print('42'.isnumeric())

print('bernd;huber;42'.split(';'))


