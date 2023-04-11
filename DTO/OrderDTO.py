class OrderDTO:
    id = ""
    customer = ""
    handler = ""
    total_price = ""
    quantity = ""
    fullname = ""
    address = ""
    phone = ""
    payment_type = ""
    order_type = ""
    order_time = ""
    note = ""

    def getId(self):
        return self.id
    def getCustomer(self):
        return self.customer
    def getHandler (self):
        return self.handler
    def getTotalPrice(self):
        return self.total_price
    def getQuantity(self):
        return self.quantity
    def getFullname(self):
        return self.fullname
    def getAddress(self):
        return self.address
    def getPhone(self):
        return self.phone
    def getPaymentType(self):
        return self.payment_type
    def getOrderType(self):
        return self.order_type
    def getOrderTime(self):
        return self.order_time
    def getNote(self):
        return self.note
    
    def setId(self,id):
        self.id = id
    def setCustomer(self,customer):
        self.customer = customer
    def setHandler(self,handler):
        self.handler = handler
    def setTotalPrice(self,total_price):
        self.total_price = total_price
    def setQuantity(self,quantity):
        self.quantity = quantity
    def setFullname(self,fullname):
        self.fullname = fullname
    def setAddress(self,address):
        self.address = address
    def setPhone(self,phone):
        self.phone = phone
    def setPaymentType(self,payment_type):
        self.payment_type = payment_type
    def setOrderType(self,oder_type):
        self.order_type = oder_type
    def setOrderTime(self,order_time):
        self.order_time = order_time
    def setNote(self,note):
        self.note = note