class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)


    def __str__(self):
        return f"{self.real} + {self.imag}i"

num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(4, -1)
print(num1 + num2)