import sys
sys.path.insert(0,".")
from DAO import CategoryDAO
from DTO import Category
class CategoryBUS:
    listCategory = []

    def readListCategory(self):
        data = CategoryDAO()
        if(self.listCategory is None):
            self.listCategory = []
        self.listCategory = data.getAllCategory()

    def addCategory(self, category):
        data = CategoryDAO()

        #Kiểm tra tên loại có trùng không
        if self.isExist(category.display):
            return False     
        # thêm vào CSDL
        data.add(category)
        #Thêm vào list
        self.listCategory.append(category)
        return True
    
    def isExist(self, display):
        for category in self.listCategory:
            if category.getDisplay().upper() == display.upper():
                return True
        return False
    
    def findCategoriesByName(self, name):
        listCategory = []
        for category in self.listCategory:
            if name in category.getDisplay():
                listCategory.append(category)    
        return listCategory
    


 ############################################################ 
 # test #   
test = CategoryBUS()
test.readListCategory()

for category in test.listCategory:
    print(category.getDisplay())
    print(category.getId())

## tìm kiếm 
# listSearch  = test.findCategoriesByName("Cao")
# for cate in listSearch:
#     print(cate.getDisplay())
#     print(cate.getId())

# # thêm
# cate_new = Category()
# cate_new.setDisplay("LoạI mới 5")
# if test.addCategory(cate_new):
#     print("thêm thành công")
# else:
#     print("thêm thất bại")