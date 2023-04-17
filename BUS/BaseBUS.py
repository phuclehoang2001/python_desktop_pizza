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
    


