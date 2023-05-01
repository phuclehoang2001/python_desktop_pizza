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
    

