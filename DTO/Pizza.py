class Pizza:
    id = ""
    display = ""
    category_id = ""
    description = ""
    image = ""
    
    def getId(self):
        return self.id
    def getDisplay(self):
        return self.display
    def getCategoryId(self):
        return self.category_id
    def getDescription(self):
        return self.description
    def getImage(self):
        return self.image

    def setDisplay(self, display):
        self.display = display
    def setCategoryId(self, category_id):
        self.category_id = category_id
    def setId(self,id):
        self.id = id
    def setDescription(self,description):
        self.description = description
    def setImage(self,image):
        self.image = image
    