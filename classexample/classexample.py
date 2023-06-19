class User:
    def __init__(self,name):
        self.name=name

class Zal:
    def __init__(self, maxmest, mesto = []):
        self.maxmest = maxmest
        self.mesto = mesto
    def __add__(self, other):
        return Zal(self.maxmest + other.maxmest,self.mesto + other.mesto)
    def __iadd__(self, other):
        self.maxmest += other.maxmest
        self.mesto += other.mesto
        return self
    def enter(self, user):
        self.mesto= self.mesto + [user]
    def check_place(self, user):
        return self.mesto.index(user)
    def exit(self, user):
        self.mesto.pop(self.mesto.index(user))


Tommy = User('Thomas Angelo')
Jo = User('Joe Barbaro')

zal1 = Zal(20)
zal1.enter(Tommy)
print(zal1.mesto)


zal2 = Zal(30)
zal2.enter(Jo)
print(zal2.mesto)


zal1 = zal1 + zal2
print(zal1.maxmest)
print(zal1.mesto)


Clemente = User('Alberto Clemente')
zal3 = Zal(40)
zal3.enter(Clemente)
zal3 += zal2
print(zal3.check_place(Clemente))
