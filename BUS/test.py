import sys
sys.path.insert(0,".")
from BUS import OrderBUS, GroupBUS, UserBUS
# from DAO import StatusDAO
from DTO import *


#############
# TEST UserBUS
userBUS = UserBUS()
userBUS.readListUser()
for user in userBUS.listUser:
    print("Tên tài khoản:" + user.getUsername())
    print("Nhóm tài khoản:" + userBUS.getGroupName(user))
    if userBUS.hasPermission(user.getUsername(),"lock"):
        print("Đã khóa")
    else:
        print("Chưa khóa")
print("--------------------------------")

#TÌM THEO USERNAME
# username_find = "adm"
# result = userBUS.findUserByUsername(username_find) 
# for item in result:
#     print(item.getUsername())

#XEM THÔNG TIN TÀI KHOẢN
# username = "admin"
# infoUser = userBUS.showInfo(username)
# print("Tên tài khoản: " + infoUser["username"])
# print("Nhóm tài khoản: " + infoUser["groupName"])
# print("Họ tên: " + infoUser["fullname"])
# print("Ngày sinh: " + str(infoUser["birthday"]))
# print("Địa chỉ: " + infoUser["address"])
# print("Số điện thoại: " + infoUser["phone"])
# print("Email: " + infoUser["email"])
#################



#THÊM USER MỚI
## khi thêm bắt buộc phải có username, groupId, password
## các thông tin còn lại có thể bỏ trống
# nv_new = User()
# nv_new.setUsername("nhanvien2")
# nv_new.setGroupId(3) 
# password = "tung@gmail.com"
# if userBUS.addUser(nv_new, password):
#     print("Thêm thành công")
# else:
#     print("Thêm thất bại")




#CẬP NHẬT THÔNG TIN
## Tạo 1 UserDTO và lấy thông tin người dùng nhập vào
## bat buoc phai co username, groupId
## các thông tin còn lại có thể bỏ trống hoặc điền mới
# user_update = User()
# user_update.setFullname("Thanh Tùng")
# user_update.setGroupId(3)
# user_update.setUsername("admin") 
# # Đối với trường hợp cập nhật password thì như sau:
# #+ Với username = admin ( trường hợp đặc biệt ) thì chỉ khi đăng nhập đúng vào tài khoản username = admin mới có thể đổi mật khẩu
# password = "abc1234" #lấy từ ô text
# re_password = "abc1234" #lấy từ ô text
# accept = True
# if user_update.getUsername() == "admin": # user đang chọn để đổi mật khẩu là admin
#     current_user = "admin2" ## lấy ở username khi login, giả sử current_user là admin
#     if current_user == "admin":
#         pass
#     else:
#         accept = False

# if accept:   
#     #+ kiểm tra password  và password nhập lần 2  có khớp nhau không
#     # khi password nhập vào khác rỗng thì thực hiện đổi mk
#     if len(password) != 0:
#         if password == re_password:
#             if not userBUS.updatePassword(user_update.getUsername(), password):
#                 print("Sửa mật khẩu thất bại")
#             else:
#                 print("Sửa mật khẩu thành công")
#         else:
#             print("Vui lòng nhập lại đúng mật khẩu, sửa mật khẩu thất bại")
#     ### cập nhật các thông tin khác
#     if userBUS.updateUser(user_update):
#         print("Cập nhật thành công")
#     else:
#         print("Cập nhật thất bại")
# else:
#     print("Không thể đổi thông tin của username là admin")




#KIỂM TRA TÀI KHOẢN CÓ BỊ KHÓA KHÔNG VÀ THỰC HIỆN KHÓA HOẶC MỞ KHÓA
# username = "nhanvien2" ## lấy username ở dòng được chọn
# if(username =="admin"): ## không thể khóa tài khoản username = admin (tài khoản đặc biệt)
#    print("Không thể khóa tài khoản có username là admin")
# else:
#     check_lock = userBUS.hasPermission(username,"lock")
#     if check_lock:
#         print("Tài khoản đã khóa, xác nhận mở khóa?")
#         userBUS.unclockUser(username) ## hàm mở khóa
#     else:
#         print("Tài khoản chưa khóa, xác nhận khóa tài khoản")
#         userBUS.clockUser(username) ## hàm khóa 




## BỎ CHỨC NĂNG XÓA TÀI KHOẢN
## BỎ CHỨC NĂNG THÊM NHÓM QUYỀN TRONG QUẢN LÝ NHÓM
## Set quyền cho User
## bấm chọn vào quyền trong drop down box -> lấy được groupId
## chỉ có 2 nhóm quyền là nhân viên (groupId = 3) và admin(groupId = 4) 

# groupId = 3 
# username = "nhanvien1"
# if userBUS.updatePermissionGroup(username, groupId):
#     print("Cập nhật quyền thành công")
# else:
#     print("Cập nhật quyền thất bại")


################################TEST LOGIN



