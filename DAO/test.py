import sys
sys.path.insert(0,".")
from DTO import *
from DAO import *

###########test update
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