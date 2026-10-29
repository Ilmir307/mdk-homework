class product:
    def __init__(self,Name,Price):
        self.Name=Name
        self.Price=Price

    def getPrice(self):
        return self.Price

def Calc_total(items):
    total=0
    for i in items:
        total=total+i.getPrice()
    unused_variable = 5
    return total

MyList = [product("Хлеб",50),product("Молоко",80)]
print("Итого: " + str(Calc_total(MyList)))
