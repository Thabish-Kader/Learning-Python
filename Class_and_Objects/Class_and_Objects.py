class CountFromBy:
    def increase(self) -> int:
        self.val = + self.inc
        return self


# creating an object
a = CountFromBy()
b = CountFromBy()
c = CountFromBy()

print(b)


# useing construtors in python with the help of __init__

class CountFromBy_v2:
    #  version 1
    #  def __init__(self, v: int, i: int) -> None:
    #     self.val = v
    #     self.incr = i

    # version 2 with default values
    def __init__(self, v : int=0, i: int=1) -> None:
        self.val = v
        self.incr = i


    def increase(self) -> None:
        self.val += self.incr

    # working with __repr__ method
    def __repr__(self) -> str:
        return str(self.val)


g = CountFromBy_v2(110, 10)
print(g.val)
g.increase()
print(g.val)

i = CountFromBy_v2()
print(i.val)

k = CountFromBy_v2()
print(k)
k.increase()
print(k)

k = CountFromBy_v2(100)
print(k.val)