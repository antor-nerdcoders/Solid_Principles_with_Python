class Calculator:
    sum = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Ops(self):
        pass


class Sum(Calculator):
    def Ops(self):
        Calculator.sum = self.a + self.b
        return Calculator.sum


class Sub(Calculator):
    def Ops(self):
        Calculator.sum = self.a - self.b
        return Calculator.sum


class Mul(Calculator):
    def Ops(self):
        Calculator.sum = self.a * self.b
        return Calculator.sum


class Div(Calculator):
    def Ops(self):
        Calculator.sum = self.a / self.b
        return Calculator.sum

calculator = int(input("Enter the type of operation\n"
                       "0 for summation\n"
                       "1 for subtraction\n"
                       "2 for multiplication\n"
                       "3 for division\n"))
if calculator == 0:
    a = int(input("Enter first number to sum "))
    b = int(input("Enter second number to sum "))
    obj_sum = Sum(a, b)
    x = obj_sum.Ops()
    print("The Summation is ", x)

elif calculator == 1:
    a = int(input("Enter first number to sub "))
    b = int(input("Enter second number to sub "))
    obj_sub = Sub(a, b)
    x = obj_sub.Ops()
    print("The Subtraction is ", x)

elif calculator == 2:
    a = int(input("Enter first number to multiply "))
    b = int(input("Enter second number to multiply "))
    obj_mul = Mul(a, b)
    x = obj_mul.Ops()
    print("The Multiplication is ", x)
else:
    a = int(input("Enter first number to div "))
    b = int(input("Enter second number to div "))
    obj_div = Div(a, b)
    x = obj_div.Ops()
    print("The Division is ", x)
