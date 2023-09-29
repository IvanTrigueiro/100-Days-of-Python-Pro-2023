def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


# print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    # print(kwargs)
    n += kwargs.get("add")
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
