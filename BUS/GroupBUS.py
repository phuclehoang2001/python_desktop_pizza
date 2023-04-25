import sys
import datetime

sys.path.insert(0,".")
from DAO import GroupDAO, GroupPermissionDAO
from DTO import *

## xử lý group và group permission

class GroupBUS:
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
        if not data.add(group):
            return False
        #Thêm vào list
        self.listGroup.append(group)
        return True
    
    def deleteGroup(self, group):
        data = GroupDAO()
        if not data.delete(group):
            return False
        for i in range(len(self.listGroup)):
            if self.listGroup[i].getId() == group.getId():      
                self.listGroup.pop(i)
                break
        return True
    
    def updateGroup(self, group):
        data = GroupDAO()
        if not data.update(group):
            return False
        for i in range(len(self.listGroup)):
            if self.listGroup[i].getId() == group.getId():                 
                self.listGroup[i] = group
                return True
        return False
    
    def isExist(self, display):
        for group in self.listGroup:
            if group.getDisplay().upper() == display.upper():
                return True
        return False
    
    def findGroupByName(self, name):
        listGroup = []
        for group in self.listGroup:
            if name.upper() in group.getDisplay().upper():
                listGroup.append(group)    
        return listGroup
    
    def isSet(self, groupId, permission):
        data = GroupPermissionDAO()
        return data.isSet(groupId,permission)

    def setPermission(self, groupId, permission, value):
        data = GroupPermissionDAO()
        return data._set(groupId, permission, value) 
            