class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

    def get_airline(self):
        return self.flight_number[:2]
    
    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

class Airplane:
    pass

class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model(self):
        return "Boeing 737 Max"

class AirbusA380(Airplane):
    @staticmethod
    def get_airplane_model(self):
        return "Airbus A380"


b = Boeing737Max()
a = AirbusA380

f = Flight("BA120", a)

print(f.get_airline())
print(f.get_number())
print(f.get_model())