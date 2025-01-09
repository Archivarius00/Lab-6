#heh

class Figure:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self):
        Valuee = self.a * self.b * self.c
        return Valuee

class Empty(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def Value_of_emptyfigure(self):
        V = Figure.value(self) - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
        return V

class Mas_figures(Figure):
    def __init__(self, a, b, c, count_shapes):
        super().__init__(a, b, c)
        self.count_shapes = count_shapes

    def sum_values(self):
        ans = Figure.value(self) * self.count_shapes
        return ans


# Пример:
if __name__ == "__main__":
    kub = Empty(10, 2, 7, 1)
    sphere = Mas_figures(10, 2, 5, 5)
    print(f"Объём куба:  {kub.value()}")
    print(f"Объём куба с внутренней полостью: {kub.Value_of_emptyfigure()}"'\n')
    print(f"Объём {sphere.count_shapes} фигур: {sphere.sum_values()}")
