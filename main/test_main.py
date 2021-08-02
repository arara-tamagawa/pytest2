from main import Car

def test_add_01():
    car = Car()
    assert car.car_display_price() == '10,000,000円'


def test_add_02():
    car = Car(amount=30_000_000)
    assert car.car_display_price() == '30,000,000円'