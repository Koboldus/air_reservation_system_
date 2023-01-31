from pprint import pprint as pp

from flight import Flight

from airplane import Airplane

from boeing737max import Boeing737Max

from airbusa380 import AirbusA380

def make_flight():
    pass

b = Boeing737Max()
a = AirbusA380()
# print(b.get_airplane_model())
f = Flight('BA120', b)
# print(f.get_airline())
# print(f.get_number())
# print(f.get_model())

# pp(f.seats)
f.allocate_passenger('12C', 'Jarosław K')
f.allocate_passenger('1D', 'Lech K')
f.allocate_passenger('12E', 'Antoni M')
pp(f.seats)

if __name__ == '__main__':
    make_flight()