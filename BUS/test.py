import sys
import datetime
sys.path.insert(0,".")
from BUS import OrderBUS, GroupBUS, UserBUS, StatisticBUS, PizzaBUS
# from DAO import StatusDAO
from DTO import *

##TEST TOPPING
pizzaBUS = PizzaBUS()
pizzaBUS.readListTopping()
name = "Thịt"
find_topping = pizzaBUS.findToppingByName(name)
for item in find_topping:
    print(item.getId())
    print(item.getDisplay())


##TEST QUẢN LÝ BÁNH PIZZA
# pizzaBUS = PizzaBUS()
##Thêm pizza
## Bước 1: xử lý file ảnh
## + kiếm tra kiểm tra kích thước file ảnh thấp hơn 2mb
## + kiểm tra định dạng tệp tin đã tải lên: allowed_types = ["jpg", "png"]
## + kiếm tra ảnh đã chọn có trùng với ảnh trong /GUI/images không? nếu có thì báo "Đã tồn tại file trong hệ thống, không thể ghi đè file!"
## + nếu các điều kiện trên hợp lệ: thực hiện di chuyển file ảnh đã được tải lên vào /GUI/images (có thể sử dụng module shutil của python)

## Bước 2: thực hiện thêm dữ liệu vào CSDL
## sau khi chọn các nhân bánh, kích thước, đế ta có 1 ví dụ cấu trúc dictionary như sau:
# info = {}
# info["PizzaName"] = "Pizza mới"
# info["CategoryId"]= 1
# info["Description"] =" test tạo bánh mới "
# info["Image"] ="newpizza.png" ## lấy filename đã chọn
# ## đây là mảng của các topping_id sau khi chọn nhân bánh
# info["ListTopping"] = [2,3,4,5] 
# ## object dạng mảng chứa SizeId, BaseId, Price, Quantity
# info["ListSize"] = [
#     {
#         "SizeId": 1,
#         "ListBase":[
#             {
#                 "BaseId":1,
#                 "Price": 1000000,
#                 "Quantity": 10
#             },
#             {
#                 "BaseId":2,
#                 "Price": 2000000,
#                 "Quantity": 20
#             },
#         ]
#     },
#     {
#         "SizeId": 2,
#         "ListBase":[
#             {
#                 "BaseId":1,
#                 "Price": 1000000,
#                 "Quantity": 10
#             },
#         ]
#     },
# ]  
# print(info)

# result = pizzaBUS.addPizza(info)
# print(result)



##Sửa pizza
## Bước 1: xử lý file ảnh tương tự như thêm
## + kiếm tra kiểm tra kích thước file ảnh thấp hơn 2mb
## + kiểm tra định dạng tệp tin đã tải lên: allowed_types = ["jpg", "png"]
## + kiếm tra ảnh đã chọn có trùng với ảnh trong /GUI/images không? nếu có thì báo "Đã tồn tại file trong hệ thống, không thể ghi đè file!"
## + nếu các điều kiện trên hợp lệ: thực hiện di chuyển file ảnh đã được tải lên vào /GUI/images (có thể sử dụng module shutil của python)

## Bước 2: thực hiện sửa dữ liệu 
## sau khi chọn các nhân bánh, kích thước, đế ta có 1 ví dụ cấu trúc dictionary như sau:
# info = {}
# info["PizzaId"] = 15 ## lấy từ dòng được chọn
# info["PizzaName"] = "Pizza mới"
# info["CategoryId"]= 2
# info["Description"] =" test tạo bánh mới "
# info["Image"] ="newpizza.png" ## lấy filename đã chọn
# ## đây là mảng của các topping_id sau khi chọn nhân bánh
# info["ListTopping"] = [6,7,8] 
# ## object dạng mảng chứa SizeId, BaseId, Price, Quantity
# info["ListSize"] = [
#     {
#         "SizeId": 1,
#         "ListBase":[
#             {
#                 "BaseId":1,
#                 "Price": 1000000,
#                 "Quantity": 80
#             },
#             {
#                 "BaseId":2,
#                 "Price": 2000000,
#                 "Quantity": 20
#             },
#         ]
#     },
#     {
#         "SizeId": 2,
#         "ListBase":[
#             {
#                 "BaseId":1,
#                 "Price": 1000000,
#                 "Quantity": 10
#             },
#         ]
#     },
# ]  
# result = pizzaBUS.editPizza(info)
# print(result)



















# trang chính chỉ hiện 3 thông tin: id bánh, tên bánh, tên danh mục bánh
# pizzaBUS.readListPizza()
# for pizza in pizzaBUS.listPizza:
#     print(pizza["IdPizza"])
#     print(pizza["PizzaName"])
#     print(pizza["CategoryName"])
#     print("-----------")


