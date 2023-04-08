import sys
import datetime

sys.path.insert(0,".")
from DAO import StatusDAO
from DTO import *

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
    
    ## kiểm tra trạng thái hợp lệ của đơn hàng
    def check(self, orderId):
        result = None
        data = StatusDAO()
        detail = data.getLastStatusDetail(orderId)
        if detail.getStatusId() == 6:
            result = "Đơn hàng đã hoàn thành"
            return result
        
        if detail.getStatusId() == 7:
            result = "Đơn hàng đã bị hủy"
            return result
        
        ## CHECK NGUYÊN LIỆU---------

        result = "Đơn hàng đủ điều kiện xử lý"
    

    ## xử lý đơn hàng
    def handleOrder(self, orderId):
        pass
        

    ## hủy đơn
    def cancelOrder(self, orderId):
        result = None
        data = StatusDAO()
        detail = data.getLastStatusDetail(orderId)
        if detail.getStatusId() == 7:
            result = "Đơn hàng đã bị hủy trước đó!"
            return result
        if detail.getStatusId() >= 2:
            result = "Không thể hủy đơn hàng đã xử lý"
            return result
        
        cancelDetail = StatusDetail()
        # trang thai 7 = hủy đơn
        cancelDetail.setStatusId(7)
        cancelDetail.setStatusId(orderId)
        cancelDetail.setTimeCreated(datetime.datetime.now())
        
        data.addStatusDetail(cancelDetail)
        result = "Hủy đơn hàng thành công!"
        return result
        

    def findOrderById(self, orderId):
        listOrder = []
        for order in self.listOrder:
            if orderId == order.getOrderId():
                listOrder.append(order)
        return listOrder
    
    ## tìm theo ngày
    def findOrderByDate(self, startDate, endDate):

        pass

    def getFirstStatusDetail(orderId):
        data = StatusDAO()
        detailFirst = data.getStatusDetailById(orderId,1)
        return detailFirst
     
    def getLastStatusDetail(orderId):
        data = StatusDAO()
        detailLast = data.getLastStatusDetail(orderId)
        return detailLast

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
