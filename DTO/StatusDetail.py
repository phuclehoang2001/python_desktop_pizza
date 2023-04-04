class StatusDetail:
    orderId = "" 
    statusId = ""
    timeCreated = ""
    
    def getStatusId(self):
        return self.status_id
    
    def getOrderId(self):
        return self.order_id
    
    def getTimeCreated(self):
        return self.time_created
    
    def setStatusId(self, statusId):
        self.statusId = statusId

    def setOrderId(self, orderId):
        self.orderId = orderId
    
    def setTimeCreated(self, timeCreated):
        self.timeCreated = timeCreated
    
    
    
    
    
    