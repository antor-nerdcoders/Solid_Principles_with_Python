class Summation:
    sum = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        Summation.sum = self.a + self.b
        return Summation.sum


class Subtraction:
    sub = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        Subtraction.sub = self.a - self.b
        return Subtraction.sub


class Multiplication:
    mul = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        Multiplication.mul = self.a * self.b
        return Multiplication.mul


class Division:
    div = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        Division.div = self.a / self.b
        return Division.div


calculator = int(input("Enter the type of operation\n"
                       "0 for summation\n"
                       "1 for subtraction\n"
                       "2 for multiplication\n"
                       "3 for division\n"))
if calculator == 0:
    a = int(input("Enter first number to sum "))
    b = int(input("Enter second number to sum "))
    obj_sum = Summation(a, b)
    x = obj_sum.calc()
    print("The Summation is ", x)

elif calculator == 1:
    a = int(input("Enter first number to sub "))
    b = int(input("Enter second number to sub "))
    obj_sub = Subtraction(a, b)
    x = obj_sub.calc()
    print("The Subtraction is ", x)

elif calculator == 2:
    a = int(input("Enter first number to multiply "))
    b = int(input("Enter second number to multiply "))
    obj_mul = Multiplication(a, b)
    x = obj_mul.calc()
    print("The Multiplication is ", x)
else:
    a = int(input("Enter first number to div "))
    b = int(input("Enter second number to div "))
    obj_div = Division(a, b)
    x = obj_div.calc()
    print("The Division is ", x)