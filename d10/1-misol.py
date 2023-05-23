class Car:
    def __init__(self, model, davlat, yil):
        self.model = model
        self.davlat = davlat
        self.yil = yil

    class Descriptor:
        def __get__(self, instance, owner):
            if not instance.model or not instance.davlat:
                raise ValueError("Model va davlat maydonlari bo'sh bo'lishi mumkin emas")
            if instance.yil < 1990 or instance.yil > 2021:
                raise ValueError("Yil 1990 va 2021 oralig'ida bo'lishi kerak")
            return instance

    __repr__ = lambda self: f"Car(model={self.model}, davlat={self.davlat}, yil={self.yil})"

car = Car("Cobalt", "O'zbekiston", 2021)
print(car)

input()