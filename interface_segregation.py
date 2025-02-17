from abc import ABC, abstractmethod

class Calculation:
    @abstractmethod
    def sum(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mul(self):
        pass

    @abstractmethod
    def div(self):
        pass


class Display_result:

    @abstractmethod
    def sum_res(self):
        pass

    @abstractmethod
    def sub_res(self):
        pass

    @abstractmethod
    def mul_res(self):
        pass

    @abstractmethod
    def div_res(self):
        pass


class App(Calculation):
    res = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        App.res = self.a + self.b
        return App.res

    def sub(self):
        App.res=self.a-self.b
        return App.res

    def mul(self):
        App.res = self.a * self.b
        return App.res

    def div(self):
        App.res = self.a / self.b
        return App.res

class App_result(Display_result):

    def __init__(self,a):
        self.a=a
    def sum_res(self):
        print("Summation is ",self.a)

    def sub_res(self):
        print("Subtraction is ",self.a)

    def mul_res(self):
        print("Multiplication is ",self.a)

    def div_res(self):
        print("Division is ",self.a)

calculator = int(input("Enter the type of operation\n"
                       "0 for summation\n"
                       "1 for subtraction\n"
                       "2 for multiplication\n"
                       "3 for division\n"))
if calculator == 0:
    a = int(input("Enter first number to sum "))
    b = int(input("Enter second number to sum "))
    obj_sum = App(a,b)
    x = obj_sum.sum()

    obj_sum_display=App_result(x)
    obj_sum_display.sum_res()

elif calculator == 1:
    a = int(input("Enter first number to sub "))
    b = int(input("Enter second number to sub "))
    obj_sub = App(a, b)
    x = obj_sub.sub()

    obj_sub_display = App_result(x)
    obj_sub_display.sub_res()

elif calculator == 2:
    a = int(input("Enter first number to multiply "))
    b = int(input("Enter second number to multiply "))
    obj_mul = App(a, b)
    x = obj_mul.mul()

    obj_mul_display=App_result(x)
    obj_mul_display.mul_res()

else:
    a = int(input("Enter first number to div "))
    b = int(input("Enter second number to div "))
    obj_div = App(a, b)
    x = obj_div.div()

    obj_div_display = App_result(x)
    obj_div_display.div_res()