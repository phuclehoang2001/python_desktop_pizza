import sys
import datetime

sys.path.insert(0,".")
from DAO import StatusDAO
from DAO import OrderDAO
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
        data = StatusDAO()
        detail = data.getLastStatusDetail(orderId)
        if detail.getStatusId() == 6:
            message = "Đơn hàng đã hoàn thành"
            return message
        
        if detail.getStatusId() == 7:
            message = "Đơn hàng đã bị hủy"
            return message
        
        ## CHECK NGUYÊN LIỆU---------
        message = "Đơn hàng đủ điều kiện xử lý"
    

    ## xử lý tiến độ đơn hàng
    def handleOrder(self, orderId):
        pass
        

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
        cancelDetail.setStatusId(orderId)
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
    def getFirstStatusDetail(orderId):
        data = StatusDAO()
        detailFirst = data.getStatusDetailById(orderId,1)
        return detailFirst
     
    #Lấy chi tiết trạng thái cuối cùng tùy theo orderId
    def getLastStatusDetail(orderId):
        data = StatusDAO()
        detailLast = data.getLastStatusDetail(orderId)
        return detailLast
    #Lấy trạng thái cuối cùng tùy theo orderId
    def getLastStatus(orderId):
        data = StatusDAO()
        statusLast = data.getByOrderId(orderId)
        return statusLast
    
    
################
#test

# test = StatusDAO()
# list_status = test.getAllStatus()
# for status in list_status:
#      print(status.getId())
#      print(status.getDisplay())

# ##
# list_detail = test.getAllDetail()
# for detail in list_detail:
#      print(detail.getOrderId())
#      print(detail.getStatusId())
#      print(detail.getTimeCreated())
# ##
# status = Status()
# status.setId(6)
# if test.delete(status):
#     print("xóa thành công")
# else:
#     print("xóa thất bại")

##
# detail = test.getStatusDetailById(4,1)
# print(detail.getTimeCreated())
# ##
# status_findByID = test.getById(1)
# print(status_findByID.getDisplay())
##
# new_detail = StatusDetail()
# new_detail.setOrderId(3)
# new_detail.setStatusId(1)
# new_detail.setTimeCreated(datetime.datetime.now())


# if test.addStatusDetail(new_detail):
#     print("thêm trạng thái mới thành công")
# else:
#     print("thêm trạng thái mới thất bại")

## lay chi tiet trang thai nho nhat, input la ma don hang
# firstDetail = test.getFirstStatusDetail(3)
# print(firstDetail.getOrderId())
# print(firstDetail.getStatusId())
# print(firstDetail.getTimeCreated())


##  lay chi tiet trang thai lon nhat, input la ma don hang
# lastDetail = test.getLastStatusDetail(3)
# print(lastDetail.getOrderId())
# print(lastDetail.getStatusId())
# print(lastDetail.getTimeCreated())

## lay trang thai lon nhat, input la ma don hang
# status = test.getByOrderId(6)
# print(status.getId())
# print(status.getDisplay())

# get list by length
# newlist = test.getListStatusDetail(2,7)
# for detail in newlist:
#     print(detail.getOrderId())
#     print(detail.getStatusId())
#     print(detail.getTimeCreated())
