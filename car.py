"""
## Автомобили
Описать класс Car
``` python
class Car:
  ...

# Значит должны быть значения по умолчанию
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_100km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то бак заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива)
```
выведет сообщение "проехали ... километров",
в результате поездки потратится бензин и увеличится пробег.
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""

class Car:
    """класс автомобиль"""
    def __init__(self,model:str='Noname',gas:int=100,capacity:int=100,gas_per_100km:int=10,mileage:int=0):
        self.model=model
        self.gas=gas
        self.capacity=capacity
        self.gas_per_100km=gas_per_100km
        self.milage=mileage
        self.calc_milage_to_tank()
    def calc_milage_to_tank(self):
        self.milage_to_tank=int(self.gas_per_100km*self.gas)
    def fill(self, litters:int):
        if self.gas+litters > self.capacity:
            self.gas=self.capacity
        else:
            self.gas+=litters
        self.calc_milage_to_tank()
    def ride(self,kilometers:int):
        if kilometers>=self.milage_to_tank:
            self.gas=0
            self.milage+=self.milage_to_tank
            print(f'car have ride {self.milage_to_tank}km and tank is over please fill {kilometers-self.milage_to_tank}km into tank toa achive')
            self.milage_to_tank=0
        else:
            self.gas-=int(kilometers*self.gas_per_100km/100)
            self.milage+=kilometers
            self.calc_milage_to_tank()
            print(f'car have ride {kilometers}km')
    def info(self):
        print(f"Car model {self.model} has {self.gas}L in tank and milage {self.milage} and can ride {self.milage_to_tank}km on this tank")



car=Car('BMW X5')
car.info()
car.ride(10)
car.info()
car.ride(900)
car.info()
car.ride(100)

car.fill(10)
car.info()
car.ride(10)
