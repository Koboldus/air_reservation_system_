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

    def __str__(self):
        return f'Temperature {self.temp_c}'

    def __repr__(self):
        return f'{type(self).__name__} (temp={self._temp})'

    def __format__(self, format_spec):
        formatters = {
            'c': self.temp_c,
            'f': self.temp_f
        }

        return formatters.get(format_spec, self.temp_c)

#        match format_spec:
#            case 'c':
#                return self.temp_c
#            case 'f':
#                return self.temp_f
#            case _:
#                return self.temp_c

#        if 'c' == format_spec:
#            result = self.temp_c
#        elif 'f' == format_spec:
#            result = self.temp_f
#        else:
#            result = self.temp_c
#
#        return result
            
class MarsTemperature(Temperature):
    pass

class JupiterTemperature(Temperature):
    pass

t = Temperature(40)
t2 = Temperature(2137)
t3 = JupiterTemperature(8000)
#print(str(t), repr(t))
#print(str(t2), repr(t2))
#print(str(t3), repr(t3))
print(f'{t:c}', f'{t:f}')