## XEM THÔNG TIN
# print("*********************************")
# print("THÔNG TIN CHI TIẾT CỦA BÁNH")
# ## xem chi tiết 1 bánh dựa theo id bánh
# info = pizzaBUS.getInfoPizza(5)
# print("Tên bánh: " + info["PizzaName"])
# print("Ảnh: " + info["Image"]) ## Chỗ này xử lý để hiện ảnh lên giao diện với output là đuôi file (ví dụ: haisan.png)
# print("Loại bánh: " + info["CategoryName"])
# print("Mô tả: " + info["Description"])
# print("Nhân bánh: ", end="")
# if len(info["ListTopping"]) != 0:
#     for topping in info["ListTopping"]:
#         print(topping.getDisplay()+", ", end="")
# print()
# for sizeInfo in info["ListSize"]:
#     print("Kích cỡ bánh: "+ sizeInfo["SizeName"] +" gồm có:")
#     for baseInfo in sizeInfo["ListBase"]:
#         print("\t" +"Đế bánh: " + baseInfo["BaseName"])
#         print("\t" +"Giá: " + str(baseInfo["Price"]))
#         print("\t" +"Số Lượng: " + str(baseInfo["Quantity"]))
#         print("\t"+"-----")


### TÌM KIẾM THEO TÊN
# name_pizza = "Hải sản"
# pizzaBUS.readListPizza()
# data = pizzaBUS.findPizzaByName(name_pizza)
# for pizza in data:
#     print(pizza["IdPizza"])
#     print(pizza["PizzaName"])
#     print(pizza["CategoryName"])
#     print("-----------")

### XÓA PIZZA theo id
# pizzaId = 12
# result = pizzaBUS.delete(pizzaId)
# print(result)


############TEST THỐNG KÊ
# statisticBUS = StatisticBUS
## doanh thu theo danh mục
# tk_category = statisticBUS.category()
# print("Thống kê doanh thu theo danh mục bánh pizza")
# print("Tổng doanh thu thực tế: "+str(tk_category["TotalActualRevenue"]))
# print("Tổng doanh thu dự kiến: "+str(tk_category["TotalExpectedRevenue"]))
# print("Tổng số lượng bán được thực tế: "+str(tk_category["TotalActualSales"]))
# print("Tổng số lượng bán được dự kiến: "+str(tk_category["TotalExpectedSales"]))
# print("---------------------------------")
# print("Tên danh mục" + "\t" + "Doanh thu thực tế"+ "\t" + "Doanh thu dự kiến" + "\t" + "Số lượng bán được thực tế"+ "\t" +"Số lượng bán được dự kiến ")
# for index, value in enumerate(tk_category["Categories"]):
#     print(value.getDisplay(),end="\t")
#     print(tk_category["ActualRevenue"][index],end="\t")
#     print(tk_category["ExpectedRevenue"][index],end="\t")
#     print(tk_category["ActualSales"][index],end="\t")
#     print(tk_category["ExpectedSales"][index],end="")
#     print()


# # tìm kiếm theo khoảng thời gian
# # yyyy-mm-dd
# print("---------------------------------------------------------------------------------")
# startDay = datetime.datetime(2022,9,23)
# endDay = datetime.datetime(2022,10,16)
# tk_category = statisticBUS.searchCategory(startDay,endDay)
# print("Thống kê doanh thu theo danh mục bánh pizza")
# print(tk_category["searchDate"])
# print("Tổng doanh thu thực tế: "+str(tk_category["TotalActualRevenue"]))
# print("Tổng doanh thu dự kiến: "+str(tk_category["TotalExpectedRevenue"]))
# print("Tổng số lượng bán được thực tế: "+str(tk_category["TotalActualSales"]))
# print("Tổng số lượng bán được dự kiến: "+str(tk_category["TotalExpectedSales"]))
# print("---------------------------------")
# print("Tên danh mục" + "\t" + "Doanh thu thực tế"+ "\t" + "Doanh thu dự kiến" + "\t" + "Số lượng bán được thực tế"+ "\t" +"Số lượng bán được dự kiến ")
# for index, value in enumerate(tk_category["Categories"]):
#     print(value.getDisplay(),end="\t") 
#     print(tk_category["ActualRevenue"][index],end="\t")
#     print(tk_category["ExpectedRevenue"][index],end="\t")
#     print(tk_category["ActualSales"][index],end="\t")
#     print(tk_category["ExpectedSales"][index],end="")
#     print()


