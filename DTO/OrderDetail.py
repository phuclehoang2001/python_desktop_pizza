class OderDetail:
    id =""
    orderId= ""
    pizzaDetailId= ""
    price = ""
    quantity= ""
    
    def getId(self):
        return self.id
    def getOrderId(self):
        return self.orderId
    def getPizzaDetailId(self):
        return self.pizzaDetailId
    def getPrice(self):
        return self.price
    def getQuantity(self):
        return self.quantity
    
    def setId(self,id):
        self.id = id
    def setOderId(self,orderId):
        self.oder_id = orderId
    def setPizzaDetailId(self,pizzaDetailId):
        self.pizzaDetailId = pizzaDetailId
    def setPrice(self,price):
        self.price = price
    def setQuantity(self,quantity):
        self.quantity = quantity