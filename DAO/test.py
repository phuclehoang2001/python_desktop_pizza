import sys
import datetime
import bcrypt
sys.path.insert(0,".")
from DTO import *
from DAO import UserDAO,GroupDAO, UserPermissionDAO, GroupPermissionDAO


########################## test GroupPermissionDAO
data = GroupPermissionDAO()
# groupId = 4
# permission = "admin.login"
# info =  data.getByGroup(groupId,permission) 
# if info is not None:
#     print(info.getId())
#     print(info.getGroupId())
#     print(info.getPermission())
#     print(info.getValue())
# else:
#     print("None")

# groupId = 5
# permission = "admin.pizza"
# checkPermission = data.isSet(4,permission)
# if checkPermission :
#     print("Đã phân quyền")
# else:
#     print("Chưa phân quyền")

# groupId = 4
# permission = "admin.pizza"
# try:
#     value =  data.has(groupId,permission)
#     print(value)
# except:
#     print("Error")


# groupId = 3
# permission = "admin.pizza"
# value = 1
# if not data._set(groupId,permission,value):
#     print("Error")
# else:
#     print("Set permission successfully")





########################## test UserPermissionDAO
# data = UserPermissionDAO()

# username = "3119410300"
# permission = "lock"
# info =  data.getByUsername(username,permission) 
# if info is not None:
#     print(info.getId())
#     print(info.getUsername())
#     print(info.getPermission())
#     print(info.getValue())
# else:
#     print("None")


# username = "3119410300"
# permission = "lock"
# checkPermission =  data.isSet(username,permission) 
# if checkPermission :
#     print("Đã phân quyền")
# else:
#     print("Chưa phân quyền")

# username = "3119410330"
# permission = "lock"
# try:
#     value =  data.has(username,permission)
#     print(value)
# except:
#     print("Error")



# username = "3119410300"
# permission = "unlock"
# value = -1
# if not data._set(username,permission,value):
#     print("Error")
# else:
#     print("Set permission successfully")


########################## test UserDAO
# data = UserDAO()
# user = data.getByUsername("3119410300")
# print(user.getFullname())
# print(user.getEmail())

# listUser = data.getAllUser()
# for item in listUser:
#     print(item.getUsername())
#     print(item.getFullname())
#     print(item.getEmail())
#     print(item.getAddress())

# user = User()
# user.setUsername("admin2")
# user.setGroupId(4)
# user.setFullname("Nguyễn Thanh Phong")
# password= "admin"
# if not data.add(user,password):
#     print("Thêm thất bại")
# else:
#     print("Thêm thành công")

# Tạo đối tượng datetime với ngày 25 tháng 4 năm 2023
# my_birthdate = datetime.datetime(2002, 4, 25)
# user = User()
# user.setUsername("admin2")
# user.setGroupId(4)
# user.setFullname("Nguyễn Thanh Hải")
# user.setBirth(my_birthdate)
# user.setEmail("hai@gmail.com")
# if not data.update(user):
#     print("Sửa thất bại")
# else:
#     print("Sửa thành công")

# username = "admin2"
# password_new = "SGUDHSG"
# if not data.updatePassword(username,password_new):
#     print("Sửa mật khẩu thất bại")
# else:
#     print("Sửa mật khẩu thành công")


# username = "admin"
# password_check = "admin"
# if  data.check(username,password_check):
#     print("Mật khẩu hợp lệ")
# else:
#     print("Sai mật khẩu")


# username = "admin"
# if  data.hasUsername(username):
#     print("Tồn tại tài khoản")
# else:
#     print("Không tồn tại tài khoản")



################################ test GroupDAO
# data = GroupDAO()
# group = data.getById(5)
# print(group.getId())
# print(group.getDisplay())

# listGroup = data.getByDisplay("viên")
# for groupItem in listGroup:
#     print(groupItem.getId())
#     print(groupItem.getDisplay())

# allGroup = data.getAllGroup()
# for groupItem in allGroup:
#     print(groupItem.getId())
#     print(groupItem.getDisplay())

# newGroup = Group()
# newGroup.setDisplay("Quản lý kho")
# if data.add(newGroup):
#     print("thêm thành công")
# else:
#     print("Thêm thất bại")

# editGroup = Group()
# editGroup.setDisplay("Kiểm hàng")
# editGroup.setId(7)## kiem id hop le trong BUS 
# data.update(editGroup)

# group = Group()
# group.setId(10)# kiem id hop le trong BUS
# data.delete(group)

# list_group = [7,8]
# data.deleteList(list_group)

###########test category
# new = Category()
# new.id = 1
# new.display ="loại mới 4"

# update1 = CategoryDAO()
# update1.update(new)
# if update1.con.is_connected():
#     print("Kết nối đang mở")
# else:
#     print("Kết nối đã đóng")

###########test add
# new = Category()
# new.display ="bánh ngọt có vị mặn"

# update1 = CategoryDAO()
# update1.add(new)
# if update1.con.is_connected():
#     print("Kết nối đang mở")
# else:
#     print("Kết nối đã đóng")

###########test add
# cate = Category()
# cate.id = 8

# update1 = CategoryDAO()
# update1.delete(cate)
# if update1.con.is_connected():
#     print("Kết nối đang mở")
# else:
#     print("Kết nối đã đóng")

#############test delete by list
# mylist = [10,11]
# update1 = CategoryDAO()
# update1.deleteList(mylist)