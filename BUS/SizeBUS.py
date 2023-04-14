import sys
sys.path.insert(0,".")
from DAO import SizeDAO
from DTO import Size
class SizeBUS:
    listSize = []

    def readListSize(self):
        data = SizeDAO()
        if(self.listSize is None):
            self.listSize = []
        self.listSize = data.getAllSize()

    def addSize(self, size):
        data = SizeDAO()
        if self.isExist(size.getDisplay()):
            return False     
        # thêm vào CSDL
        if not data.add(size):
            return False
        #Thêm vào list
        self.listSize.append(size)
        return True
    
    def deleteSize(self, size):
        data = SizeDAO()
        if not data.delete(size):
            return False
        for i in range(len(self.listSize)):
            if self.listSize[i].getId() == size.getId():      
                self.listSize.pop(i)
                break
        return True
    
    def updateSize(self, size):
        data = SizeDAO()
        if not data.update(size):     
            return False
        for i in range(len(self.listSize)):
            if self.listSize[i].getId() == size.getId():      
                self.listSize[i] = size
                
                return True
        return False
    
    def isExist(self, display):
        for size in self.listSize:
            if size.getDisplay().upper() == display.upper():
                return True
        return False
    
    def findSizesByName(self, name):
        listSize = []
        for size in self.listSize:
            if name.upper() in size.getDisplay().upper():
                listSize.append(size)    
        return listSize
    


########################################################### 
#  test #   
# test = SizeBUS()
# test.readListSize()
# for size in test.listSize:
#     print(size.getId())
#     print(size.getDisplay())
#     print(size.getPriority())
# print("-----------------------------------")

# # # thêm
# size_new = Size()
# size_new.setDisplay("Siêu to 20''".replace("'","''"))
# if test.addSize(size_new):
#     print("thêm thành công")
# else:
#     print("thêm thất bại")

# sửa
# editSize = Size()
# editSize.setId(11)
# editSize.setDisplay("Siêu to 15\"")
# if test.updateSize(editSize):
#     print("sửa thành công")
# else:
#     print("sửa thất bại")

#xóa
# size = Size()
# size.setId(12)
# if test.deleteSize(size):
#     print("xóa thành công")
#     for item in test.listSize:
#         print(item.getId())
#         print(item.getDisplay())
#         print(item.getPriority())
# else:
#     print("xóa thất bại")
#     for item in test.listSize:
#         print(item.getId())
#         print(item.getDisplay())
#         print(item.getPriority())    

# tìm kiếm 
# listSearch  = test.findSizesByName("6")
# for item in listSearch:
#     print(item.getId())
#     print(item.getDisplay())
#     print(item.getPriority()) 
