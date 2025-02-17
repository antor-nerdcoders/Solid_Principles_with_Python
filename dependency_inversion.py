from abc import ABC, abstractmethod


class App:
    def __init__(self, a, b, ops):
        self.a = a
        self.b = b
        self.ops = ops

    def init_app(self):
        obj = Calculation()
        if self.ops == 0:
            return obj.sum(self.a, self.b)
        elif self.ops == 1:
            return obj.sub(self.a, self.b)
        elif self.ops == 2:
            return obj.mul(self.a, self.b)
        else:
            return obj.div(self.a, self.b)


class CalculatorInterface(ABC):
    @abstractmethod
    def sum(self, a, b):
        pass

    @abstractmethod
    def sub(self, a, b):
        pass

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def div(self, a, b):
        pass


class Calculation(CalculatorInterface):
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calculator = int(input("Enter the type of operation\n"
                       "0 for summation\n"
                       "1 for subtraction\n"
                       "2 for multiplication\n"
                       "3 for division\n"))
if calculator == 0:
    a = int(input("Enter first number to sum "))
    b = int(input("Enter second number to sum "))
    obj_sum = App(a, b, 0)
    x = obj_sum.init_app()

    print("The Summation is ", x)

elif calculator == 1:
    a = int(input("Enter first number to sub "))
    b = int(input("Enter second number to sub "))
    obj_sub = App(a, b, 1)
    x = obj_sub.init_app()
    print("The Subtraction is ", x)

elif calculator == 2:
    a = int(input("Enter first number to multiply "))
    b = int(input("Enter second number to multiply "))
    obj_mul = App(a, b, 2)
    x = obj_mul.init_app()
    print("The Multiplication is ", x)

else:
    a = int(input("Enter first number to div "))
    b = int(input("Enter second number to div "))
    obj_div = App(a, b, 3)
    x = obj_div.init_app()
    print("The Multiplication is ", x)
