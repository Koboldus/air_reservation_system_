class Temperature:
    def __init__(self, temp):
        self.temp_c = temp

    @property
    def temp_c(self):
        return f'{self._temp}°C'

    @temp_c.setter
    def temp_c(self, value):
        if value < -273.15:
            raise ValueError(f'too cold: {value}')

        self._temp = value

    @property
    def temp_f(self):
        return f'{32 + 9 / 5 * self._temp:.2f}°F'

    @temp_f.setter
    def temp_f(self, value):
        self.temp_c = 5 / 9 * (value - 32)

t = Temperature(40)
t.temp_c = 40
print(t.temp_c)
print(t.temp_f)
t.temp_f = 40
print(t.temp_c)
print(t.temp_f)
# print(dir(t), vars(t))