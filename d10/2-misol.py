class Car:
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    SUV = "SUV"

    def __init__(self, model, davlat, yil, kuzov_turi):
        self.model = model
        self.davlat = davlat
        self.yil = yil
        self.kuzov_turi = kuzov_turi

    class Descriptor:
        def __get__(self, instance, owner):
            if not instance.model or not instance.davlat:
                raise ValueError("Model va davlat maydonlari bo'sh bo'lishi mumkin emas")
            if instance.yil < 1990 or instance.yil > 2021:
                raise ValueError("Yil 1990 va 2021 oralig'ida bo'lishi kerak")
            return instance

    __repr__ = lambda self: f"Car(model={self.model}, davlat={self.davlat}, yil={self.yil}, kuzov_turi={self.kuzov_turi})"

    @staticmethod
    def get_kuzov_turlari():
        return [Car.SEDAN, Car.HATCHBACK, Car.SUV]

    @classmethod
    def from_dict(cls, car_dict):
        model = car_dict.get("model")
        davlat = car_dict.get("davlat")
        yil = car_dict.get("yil")
        kuzov_turi = car_dict.get("kuzov_turi")
        return cls(model, davlat, yil, kuzov_turi)

car = Car("Cobalt", "O'zbekiston", 2021, Car.SEDAN)
print(car)

input()