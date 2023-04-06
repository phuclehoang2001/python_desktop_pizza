from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class CategoryDAO:
    cursor = None
    result = None
    con = None
    sqlConnect = sqlConnect()
    def __init__(self):
        if self.con is None:
            try:
                self.con = self.sqlConnect.getConnect()
            except Error as error:
                print(error)

    #trả về 1 object theo id loại
    def getByID(self, categoryID):
        obj_cate = None
        try:
            query = "SELECT * FROM category WHERE id = "+ str(categoryID)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            obj_cate = self.result
        except Error as error:
                print(error)
        return obj_cate
    
    # trả về một list theo tên loại
    def getByDisplay(self, display):
        obj_cate = None
        try:
            query = "SELECT * FROM category WHERE display = "+ str(display)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            obj_cate = self.result
        except Error as error:
                print(error)
        return obj_cate
    
    #lấy tất cả loại
    def getAllCategory(self):
        result = []
        try:
            query = "SELECT * FROM category"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng CategoryDTO để thêm vào result
            for category in self.result:
                ## category trả về là kiểu tuple
                cateDTO = Category()
                cateDTO.setId(category[0])
                cateDTO.setDisplay(category[1])
                result.append(cateDTO)
    
        except Error as error:
                print(error)
        return result
    
    
    def add(self, category):
        try:
            query = "INSERT INTO `category`(display) VALUES('{display}')"\
            .format(display=category.getDisplay())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def update(self, category):
        try:
            ## dấu\ để xuống dòng chuỗi, format để chèn giá trị vào chuỗi
            query = "UPDATE `category` SET display = '{display}' WHERE id = {id}"\
            .format(display=category.display, id=category.id)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def delete(self, category):
        try:
            query = "DELETE FROM `category` WHERE id = {id}"\
            .format(id=category.id)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False


    # Hàm xóa nhiều category theo mảng các id 
    def deleteList(self, listIdCategory):
        wheres = []
        for id_category in listIdCategory:
             wheres.append("id = {id_category}".format(id_category=id_category))
        try:
            sub_query = " or ".join(wheres)
            query = "DELETE FROM `category` WHERE " + sub_query
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
