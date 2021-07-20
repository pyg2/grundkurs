# Palindrom
# anna, rentner, reliefpfeiler
# hallo => ollah

eingabe = input('Wort? ')
umgedreht = ''

# for (int i = eingabe.length -1; i >= 0; i--)

for i in range(len(eingabe) - 1, -1, -1): # 4 3 2 1 0
    umgedreht += eingabe[i]

if umgedreht.lower() == eingabe.lower():
    print(eingabe, 'ist ein Palindrom')
else:
    print(eingabe, 'ist KEIN Palindrom')

print('hallo'[::-1])

## Viel einfacher in Python
umgedreht = eingabe[::-1]

# Oder als ARray
liste = [] + eingabe
liste.reverse()

