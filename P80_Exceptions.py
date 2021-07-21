try:
    # print(10 / 0)
    print('hallo')

    # print(int('asdf'))

    # print(hallo)
    # zahlen = [1, 2]
    # print(zahlen[2])

    print(asdf)
except ZeroDivisionError:
    print('Gefangen')
except ValueError:
    print('Falscher Wert / Cast')
# catch (ArrayIndexOutOfBoundsException e)
except IndexError as e:
    print('Ungültiger index')
    print(dir(e))
    print(e.args)
    # print(e.__cause__)
except Exception:
    print('alles andere')