class Figure:
    def __init__(self, color, *sides):
        self.__sides = list(self.__init_sides(sides))
        self.__color = list(color)
        self.filled = True
        self.sides_count = 0

    def __init_sides(self, sides):
        count = self.sides_count
        if len(sides) != count:
            return [1] * count
        return sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        __bool = True
        for i in (r, g, b):
            if not 0 <= i <= 255 and isinstance(i, int):
                __bool = False
        return __bool

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        __bool = True
        for side in new_sides:
            if not len(new_sides) == len(self.__sides) and isinstance(side, int) and side > 0:
                __bool = False
        return __bool

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_sides()[0] > 0:
            self.__radius = self.get_sides()[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, list(self.__init_sides(sides)))

    def __init_sides(self, *sides):
        if self.__is_valid_sides():
            return sides
        else:
            return sides[0] * self.sides_count

    def __is_valid_sides(self, *new_sides):
        __is_triangle = False
        for x, y, z in new_sides:
            print(f'стороны треугольника: {x, y, z}')
            if x < y + z and y < x + z and z < x + y:
                __is_triangle = True
        return __is_triangle

    def set_sides(self, *new_sides):
        if self.__is_valid_sides():
            super().set_sides(*new_sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *[side] * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((251, 33, 133), 5, 3, 4)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'Круг, цвет:{circle1.get_color()}')
cube1.set_color(300, 70, 15)  # Не изменится
print(f'Куб, цвет:{cube1.get_color()}')
triangle1.set_color(255, 255, 255)
print(f'Треугольник, цвет:{triangle1.get_color()}')

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(f'Куб, стороны:{cube1.get_sides()}')
circle1.set_sides(15)  # Изменится
print(f'Круг, длина окружности:{circle1.get_sides()}')
triangle1.set_sides(5, 5, 12)  # Невозможный треугольник
print(f'Треугольник, стороны:{triangle1.get_sides()}')

# Проверка периметра (круга), это и есть длина:
print(f'Круг, периметр:{len(circle1)}')

# Проверка объёма (куба):
print(f'Куб, объем:{cube1.get_volume()}')

# Проверка площади треугольника
print(f'Треугольник, площадь{triangle1.get_square()}')
