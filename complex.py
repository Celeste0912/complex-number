class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)