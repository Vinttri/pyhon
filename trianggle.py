import math
from typing import Self

class Point:
    """класс точка на вход координаты x,y и цвет
    
    Атрибуты:
        x,y- координаты
        color- цвет, строка
    """
    def __init__(self, x:int|float, y:int|float, color:str=""):
        self.x = x
        self.y = y
        self.color = color
    def distance(self, other_point: Self) -> float:
        """Расчёт расстояния от данной точки до другой параметр точка класса Point"""
        return math.sqrt(math.pow(self.x-other_point.x,2)+math.pow(self.y-other_point.y,2))

class Triangle:
     """класс треугольник конструктор принимает три точки класса point
     
     Атрибуты:
        area-площадь треугольника
        perimeter-периметр треугольника
     """
     def __init__(self,p1:Point,p2:Point,p3:Point):
        self.a=p1.distance(p2)
        self.b=p2.distance(p3)
        self.c=p3.distance(p1)
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.calc_perimeter()
        self.calc_area()
     def calc_perimeter(self):
        """посчитать периметр"""
        self.perimeter=self.a+self.b+self.c
     def calc_area(self):
        """посчитать площадь"""
        self.area=math.sqrt(self.perimeter/2 * (self.perimeter/2-self.a) * (self.perimeter/2-self.b) * (self.perimeter/2-self.c))


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

# TODO: your code here...

#делим список на треугольнки
triangle_red_points=[]
triangle_green_points=[]
for point in points:
    if point.color=='red':
            triangle_red_points.append(point)
    if point.color=='green':
            triangle_green_points.append(point)
#coздаем объекты
triangle_red=Triangle(triangle_red_points[0],triangle_red_points[1],triangle_red_points[2])
triangle_green=Triangle(triangle_green_points[0],triangle_green_points[1],triangle_green_points[2])

#result
print("Площадь красного треугольника = ", triangle_red.area)
print("Площадь зеленого треугольника = ", triangle_green.area)