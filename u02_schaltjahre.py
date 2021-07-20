"""
Schaltjahre

- Sind die durch 4 teilbar
- ausser sie sind durch 100 teilbar und nicht durch 400

Schaltjahre: 2000, 2020, 2016
KEINE: 2021, 2018, 1900, 1800, 1700
"""

jahr_als_str = input('Zahl? ')

if not jahr_als_str.isnumeric():
    print('Bitte eine Zahl eingeben')
    exit(42)

jahr = int(jahr_als_str)



if jahr % 4 != 0:
    print('Kein Schaltjahr')
elif jahr % 100 == 0 and jahr % 400 != 0:
    print('Kein Schaltjahr')
else:
    print('EIN Schaltjahr')

