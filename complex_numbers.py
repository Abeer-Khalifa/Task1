import math
class ComplexNumber:
    def __init__(self, number):
        self.real, self.imaginary= self.get_complex(number)
    def get_complex (self,number):
        if "+" in number:
            real, imaginary = number.split("+")
            real = float(real)
            imaginary = float(imaginary[:-1] if len(imaginary)>1 else 1)
        elif number.count("-") == 1:
            if number[0] == "-":
                real, imaginary = number.split("+")
                real = float("-"+real)
                imaginary = float(imaginary[:-1] if len(imaginary)>1 else 1)
            else:
                real, imaginary = number.split("-")
                real = float(real)
                imaginary = float("-"+imaginary[:-1] if len(imaginary)>1 else -1)
        elif number.count("-") == 2:
            real, imaginary = number[1:].split("-")
            real = float("-" + real)
            imaginary = float("-" + imaginary[:-1] if len(imaginary)>1 else -1)
        else:
            if "i" in number:
                real=0.0
                imaginary=float(number[:-1])
            else:
                real=float(number)
                imaginary=0.0
        return real,imaginary
    def __add__ (self,other):
        out_real=round(self.real+other.real,2)
        out_imaginary=round(self.imaginary+other.imaginary,2)
        return f"{out_real}{'+' if out_imaginary >= 0 else ''}{out_imaginary}i"
    def __sub__(self,other):
        out_real = round(self.real - other.real,2)
        out_imaginary = round(self.imaginary - other.imaginary,2)
        return f"{out_real}{'+' if out_imaginary >= 0 else ''}{out_imaginary}i"
    def __mul__(self,other):
        out_real=round((self.real*other.real) - (self.imaginary*other.imaginary),2)
        out_imaginary=round((self.real*other.imaginary) + (self.imaginary*other.real),2)
        return f"{out_real}{'+' if out_imaginary >= 0 else ''}{out_imaginary}i"
    def __truediv__ (self,other):
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        out_real=round((self.real*other.real + self.imaginary * other.imaginary)/denominator,2)
        out_imaginary =round((self.imaginary*other.real - self.real*other.imaginary)/denominator,2)
        return f"{out_real}{'+' if out_imaginary >= 0 else ''}{out_imaginary}i"
    def mod(self):
        return round(math.sqrt(self.real**2 + self.imaginary**2),2)

num1=input("")
A=ComplexNumber(num1)
num2=input("")
B=ComplexNumber(num2)
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A.mod())
print(B.mod())
print("\n")
