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
        if self.isExist(category.getDisplay()):
            return False     
        # thêm vào CSDL
        data.add(category)
        #Thêm vào list
        self.listCategory.append(category)
        return True
    
    def deleteCategory(self, category):
        data = CategoryDAO()
        if not data.delete(category):
            return False
        for i in range(len(self.listCategory)):
            if self.listCategory[i].getId() == category.getId():      
                self.listCategory.pop(i)
                break
        return True
    
    def updateCategory(self, category):
        data = CategoryDAO()
        for i in range(len(self.listCategory)):
            if self.listCategory[i].getId() == category.getId():      
                data.update(category)
                self.listCategory[i] = category
                return True
        return False
    
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
#  test #   
test = CategoryBUS()
test.readListCategory()
for category in test.listCategory:
    print(category.getDisplay())
    print(category.getId())
print("-----------------------------------")
# sửa
# editCate = Category()
# editCate.setId(9)
# editCate.setDisplay("loại mới 77S")
# if test.updateCategory(editCate):
#     print("sửa thành công")
# else:
#     print("sửa thất bại")

#xóa
# cate = Category()
# cate.setId(3)
# if test.deleteCategory(cate):
#     print("xóa thành công")
#     for category in test.listCategory:
#         print(category.getDisplay())
#         print(category.getId())
# else:
#     print("xóa thất bại")
#     for category in test.listCategory:
#         print(category.getDisplay())
#         print(category.getId())     

# # # thêm
# cate_new = Category()
# cate_new.setDisplay("LoạI mới 5")
# if test.addCategory(cate_new):
#     print("thêm thành công")
# else:
#     print("thêm thất bại")

# print("------------------------")
# test2 = CategoryBUS()
# test2.readListCategory()

# for category in test2.listCategory:
#     print(category.getDisplay())
#     print(category.getId())
# ## tìm kiếm 
# # listSearch  = test.findCategoriesByName("Cao")
# # for cate in listSearch:
# #     print(cate.getDisplay())
# #     print(cate.getId())
