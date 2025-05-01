class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def __str__(self):
        return f'{self.a}, {self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)