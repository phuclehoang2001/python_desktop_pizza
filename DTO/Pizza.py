class Pizza:
    id = ""
    display = ""
    categoryId = ""
    description = ""
    image = ""
    
    def getId(self):
        return self.id
    def getDisplay(self):
        return self.display
    def getCategoryId(self):
        return self.categoryId
    def getDescription(self):
        return self.description
    def getImage(self):
        return self.image

    def setDisplay(self, display):
        self.display = display
    def setCategoryId(self, categoryId):
        self.categoryId = categoryId
    def setId(self,id):
        self.id = id
    def setDescription(self,description):
        self.description = description
    def setImage(self,image):
        self.image = image
    