class Car:
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    SUV = "SUV"

    def __init__(self, model, davlat, yil, kuzov_turi, rang):
        self.model = model
        self.davlat = davlat
        self.yil = yil
        self.kuzov_turi = kuzov_turi
        self.rang = rang

    class Descriptor:
        def __get__(self, instance, owner):
            if not instance.model or not instance.davlat:
                raise ValueError("Model va davlat maydonlari bo'sh bo'lishi mumkin emas")
            if instance.yil < 1990 or instance.yil > 2021:
                raise ValueError("Yil 1990 va 2021 oralig'ida bo'lishi kerak")
            return instance

    __repr__ = lambda self: f"Car(model={self.model}, davlat={self.davlat}, yil={self.yil}, kuzov_turi={self.kuzov_turi}, rang={self.rang})"

    @staticmethod
    def get_kuzov_turlari():
        return [Car.SEDAN, Car.HATCHBACK, Car.SUV]

    @classmethod
    def from_dict(cls, car_dict):
        model = car_dict.get("model")
        davlat = car_dict.get("davlat")
        yil = car_dict.get("yil")
        kuzov_turi = car_dict.get("kuzov_turi")
        rang = car_dict.get("rang")
        return cls(model, davlat, yil, kuzov_turi, rang)

    @classmethod
    def from_list(cls, car_list):
        cars = []
        for car_dict in car_list:
            car = cls.from_dict(car_dict)
            cars.append(car)
        return cars

    @classmethod
    def get_car_by_rang(cls, cars, rang):
        result = []
        for car in cars:
            if car.rang == rang:
                result.append(car)
        return result

car1 = Car("Cobalt", "O'zbekiston", 2021, Car.SEDAN, "Oq")
car2 = Car("Spark", "AQSH", 2019, Car.HATCHBACK, "Qora")
car3 = Car("Captiva", "Rossiya", 2018, Car.SUV, "Kok")
car4 = Car("Malibu", "AQSH", 2020, Car.SEDAN, "Qizil")

cars = [car1, car2, car3, car4]

print(Car.get_car_by_rang(cars, "Qora"))
print(Car.get_car_by_rang(cars, "Sariq"))

input()