class OderDetail:
    id =""
    order_id= ""
    pizza_detail_id= ""
    price = ""
    quantity= ""
    
    def getId(self):
        return self.id
    def getOrderId(self):
        return self.order_id
    def getPizzaDetailId(self):
        return self.pizza_detail_id
    def getPrice(self):
        return self.price
    def getQuantity(self):
        return self.quantity
    
    def setId(self,id):
        self.id = id
    def setOderId(self,order_id):
        self.oder_id = order_id
    def setPizzaDetailId(self,pizza_detail_id):
        self.pizza_detail_id = pizza_detail_id
    def setPrice(self,price):
        self.price = price
    def setQuantity(self,quantity):
        self.quantity = quantity