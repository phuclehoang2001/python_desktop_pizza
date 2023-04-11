class StatusDetailDTO:
    order_id = ""
    status_id = ""
    time_created = ""

    def getOrderId(self):
        return self.order_id
    def getStatusId(self):
        return self.status_id
    def getTimeCreated(self):
        return self.time_created
    
    def setOrderId(self,order_id):
        self.order_id = order_id
    def setStatusId(self,status_id):
        self.status_id = status_id
    def setTimeCreated(self,time_created):
        self.time_created = time_created