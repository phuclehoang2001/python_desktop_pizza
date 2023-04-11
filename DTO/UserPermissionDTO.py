class UserPermissionDTO:
    id =""
    username = ""
    permission = ""
    value= ""
    
    def getId(self):
        return self.id
    def getUsername(self):
        return self.username
    def getPermission(self):
        return self.permission
    def getValue(self):
        return self.value
    
    def setId(self,id):
        self.id = id
    def setUsername(self,username):
        self.username = username
    def setPermission(self,permission):
        self.permission = permission
    def setValue(self,value):
        self.value = value
