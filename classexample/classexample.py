class User:
    def __init__(self, name):
        self.name = name

class Zal:
    def __init__(self, maxmest):
        self.maxmest = maxmest
        self.mesto = []
    def __add__(self, other):
        self.maxmest += other.maxmest
        self.mesto += other.mesto
    def enter(self, user):
        self.mesto.append(user)
    def check_place(self, user):
        return self.mesto.index(user)
    def exit(self, user):
        self.mesto.pop(self.mesto.index(user))


Tommy = User('Thomas Angelo')
Jo = User('Joe Barbaro')
zal1 = Zal(20)
zal1.enter(Tommy.name)
print(zal1.mesto)
zal2 = Zal(30)
zal2.enter(Jo.name)
print(zal2.mesto)
zal1 + zal2
print(zal1.maxmest)
print(zal1.mesto)
