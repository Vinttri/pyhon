import math as math

class Point:
    """класс точка 
    
        num - ид точки,
        x,y - координаты точки


    """
    #порядковый номер точки
    num = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.num=Point.num+1       
        self.num=Point.num

    #перегрузки для сортировки
    def __lt__(self, other):
        return self.x < other.x
    def __le__(self, other):
        return self.x <= other.x
    def __eq__(self, other):
        return self.x == other.x
    def __ne__(self, other):
        return self.x != other.x
    def __gt__(self, other):
        return self.x > other.x
    def __ge__(self, other):
        return self.x >= other.x    
    
    def distance(self:'Point',p:'Point')->float:
        """Поиск расстояния между точками, на вход: точку класса Point"""
        return math.sqrt(math.pow(self.x-p.x,2)+math.pow(self.y-p.y,2))
    def get_point_str(self)->str:
        """Вернуть координаты точки - строка"""
        return F"точка {self.num}: x={self.x},y={self.y}"
    def print(self):
        """Распечатать координаты точки"""
        print (self.get_point_str())

class Line:
    """класс линия
    
        num - ид линии,
        length - длина линии
    """
    #порядковый номер
    num=0
    length=0.0
    def __init__(self, points=[]):
        self.points=points
        Line.num+=1
        self.point_cnt=len(points)  
        self.calk_length()
    def append(self,p: Point):
        """добавить точку в линию, на вход: точку класса Point"""
        self.points.append(p)
        self.point_cnt=self.point_cnt+1
        self.calk_length()
    def print(self):
        """распечатать линию по точкам"""
        print(F"линия {self.num} длиной {self.length} состоит из {self.point_cnt} следующих точек:")
        for point in self.points:
            point.print()
    def calk_length(self):
        """расчёт длины линии - сохраянется в свойстве length"""
        #сортируем точки по Х координате
        self.points.sort()
        #Суммируем расстояния между соседними точками
        for i,point in enumerate(self.points):
            if i != 0:
                self.length=self.length+prv_point.distance(point)
            prv_point=point
    def get_point_max_distace_from(self,point2:Point)->Point:
        """максимальное расстояние точки линии от заданой точки"""
        distace_max=0
        point_max_distance=self.points[0]
        for point in self.points:
           range_from=point.distance(point2)
           if range_from>distace_max:
                distace_max=range_from
                point_max_distance=point
        return point_max_distance
    

#входные данные оригинал    
#points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

#добавляем точки на линию
Line1 = Line([Point(2, 4), Point(7, 5), Point(5, -2)])
Line1.append(Point(0, 6))
Point1=Point(-12, 0)
Line1.append(Point1)

#Выводим расчёты
#информация о линии
Line1.print()
#отдельно выведем длину - по условию задачи
print("длина линии:",Line1.length)
#самая удалённая точка
print("Самая удалённая точка от 0,0:",Line1.get_point_max_distace_from(Point(0,0)).get_point_str())


