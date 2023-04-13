class User:
    username = ""
    group_id = ""
    password = ""
    fullname = ""
    birth = ""
    address = ""
    phone = ""
    email = ""

    def getGroupId(self):
        return self.group_id
    def getFullname(self):
        return self.fullname
    def getAddress(self):
        return self.address
    def getPhone(self):
        return self.phone
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getBirth(self):
        return self.birth
    def getEmail(self):
        return self.email

    
    def setGroupId(self,group_id):
        self.group_id = group_id
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
    def setPassword(self,password):
        self.password = password
