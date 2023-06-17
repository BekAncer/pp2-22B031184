class User:
    def __init__(self,name):
        self.name=name

class zal:
    def __init__(self,maxmest):
        self.maxmest=maxmest
        self.mesto=[]
    def __add__(self,other):
        self.maxmest = self.maxmest + other.maxmest
        self.mesto += other.mesto

    def enter(self,user):
        self.mesto.append(user)
    def checkplace(self,user):
        return self.mesto.index(user)
    def exit(self,user):
        self.mesto.pop(self.mesto.index(user))
