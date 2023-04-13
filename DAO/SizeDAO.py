from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class SizeDAO:
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

    def getById(self, sizeId):
        size = Size()
        try:
            query = "SELECT * FROM `size` WHERE id = {sizeId}"\
            .format(sizeId=sizeId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                size.setId(self.result[0]) 
                size.setPriority(self.result[0])
                size.setDisplay(self.result[1]) 
        except Error as error:
                print(error)
        return size
    
    # trả về một list theo tên
    def getByDisplay(self, display):
        result = []
        try:
            query = "SELECT * FROM `size` WHERE display LIKE '%{display}%'"\
            .format(display=display)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
          
            for size in self.result:
                sizeDTO = Size()
                sizeDTO.setId(size[0])
                sizeDTO.setPriority(size[0])
                sizeDTO.setDisplay(size[1])
                result.append(sizeDTO)
        except Error as error:
                print(error)
        return result
    
    def getByPriority(self, sizePriority):
        size = Size()
        try:
            query = "SELECT * FROM `size` WHERE priority = {sizePriority}"\
            .format(sizePriority=sizeId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                size.setId(self.result[0]) 
                size.setPriority(self.result[0])
                size.setDisplay(self.result[1]) 
        except Error as error:
                print(error)
        return size
    
    #lấy tất cả 
    def getAllSize(self):
        result = []
        try:
            query = "SELECT * FROM `size`"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()        
            for size in self.result:         
                sizeDTO = Size()
                sizeDTO.setId(size[0])
                sizeDTO.setPriority(size[0])
                sizeDTO.setDisplay(size[1])
                result.append(sizeDTO)   
        except Error as error:
                print(error)
        return result
    
    
    def add(self, size):
        try:
            query = "INSERT INTO `size`(display) VALUES('{display}')"\
            .format(display=size.getDisplay())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def update(self, size):
        try:
            ## dấu\ để xuống dòng chuỗi, format để chèn giá trị vào chuỗi
            query = "UPDATE `size` SET display = '{display}' WHERE id = {id}"\
            .format(display=size.getDisplay(), id=size.getId())       
            print(query) 
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def delete(self, size):
        try:
            query = "DELETE FROM `size` WHERE id = {id}"\
            .format(id=size.getId())        
            print(query)
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    # Hàm xóa nhiều hàng theo mảng các id 
    def deleteList(self, listIdSize):
        wheres = []
        for id_size in listIdSize:
             wheres.append("id = {id_size}".format(id_size=id_size))
        try:
            sub_query = " or ".join(wheres)
            query = "DELETE FROM `size` WHERE " + sub_query
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
  