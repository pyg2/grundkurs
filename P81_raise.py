# class PsZeroError extends ValueError {..

class PsZeroError(ValueError):
    pass


class PsTooHighError(ValueError):
    pass


class Auto:
    def __init__(self, ps):
        self.set_ps(ps)

    def set_ps(self, ps):
        if not ps:
            raise PsZeroError('Bitte einen Wert der nicht 0 ist')

        if ps > 1000:
            raise PsTooHighError('Glaub ich nicht')

        self.ps = ps

try:
    a1 = Auto(24)
    # a1.set_ps(99999)
    a1.set_ps(0)
except PsTooHighError:
    print('Dein Auto ist zu schnell')
except PsZeroError:
    print('bitte PS eintippen')
