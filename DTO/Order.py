class Order:
    id = ""
    customer = ""
    handler = ""
    totalPrice = ""
    quantity = ""
    fullname =""
    address = ""
    phone = ""
    paymentType = ""
    orderType = ""
    orderTime = ""
    note = ""
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getCustomer(self):
        return self.customer
    
    def setCustomer(self, customer):
        self.customer = customer
    
    def getHandler(self):
        return self.handler
    
    def setPermission(self, handler):
        self.handler = handler

    def getTotalPrice(self):
        return self.totalPrice
    
    def setTotalPrice(self, totalPrice):
        self.totalPrice = totalPrice
    
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity):
        self.quantity = quantity
    
    def getFullname(self):
        return self.fullname
    
    def setFullname(self, fullname):
        self.fullname = fullname
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
    
    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone
    
    def getPaymentType(self):
        return self.paymentType
    
    def setPaymentType(self, paymentType):
        self.paymentType = paymentType
    
    def getOrderType(self):
        return self.orderType
    
    def setOrderType(self, orderType):
        self.orderType = orderType

    def getOrderTime(self):
        return self.OrderTime
    
    def setOrderTime(self, orderTime):
        self.orderTime = orderTime

    def getNote(self):
        return self.note
    
    def setNote(self, note):
        self.note = note