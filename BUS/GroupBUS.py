import sys
import datetime

sys.path.insert(0,".")
from DAO import GroupDAO
from DTO import *

class OrderBUS:
    listGroup = []

    def readListGroup(self):
        data = GroupDAO()
        if(self.listGroup is None):
            self.listGroup = []
        self.listGroup = data.getAllGroup()

    def addGroup(self, group):
        data = GroupDAO()

        #Kiểm tra tên có trùng không
        if self.isExist(group.getDisplay()):
            return False     
        # thêm vào CSDL
        data.add(group)
        #Thêm vào list
        self.listCategory.append(group)
        return True
    
    def isExist(self, display):
        for group in self.listGroup:
            if group.getDisplay().upper() == display.upper():
                return True
        return False
    
    def findCategoriesByName(self, name):
        listGroup = []
        for group in self.listGroup:
            if name in group.getDisplay():
                listGroup.append(group)    
        return listGroup