import sys
sys.path.insert(0,".")
from DTO import *
from DAO import *

  
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