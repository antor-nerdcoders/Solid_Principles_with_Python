class Calculator:
    def __init__(self, a, b, ops):
        self.a = a
        self.b = b
        self.ops = ops


class Sum(Calculator):
    def display_sum(self):
        return self.a + self.b


class Sub(Calculator):
    def display_sub(self):
        return self.a - self.b


class Mul(Calculator):
    def display_mul(self):
        return self.a * self.b


class Div(Calculator):
    def display_div(self):
        return self.a / self.b

calculator = int(input("Enter the type of operation\n"
                       "0 for summation\n"
                       "1 for subtraction\n"
                       "2 for multiplication\n"
                       "3 for division\n"))
if calculator == 0:
    a = int(input("Enter first number to sum "))
    b = int(input("Enter second number to sum "))
    obj_sum = Sum(a,b,0)
    obj_sum.display_sum()


elif calculator == 1:
    a = int(input("Enter first number to sub "))
    b = int(input("Enter second number to sub "))
    obj_sub = Sub(a, b,1)
    obj_sub.display_sub()

elif calculator == 2:
    a = int(input("Enter first number to multiply "))
    b = int(input("Enter second number to multiply "))
    obj_mul = Mul(a,b,2)
    obj_mul.display_mul()
else:
    a = int(input("Enter first number to div "))
    b = int(input("Enter second number to div "))
    obj_div = Div(a, b,3)
    obj_div.display_div()