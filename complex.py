class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real}, {self.imaginary}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
    
A = Complex(1, 2)
B = Complex(3, 4)
print(567)
print(A + B)
print(A - B)
print(A * B)