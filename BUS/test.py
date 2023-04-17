import sys
sys.path.insert(0,".")
from BUS import OrderBUS
# from DAO import StatusDAO
from DTO import *
#############
#TEST OrderBUS
orderBUS = OrderBUS()

# Chức năng hiển thị tất cả đơn hàng
orders = orderBUS.showAllOrder()
for order in orders:
    print("Mã đơn hàng:" + str(order["OrderId"]))
    ## xử lý highlight màu chữ ở giao diện tùy theo trạng thái
    if order["EndStatus"].getId() > 6:
        print("Trạng thái (CHỮ ĐỎ):" + str(order["EndStatus"].getDisplay()))
    elif order["EndStatus"].getId() < 6:
        print("Trạng thái (CHỮ VÀNG):" + str(order["EndStatus"].getDisplay()))
    else:
        print("Trạng thái (CHỮ XANH):" + str(order["EndStatus"].getDisplay()))
    print("Thời gian đặt:" + str(order["StartStatusDetail"].getTimeCreated()))
    print("Thời gian xử lý lần cuối:" + str(order["EndStatusDetail"]))
    print("Người mua:"+order["CustomerUsername"])
    print("Người xử lý:" + order["HandlerUsername"])
    print("Tổng giá:"+str(order["TotalPrice"]))
    print("Tổng số lượng:"+ str(order["Quantity"]))
    print("--------------------")

# Chức năng Xem thông tin chi tiết đơn hàng

infoOrder = orderBUS.getInfoOrder(2) # mã đơn 
print("***THÔNG TIN ĐƠN HÀNG***")
print("Họ tên khách hàng: "+ infoOrder["FullName"])
print("Địa chỉ giao hàng: "+ infoOrder["Address"])
print("Số điện thoại liên lạc: "+ infoOrder["Phone"])
print("Phương thức thanh toán: "+ infoOrder["DisplayPayment"])
print("Thời gian giao hàng: "+ infoOrder["DisplayTime"])

print("***TRẠNG THÁI ĐƠN HÀNG***")
print("Trạng thái" + "\t" * 4 + "Thời gian xử lý")
for i in range(len(infoOrder["ListStatusDetail"])):
    displayStatus = infoOrder["ListStatus"][i].getDisplay()
    if infoOrder["ListStatusDetail"][i] is not None:        
        print(displayStatus + "\t" * 4 + str(infoOrder["ListStatusDetail"][i].getTimeCreated()))
    else:
        print(displayStatus + "\t" * 4 + "Trống")

print("***CHI TIẾT ĐƠN HÀNG***")
print("Pizza" + "\t" * 4 + "Giá")
for orderDetail in infoOrder["OrderDetails"]:
    print(orderDetail["DisplayPizza"] +" x " + str(orderDetail["Quantity"]) +"\t" * 4 + str(orderDetail["Amount"]))
print("Tổng tiền:" + "\t" * 4 + str(infoOrder["Total"]))
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
