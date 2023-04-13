class PizzaDetail:
    id =""
    pizza_id =""
    size_id = ""
    base_id = ""
    price = ""
    quantity= ""
    def getId(self):
        return self.id
    def getQuantity(self):
        return self.quantity
    def getPrice(self):
        return self.price
    def getPizzaId(self):
        return self.pizza_id
    def getSizeId(self):
        return self.size_id
    def getBaseId(self):
        return self.base_id
    
    def setId(self,id):
        self.id = id
    def setPrice(self,price):
        self.price = price
    def setQuantity(self,quantity):
        self.quantity = quantity
    def setPizzaId(self,pizza_id):
        self.pizza_id=pizza_id
    def setSizeId(self,size_id):
        self.size_id = size_id
    def setBaseId(self,base_id):
        self.base_id = base_id