class Summation:
    sum = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_sum(self):
        Summation.sum = self.a + self.b


class Subtraction:
    sub = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_sub(self):
        Subtraction.sub = self.a - self.b


class Multiplication:
    mul = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_mul(self):
        Multiplication.mul = self.a * self.b

class Division:
    div = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_div(self):
        Division.div = self.a / self.b

class display_sum(Summation):
    def display(self):
        print("The summation is ",Summation.sum)

class display_sub(Subtraction):
    def display(self):
        print("The Subtraction is ",Subtraction.sub)

class display_mul(Multiplication):
    def display(self):
        print("The Multiplication is ",Multiplication.mul)

class display_div(Division):
    def display(self):
        print("The Division is ",Division.div)


calculator = int(input("Enter the type of operation\n"
                       "0 for summation\n"
                       "1 for subtraction\n"
                       "2 for multiplication\n"
                       "3 for division\n"))
if calculator == 0:
    a = int(input("Enter first number to sum "))
    b = int(input("Enter second number to sum "))
    obj_sum = display_sum(a,b)
    obj_sum.calc_sum()
    obj_sum.display()

elif calculator == 1:
    a = int(input("Enter first number to sub "))
    b = int(input("Enter second number to sub "))
    obj_sub = display_sub(a, b)
    obj_sub.calc_sub()
    obj_sub.display()

elif calculator == 2:
    a = int(input("Enter first number to multiply "))
    b = int(input("Enter second number to multiply "))
    obj_mul = display_mul(a, b)
    obj_mul.calc_mul()
    obj_mul.display()
else:
    a = int(input("Enter first number to div "))
    b = int(input("Enter second number to div "))
    obj_div = display_div(a, b)
    obj_div.calc_div()
    obj_div.display()