#############
#TEST GroupBUS
# groupBUS = GroupBUS()
### chỉ hiển thị 2 nhóm qtv và nhân viên
# groupBUS.readListGroup()
# for item in groupBUS.listGroup:
#     print(item.getDisplay())

# permission_dict = {
#     "admin.login": "Đăng nhập trang quản trị",
#     "admin.group": "Quản lý nhóm tài khoản",
#     "admin.user": "Quản lý tài khoản",
#     "admin.category": "Quản lý danh mục bánh",
#     "admin.topping": "Quản lý nhân bánh",
#     "admin.size": "Quản lý kích thước bánh",
#     "admin.base": "Quản lý đế bánh",
#     "admin.pizza": "Quản lý bánh pizza",
#     "admin.order": "Quản lý đơn hàng",
#     "admin.statistic": "Thống kê báo cáo"
# }

## Chức năng hiển thị quyền
#chọn 1 nhóm từ danh sách => lấy groupId của nó, giả sử groupId = 4
# groupId = 3
# for key, value in permission_dict.items():
#     print(value)
#     if groupBUS.isSet(groupId, key):
#         if groupBUS.hasPermission(groupId, key):
#             print("Quyền đã mở") #check vào radio box 
#         else:
#             print("Quyền bị khóa")
#     else:
#         print("Chưa phân quyền") # bỏ check radio box
#     print("---------------")

## Chức năng thiết lập quyền khi nhấn chọn các quyền và đồng ý
# groupId = 3
# for key, value in permission_dict.items():
#     value = 0 ## bắt sự kiện nhấn vào radio box, khi nhấn có sẽ là 1, không là 0 
#     if groupBUS.setPermission(groupId, key,value):
#         print("Phân quyền thành công") 
#     else:
#         print("Phân quyền thất bại") 
#     print("---------------")






######################### TEST UserBUS
# userBUS = UserBUS()
## chỉ hiển thị user thuộc 2 nhóm admin (qtv) và nhân viên
# userBUS.readListUser()
# for item in userBUS.listUser:
#     print(item.getFullname())












#############
#TEST OrderBUS
# orderBUS = OrderBUS()

# Chức năng hiển thị tất cả đơn hàng
# orders = orderBUS.showAllOrder()
# for order in orders:
#     print("Mã đơn hàng:" + str(order["OrderId"]))
#     ## xử lý highlight màu chữ ở giao diện tùy theo trạng thái
#     if order["EndStatus"].getId() > 6:
#         print("Trạng thái (CHỮ ĐỎ):" + str(order["EndStatus"].getDisplay()))
#     elif order["EndStatus"].getId() < 6:
#         print("Trạng thái (CHỮ VÀNG):" + str(order["EndStatus"].getDisplay()))
#     else:
#         print("Trạng thái (CHỮ XANH):" + str(order["EndStatus"].getDisplay()))
#     print("Thời gian đặt:" + str(order["StartStatusDetail"].getTimeCreated()))
#     print("Thời gian xử lý lần cuối:" + str(order["EndStatusDetail"]))
#     print("Người mua:"+order["CustomerUsername"])
#     print("Người xử lý:" + order["HandlerUsername"])
#     print("Tổng giá:"+str(order["TotalPrice"]))
#     print("Tổng số lượng:"+ str(order["Quantity"]))
#     print("--------------------")

# Chức năng Xem thông tin chi tiết đơn hàng

# infoOrder = orderBUS.getInfoOrder(2) # mã đơn 
# print("***THÔNG TIN ĐƠN HÀNG***")
# print("Họ tên khách hàng: "+ infoOrder["FullName"])
# print("Địa chỉ giao hàng: "+ infoOrder["Address"])
# print("Số điện thoại liên lạc: "+ infoOrder["Phone"])
# print("Phương thức thanh toán: "+ infoOrder["DisplayPayment"])
# print("Thời gian giao hàng: "+ infoOrder["DisplayTime"])

# print("***TRẠNG THÁI ĐƠN HÀNG***")
# print("Trạng thái" + "\t" * 4 + "Thời gian xử lý")
# for i in range(len(infoOrder["ListStatusDetail"])):
#     displayStatus = infoOrder["ListStatus"][i].getDisplay()
#     if infoOrder["ListStatusDetail"][i] is not None:        
#         print(displayStatus + "\t" * 4 + str(infoOrder["ListStatusDetail"][i].getTimeCreated()))
#     else:
#         print(displayStatus + "\t" * 4 + "Trống")

# print("***CHI TIẾT ĐƠN HÀNG***")
# print("Pizza" + "\t" * 4 + "Giá")
# for orderDetail in infoOrder["OrderDetails"]:
#     print(orderDetail["DisplayPizza"] +" x " + str(orderDetail["Quantity"]) +"\t" * 4 + str(orderDetail["Amount"]))
# print("Tổng tiền:" + "\t" * 4 + str(infoOrder["Total"]))
################
#test

# print(orderBUS.cancelOrder(9))


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
