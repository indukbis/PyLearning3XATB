class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

print(Calc(5,9).sum())
print(Calc(5,9).sub())
print(Calc(5,9).mul())
print(Calc(5,9).div())


