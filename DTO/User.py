class User:
    username = ""
    groupId = ""
    fullname = ""
    birth = ""
    address = ""
    phone = ""
    email = ""

    def getGroupId(self):
        return self.groupId
    def getFullname(self):
        return self.fullname
    def getAddress(self):
        return self.address
    def getPhone(self):
        return self.phone
    def getUsername(self):
        return self.username
    def getBirth(self):
        return self.birth
    def getEmail(self):
        return self.email

    
    def setGroupId(self,groupId):
        self.groupId = groupId
    def setFullname(self,fullname):
        self.fullname = fullname
    def setAddress(self,address):
        self.address = address
    def setPhone(self,phone):
        self.phone = phone
    def setUsername(self,username):
        self.username = username
    def setBirth(self,birth):
        self.birth = birth
    def setEmail(self,email):
        self.email = email