## doanh thu theo bánh
# tk_pizza = statisticBUS.pizza()
# print("Thống kê doanh thu theo bánh pizza")
# print("Tổng doanh thu thực tế: "+str(tk_pizza["TotalActualRevenue"]))
# print("Tổng doanh thu dự kiến: "+str(tk_pizza["TotalExpectedRevenue"]))
# print("Tổng số lượng bán được thực tế: "+str(tk_pizza["TotalActualSales"]))
# print("Tổng số lượng bán được dự kiến: "+str(tk_pizza["TotalExpectedSales"]))
# print("---------------------------------")
# print("Tên bánh" + "\t" + "Doanh thu thực tế"+ "\t" + "Doanh thu dự kiến" + "\t" + "Số lượng bán được thực tế"+ "\t" +"Số lượng bán được dự kiến ")
# for index, value in enumerate(tk_pizza["Pizzas"]):
#     print(value.getDisplay(),end="\t")
#     print(tk_pizza["ActualRevenue"][index],end="\t")
#     print(tk_pizza["ExpectedRevenue"][index],end="\t")
#     print(tk_pizza["ActualSales"][index],end="\t")
#     print(tk_pizza["ExpectedSales"][index],end="")
#     print()

# # # tìm kiếm theo khoảng thời gian
# # # yyyy-mm-dd
# print("---------------------------------------------------------------------------------")
# startDay = datetime.datetime(2022,9,26)
# endDay = datetime.datetime(2022,10,26)
# tk_pizza = statisticBUS.searchPizza(startDay,endDay)
# print("Thống kê doanh thu theo bánh pizza")
# print(tk_pizza["searchDate"])
# print("Tổng doanh thu thực tế: "+str(tk_pizza["TotalActualRevenue"]))
# print("Tổng doanh thu dự kiến: "+str(tk_pizza["TotalExpectedRevenue"]))
# print("Tổng số lượng bán được thực tế: "+str(tk_pizza["TotalActualSales"]))
# print("Tổng số lượng bán được dự kiến: "+str(tk_pizza["TotalExpectedSales"]))
# print("---------------------------------")
# print("Tên danh mục" + "\t" + "Doanh thu thực tế"+ "\t" + "Doanh thu dự kiến" + "\t" + "Số lượng bán được thực tế"+ "\t" +"Số lượng bán được dự kiến ")
# for index, value in enumerate(tk_pizza["Pizzas"]):
#     print(value.getDisplay(),end="\t") 
#     print(tk_pizza["ActualRevenue"][index],end="\t")
#     print(tk_pizza["ExpectedRevenue"][index],end="\t")
#     print(tk_pizza["ActualSales"][index],end="\t")
#     print(tk_pizza["ExpectedSales"][index],end="")
#     print()


#############
# TEST UserBUS
# userBUS = UserBUS()
# userBUS.readListUser()
# for user in userBUS.listUser:
#     print("Tên tài khoản:" + user.getUsername())
#     print("Nhóm tài khoản:" + userBUS.getGroupName(user))
#     if userBUS.hasPermission(user.getUsername(),"lock"):
#         print("Đã khóa")
#     else:
#         print("Chưa khóa")
# print("--------------------------------")

#TÌM THEO USERNAME
# username_find = "adm"
# result = userBUS.findUserByUsername(username_find) 
# for item in result:
#     print(item.getUsername())

#XEM THÔNG TIN TÀI KHOẢN
# username = "admin"
# infoUser = userBUS.getInfo(username)
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
# userBUS = UserBUS()
# username_input = "nhanvien2"
# password_input = "nhanvien"
# result = userBUS.checkLogin(username_input, password_input)
# if result == "OK": ## đăng nhập thành công
#     infoUser = userBUS.getInfo(username_input)
#     groupBUS = GroupBUS()
#     # Đóng form đăng nhập, mở giao diện quản lý và gửi thông tin (infoUser) sang
#     # Hiển thị các chức năng quyền ở menu quyền
#     permission_dict = {
#         "admin.login": "Đăng nhập trang quản trị",
#         "admin.group": "Quản lý nhóm tài khoản",
#         "admin.user": "Quản lý tài khoản",
#         "admin.category": "Quản lý danh mục bánh",
#         "admin.topping": "Quản lý nhân bánh",
#         "admin.size": "Quản lý kích thước bánh",
#         "admin.base": "Quản lý đế bánh",
#         "admin.pizza": "Quản lý bánh pizza",
#         "admin.order": "Quản lý đơn hàng",
#         "admin.statistic": "Thống kê báo cáo"
#     }

#     for key, value in permission_dict.items():
#         print(value) 
#         if groupBUS.isSet(infoUser["groupId"], key):
#             if groupBUS.hasPermission(infoUser["groupId"], key):
#                 print("Quyền đã mở") 
#                 # thêm vào menu quyền
#             else:
#                 print("Quyền bị khóa")
#         else:
#             print("Chưa phân quyền") 
# else:
#     print(result)##  đăng nhập thất bại, xuất ra lỗi 


## chức năng đăng xuất thì bấm nút đăng xuất => tắt ứng dụng luôn




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
