class Calc:
    def sum(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

object_ref = Calc()
output = object_ref.sum(3,5)
print(output)
output = object_ref.sub(3,5)
print(output)
output = object_ref.mul(3,5)
print(output)
output = object_ref.div(3,5)
print(output)