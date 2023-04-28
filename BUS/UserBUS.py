import sys
import datetime

sys.path.insert(0,".")
from DAO import UserDAO, GroupPermissionDAO, UserPermissionDAO, GroupDAO
from DTO import *

## Chỉ xử lý cho các user thuộc nhóm nhân viên và admin

class UserBUS:
    listUser = []

    def readListUser(self):
        data = UserDAO()
        if(self.listUser is None):
            self.listUser = []
        if(len(self.listUser) == 0):
            self.listUser = data.getAllUser()


    def addUser(self, user, password):
        data = UserDAO()
        #Kiểm tra tên có trùng không
        if self.isExist(user.getUsername()):
            return False     
        # thêm vào CSDL
        if not data.add(user, password):
            return False
        #Thêm vào list
        self.listUser.append(user)
        return True        
    
    def updateUser(self, user):
        data = UserDAO()
        self.readListUser()
        if not data.update(user):
            return False
        for i in range(len(self.listUser)):
            if self.listUser[i].getUsername().upper() == user.getUsername().upper():               
                self.listUser[i] = user
                return True
        return False
    
    def updatePassword(self, username, password):
        data = UserDAO()
        if not data.updatePassword(username, password):
            return False
        return True

    def isExist(self, username):
        for user in self.listUser:
            if user.getUsername().upper() == username.upper():
                return True
        return False
    
    def findUserByFullname(self, fullname):
        listUser = []
        for user in self.listUser:
            if fullname.upper() in user.getFullname().upper():
                listUser.append(user)    
        return listUser
    
    def findUserByUsername(self, username):
        listUser = []
        for user in self.listUser:
            if username.upper() in user.getUsername().upper():
                listUser.append(user)    
        return listUser
    
    def isSet(self, groupId, permission):
        data = GroupPermissionDAO()
        return data.isSet(groupId,permission)
    
    def hasPermission(self, groupId, permission):
        data = GroupPermissionDAO()
        return True if data.has(groupId,permission) == 1 else False


    def setPermission(self, groupId, permission, value):
        data = GroupPermissionDAO()
        return  data._set(groupId, permission, value) 
    
    def updatePermissionGroup(self, username, groupId):
        data = UserDAO()
        return  data.updatePermissionGroup(username, groupId) 

    def clockUser(self, username):
        data = UserPermissionDAO()
        if(username == "admin"):
            return False
        data._set(username,"lock", 1)
        
    def unclockUser(self, username):
        data = UserPermissionDAO()
        if(username == "admin"):
            return False
        data._set(username,"lock", 0)

    def hasPermission(self, username, permission):
        userDAO = UserDAO()
        userPermissionDAO = UserPermissionDAO()
        groupPermissionDAO = GroupPermissionDAO()
        if userDAO.hasUsername(username):
            user = userDAO.getByUsername(username)
            userPermission = userPermissionDAO.getByUsername(username, permission)
            if userPermission is not None:
                return userPermission.getValue()
            groupPermission = groupPermissionDAO.getByGroup(user.getGroupId(), permission)
            return False if groupPermission is None else groupPermission.getValue()
        return False
    
    def showInfo(self, username):
        data = GroupDAO()
        self.readListUser()
        for user in self.listUser:
            if user.getUsername().upper() == username.upper():
                user_dict = {}
                user_dict["username"] = user.getUsername()
                user_dict["fullname"] = user.getFullname()
                user_dict["address"] = user.getAddress()
                user_dict["phone"] = user.getPhone()
                user_dict["birthday"] = user.getBirth()
                user_dict["email"] = user.getEmail()
                user_dict["groupName"] = data.getById(user.getGroupId()).getDisplay()
                return user_dict
        return None
    
    def getGroupName(self, user):
        data = GroupDAO()
        return data.getById(user.getGroupId()).getDisplay()