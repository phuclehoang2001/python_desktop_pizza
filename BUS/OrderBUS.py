import sys
import datetime

sys.path.insert(0,".")
from DAO import StatusDAO
from DAO import OrderDAO
from DAO import PizzaDAO
from DAO import SizeDAO
from DAO import BaseDAO
from DTO import *

## CLASS NÀY XỬ LÝ CHUNG CÁC LOGIC VỀ ĐƠN HÀNG (ORDER) VÀ TRẠNG THÁI ĐƠN HÀNG (STATUS)

class OrderBUS:
    listOrder = []
    listStatus = []
    listStatusDetail = []   

    
    def readListStatus(self):
        data = StatusDAO()
        if(self.listStatus is None):
            self.listStatus = []
        self.listStatus = data.getAllStatus()

    def readListStatusDetail(self):
        data = StatusDAO()  
        if(self.listStatusDetail is None):
            self.listStatusDetail = []
        self.listStatusDetail = data.getAllDetail()
    
    def readListOrder(self):
        data = OrderDAO()  
        if(self.listOrder is None):
            self.listOrder = []
        self.listOrder = data.getAllOrder()
    
    ## kiểm tra trạng thái hợp lệ của đơn hàng, OUTPUT là 1 thông báo (message)
    def check(self, orderId):
        message = None
        dataStatus = StatusDAO()
        dataOrder = OrderDAO()
        dataPizza = PizzaDAO()
        endStatusDetail = dataStatus.getLastStatusDetail(orderId)
        if endStatusDetail.getStatusId() == 6:
            message = "Đơn hàng đã hoàn thành"
            return message
        
        if endStatusDetail.getStatusId() == 7:
            message = "Đơn hàng đã bị hủy"
            return message
        
        ## CHECK NGUYÊN LIỆU---------
        listOrderDetail = dataOrder.getListOrderDetail(orderId)
        for orderDetail in listOrderDetail:
            pizzaDetail = dataPizza.getByPizzaDetailId(orderDetail.getPizzaDetailId())
            if pizzaDetail.getQuantity() - OrderDetail.getQuantity() < 0: 
                    message = "Đơn hàng không đủ nguyên liệu làm bánh!"
                    return message
        
        message = "Đơn hàng đủ điều kiện xử lý"
        return message

    ## xử lý tiến độ đơn hàng
    def handleOrder(self, orderId):
        message = None
        dataStatus = StatusDAO()
        dataOrder = OrderDAO()
        dataPizza = PizzaDAO()
        endStatusDetail = dataStatus.getLastStatusDetail(orderId)
        if endStatusDetail.getStatusId() == 6:
            message = "Đơn hàng đã hoàn thành"
            return message
        
        if endStatusDetail.getStatusId() == 7:
            message = "Đơn hàng đã bị hủy"
            return message
        
        listOrderDetail = dataOrder.getListOrderDetail(orderId)
        for orderDetail in listOrderDetail:
            pizzaDetail = dataPizza.getByPizzaDetailId(orderDetail.getPizzaDetailId())
            if pizzaDetail.getQuantity() - orderDetail.getQuantity() < 0: 
                    message = "Đơn hàng không đủ nguyên liệu làm bánh!"
                    return message
            
        nextStatusId = endStatusDetail.getStatusId() + 1
        for orderDetail in listOrderDetail:
            pizzaDetail = dataPizza.getByPizzaDetailId(orderDetail.getPizzaDetailId())
            quantity = orderDetail.getQuantity()
            currentQuantity = pizzaDetail.getQuantity()
            pizzaDetail.setQuantity(currentQuantity - quantity)
            dataPizza.updatePizzaDetail(pizzaDetail)

        order = dataOrder.getById(orderId)
        order.setHandler("admin")
        dataOrder.update(order)

        newStatusDetail = StatusDetail()
        newStatusDetail.setStatusId(nextStatusId)
        newStatusDetail.setOrderId(orderId)
        newStatusDetail.setTimeCreated(datetime.datetime.now())
        dataStatus.addStatusDetail(newStatusDetail)
        message = "Xử lý đơn hàng thành công!"
        return message
        

    ## xử lý hủy đơn, OUTPUT là một kết quả thông báo (message)
    def cancelOrder(self, orderId):
        message = None
        data = StatusDAO()
        detail = data.getLastStatusDetail(orderId)
        if detail.getStatusId() == 7:
            message = "Đơn hàng đã bị hủy trước đó!"
            return message
        if detail.getStatusId() >= 2:
            message = "Không thể hủy đơn hàng đã xử lý"
            return message
        
        cancelDetail = StatusDetail()
        # trang thai 7 = hủy đơn
        cancelDetail.setStatusId(7)
        cancelDetail.setOrderId(orderId)
        cancelDetail.setTimeCreated(datetime.datetime.now())
        
        data.addStatusDetail(cancelDetail)
        message = "Hủy đơn hàng thành công!"
        return message
        

    #Tìm đơn hàng theo orderId
    def findOrderById(self, orderId):
        listOrder = []
        for order in self.listOrder:
            if orderId == order.getOrderId():
                listOrder.append(order)
        return listOrder
    
    ## tìm theo ngày bắt đầu và kết thúc
    def findOrderByDate(self, startDay, endDay):
        self.readListOrder()
        statusService = StatusDAO()
        result = []
        for order in self.listOrder:
            statusDetail = statusService.getFirstStatusDetail(order.getId())
            orderTimeCreated = statusDetail.getTimeCreated()
            if orderTimeCreated >= startDay and orderTimeCreated <= endDay:
                result.append(order)
        return result        

    #Lấy chi tiết trạng thái đầu tiên (statusId = 1: Chờ xác nhận)
    def getFirstStatusDetail(self,orderId):
        data = StatusDAO()
        detailFirst = data.getStatusDetailById(orderId,1)
        return detailFirst
     
    #Lấy chi tiết trạng thái cuối cùng tùy theo orderId
    def getLastStatusDetail(self,orderId):
        data = StatusDAO()
        detailLast = data.getLastStatusDetail(orderId)
        return detailLast
    
    #Lấy trạng thái cuối cùng tùy theo orderId
    def getLastStatus(self,orderId):
        data = StatusDAO()
        statusLast = data.getByOrderId(orderId)
        return statusLast
    
    # hàm lấy tất cả đơn hàng và các thông tin của từng đơn hàng
    def showAllOrder(self):
        data = StatusDAO()
        self.readListOrder()
        result = []
        for order in self.listOrder:
            order_dict = {}
            order_dict["OrderId"] = order.getId()
            
            handler = order.getHandler() if order.getHandler() is not None else "Chưa xử lý"
            endStatusDetail =  self.getLastStatusDetail(order.getId()).getTimeCreated()\
                if self.getLastStatusDetail(order.getId()).getStatusId() != 1 else "Chưa xử lý"
            order_dict["StartStatusDetail"] = self.getFirstStatusDetail(order.getId())
            order_dict["EndStatusDetail"] = endStatusDetail
            order_dict["EndStatus"] = self.getLastStatus(order.getId())
            order_dict["CustomerUsername"] = order.getCustomer()
            order_dict["HandlerUsername"] = handler
            order_dict["TotalPrice"] = order.getTotalPrice()
            order_dict["Quantity"] = order.getQuantity()
            result.append(order_dict)
        return result
    # hàm lấy thông tin chi tiet đơn hàng
    # input là mã đơn hàng, output là một dictionary
    def getInfoOrder(self, orderId):
        infoOrder = {}
        dataStatus = StatusDAO()
        dataOrder = OrderDAO()
        dataPizza = PizzaDAO()
        dataSize = SizeDAO()
        dataBase = BaseDAO()

        order = dataOrder.getById(orderId)
        listStatusDetail = dataStatus.getListStatusDetail(orderId,7)
        listOrderDetail = dataOrder.getListOrderDetail(orderId)
        listStatus = dataStatus.getAllStatus()

        infoOrder = {}
        orderDetails = []
        
        total = 0
        for orderDetail in listOrderDetail:  
            pizzaDetail = dataPizza.getByPizzaDetailId(orderDetail.getPizzaDetailId())
            amount = orderDetail.getPrice() * orderDetail.getQuantity()
            total+=amount
            orderDetail_dict = {}
            orderDetail_dict["DisplayPizza"] = dataPizza.getById(pizzaDetail.getPizzaId()).getDisplay()
            orderDetail_dict["DisplaySize"] = dataSize.getById(pizzaDetail.getSizeId()).getDisplay()
            orderDetail_dict["DisplayBase"] = dataBase.getById(pizzaDetail.getBaseId()).getDisplay()
            orderDetail_dict["Price"] = orderDetail.getPrice()
            orderDetail_dict["Quantity"] = orderDetail.getQuantity()
            orderDetail_dict["Amount"] = amount
            orderDetails.append(orderDetail_dict)

        displayPayment = ""
        if order.getPaymentType() == 0:
            displayPayment = "Tiền mặt"
        elif order.getPaymentType() == 1:
            displayPayment = "ATM"
        elif order.getPaymentType() == 2:
            displayPayment = "Momo"
        elif order.getPaymentType() == 3:
            displayPayment = "ShoppePay"
        elif order.getPaymentType() == 4:
            displayPayment = "ZaloPay"

        displayTime = ""
        if order.getOrderType() == 0:
            displayTime = "Giao hàng ngay"
        else:
            displayTime = "Giao vào lúc " +str(order.getOrderTime())

        infoOrder["FullName"] = order.getFullname()
        infoOrder["Address"] = order.getAddress()
        infoOrder["Phone"] = order.getPhone()
        infoOrder["DisplayPayment"] = displayPayment
        infoOrder["DisplayTime"] = displayTime
        infoOrder["Note"] = order.getNote()
        infoOrder["Total"] = total
        infoOrder["ListStatusDetail"] = listStatusDetail
        infoOrder["ListStatus"] = listStatus
        infoOrder["OrderDetails"] = orderDetails
        return infoOrder


