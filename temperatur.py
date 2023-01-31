class Temperature:
    def __init__(self, temp):
        self._temp = temp

    @property
    def temp(self):
        return f'{self._temp}C'

    def set_temp(self, value):
        if value < -273.15:
            raise ValueError(f'too cold')

        self._temp = value

t = Temperature(42)

print(t.temp())