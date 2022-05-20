class Car:
    counter = 0
    last_model = None

    def __init__(self, model: str, counter):
        self.model = model
        self.counter = counter
        Car.counter += 1
        Car.last_model = model


    def __str__(self):
        return self.counter

    @classmethod
    def get_counter(cls):
        return cls.counter


if __name__ == '__main__':
    honda = Car(model='honda', counter=5)
    tesla = Car(model='tesla', counter=10)
    bmw = Car(model='BMW', counter=17)
    print(Car.get_counter())
