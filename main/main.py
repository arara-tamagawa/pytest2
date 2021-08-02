class Car:
    def __init__(self, name='Banana', amount=10_000_000):
        self.car_name = name
        self.car_amount = amount

    def car_display_price(self):
        return f'{self.car_amount:,}円'