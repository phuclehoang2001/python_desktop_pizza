class CategoryDTO:
    id = ""
    group_id = ""
    permission = ""
    value =""
    
    def getId(self):
        return self.id
    
    def getGroupId(self):
        return self.group_id
    
    def getPermission(self):
        return self.permission
    
    def getValue(self):
        return self.value
    
    def setGroupId(self, group_id):
        self.group_id = group_id
    
    def setId(self, id):
        self.id = id

    def setPermission(self , permission):
        self.permission = permission
        
    def setValue(self , value):
        self.value = value