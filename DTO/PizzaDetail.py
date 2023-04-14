class PizzaDetail:
    id =""
    pizzaId =""
    sizeId = ""
    baseId = ""
    price = ""
    quantity= ""
    def getId(self):
        return self.id
    def getQuantity(self):
        return self.quantity
    def getPrice(self):
        return self.price
    def getPizzaId(self):
        return self.pizzaId
    def getSizeId(self):
        return self.sizeId
    def getBaseId(self):
        return self.baseId
    
    def setId(self,id):
        self.id = id
    def setPrice(self,price):
        self.price = price
    def setQuantity(self,quantity):
        self.quantity = quantity
    def setPizzaId(self,pizzaId):
        self.pizzaId=pizzaId
    def setSizeId(self,sizeId):
        self.sizeId = sizeId
    def setBaseId(self,baseId):
        self.baseId = baseId