import sys
sys.path.insert(0,".")
from DAO import BaseDAO
from DTO import Base
class BaseBUS:
    listBase = []

    def readListBase(self):
        data = BaseDAO()
        if(self.listBase is None):
            self.listBase = []
        self.listBase = data.getAllbase()

    def addBase(self, base):
        data = BaseDAO()
        if self.isExist(base.getDisplay()):
            return False     
        # thêm vào CSDL
        if not data.add(base):
            return False
        #Thêm vào list
        self.listBase.append(base)
        return True
    
    def deleteBase(self, base):
        data = BaseDAO()
        if not data.delete(base):
            return False
        for i in range(len(self.listBase)):
            if self.listBase[i].getId() == base.getId():      
                self.listBase.pop(i)
                break
        return True
    
    def updateBase(self, base):
        data = BaseDAO()
        if not data.update(base):     
            return False
        for i in range(len(self.listBase)):
            if self.listBase[i].getId() == base.getId():      
                self.listBase[i] = base          
                return True
        return False
    
    def isExist(self, display):
        for size in self.listBase:
            if size.getDisplay().upper() == display.upper():
                return True
        return False
    
    def findBasesByName(self, name):
        listBase = []
        for base in self.listBase:
            if name.upper() in base.getDisplay().upper():
                listBase.append(base)    
        return listBase
    


########################################################### 
#  test #   
test = BaseBUS()
test.readListBase()
for base in test.listBase:
    print(base.getId())
    print(base.getDisplay())
print("-----------------------------------")

# # # thêm
# base_new = Base()
# base_new.setDisplay("Viền rau củ")
# if test.addBase(base_new):
#     print("thêm thành công")
# else:
#     print("thêm thất bại")

# sửa
# editBase = Base()
# editBase.setId(6)
# editBase.setDisplay("Viền thịt bò")
# if test.updateBase(editBase):
#     print("sửa thành công")
# else:
#     print("sửa thất bại")

#xóa
# base = Base()
# base.setId(5)
# if test.deleteBase(base):
#     print("xóa thành công")
#     for item in test.listBase:
#         print(item.getId())
#         print(item.getDisplay())
# else:
#     print("xóa thất bại")
#     for item in test.listBase:
#         print(item.getId())
#         print(item.getDisplay())

# tìm kiếm 
# listSearch  = test.findBasesByName("Vi")
# if len(listSearch) != 0:
#     for item in listSearch:
#         print(item.getId())
#         print(item.getDisplay())
# else:
#     print("Không tìm thấy")