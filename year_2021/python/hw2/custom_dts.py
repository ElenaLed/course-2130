from __future__ import annotations

from typing import List, Any


class CycledList:
    """
    Реализуйте список фиксированой длины, в котором новые элементы перезаписываются
    ```
    cycled_list = CycledList(5)
    cycled_list.append(1)
    cycled_list.append(2)
    cycled_list.append(3)
    cycled_list.append(4)
    cycled_list.append(5)
    cycled_list.append(6)
    ```
    Expected Output:
    ```
    [6, 2, 3, 4, 5]
    ```
    """

    def __init__(self, size: int):
        self._data = []
        self.__size = size
        self._counter = 0
    
    def append(self, item):
        
        if len(self._data) >= self.__size:
            self._counter+=1
            self._data[(self._counter-1)%self.__size] = item
        else:
            self._data.append(item)
        pass


class Fraction:
    """
    Написать класс чисел с бесконечной точностью. Дроби.
    Определите следующие операции:
    1. a / b
    2. a + b
    3. a * b
    4. a - b
    Вы можете найти больше здесь https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
    В каждый момент времени дробь должна быть правильной
    """


    def __init__(self, nominator, denominator):
        
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        divisor = gcd(nominator, denominator)
        self.nominator = nominator//divisor
        self.denominator = denominator//divisor
        


    def __eq__(self, other: Fraction) -> bool:
        if (self.nominator==other.nominator) and (self.denominator==other.denominator):
            return True
        else:
            return False
        
        
    def __truediv__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator*other.denominator, self.denominator*other.nominator)

    def __add__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator*other.denominator+self.denominator*other.nominator, self.denominator*other.denominator)

    def __mul__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator*other.nominator, self.denominator*other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator*other.denominator-self.denominator*other.nominator, self.denominator*other.denominator)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'

    
    
    
class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter
    Достаточно поддерживать только два метода
    """

    def __init__(self, iterable):
        self._data = {x: iterable.count(x) for x in iterable}

    def append(self, item):
        if item in self._data:
            self._data[item] = self._data[item] + 1
        else:
            self._data[item] = 1
        pass

    def remove(self, item):
        del self._data[item]
        pass

class Figure:
    
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        return None

    def square(self):
        return None

    def __repr__(self):
        return f'Figure({self.name})'

class Square(Figure):
    """
    Реализуйте класс квадрат и два метода для него
    """
    def __init__(self, length, height):
        self.name = 'Square'
        self.length = length
        self.height = height
    
    def perimeter(self):
        return 2 *(self.length + self.height)

    def square(self):
        return self.length*self.height
    
    pass


class Container:
    def __init__(self, data):
        self.data = data

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, item):
        return self.data[item]

    def append(self, item):
        self.data.append(item)


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл
    Формат файла - json
    """

    import json
    
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.data = iterable
        self.path = path_to_file
        with open(path_to_file, "w+") as f:
            json.dump(iterable, f)
        pass

    def append(self, iterable: List[Any]):
        """add item to list"""
        self.data.append(iterable)
        with open(self.path, "w") as f:
            json.dump(self.data, f)
        pass

    def __getitem__(self, item):
        """ return item by index """
        return self.data[item]

    def __delite__(self, key):
        """ delete item by index
            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]
            if index lower then delete from end of list
        """
        if key >len(self.data):
            key = key % len(self.data)
            del self.data[key]

        else:
            del self.data[-(key+1)]
            
        with open(self.path, "w") as f:
            json.dump(self.data, f)    

            
    def __repr__(self):
        return f'{self.data}'