from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class BaseDAO:
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

    def getById(self, baseId):
        base = Base()
        try:
            query = "SELECT * FROM `base` WHERE id = {baseId}"\
            .format(baseId=baseId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                base.setId(self.result[0]) 
                base.setDisplay(self.result[1]) 
        except Error as error:
                print(error)
        return base
    
    # trả về một list theo tên
    def getByDisplay(self, display):
        result = []
        try:
            query = "SELECT * FROM `base` WHERE display LIKE '%{display}%'"\
            .format(display=display)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
          
            for base in self.result:
                baseDTO = Base()
                baseDTO.setId(base[0])
                baseDTO.setDisplay(base[1])
                result.append(baseDTO)
        except Error as error:
                print(error)
        return result
    
    #lấy tất cả 
    def getAllbase(self):
        result = []
        try:
            query = "SELECT * FROM `base`"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()        
            for base in self.result:         
                baseDTO = Base()
                baseDTO.setId(base[0])
                baseDTO.setDisplay(base[1])
                result.append(baseDTO)   
        except Error as error:
                print(error)
        return result
    
    
    def add(self, base):
        try:
            query = "INSERT INTO `base`(display) VALUES('{display}')"\
            .format(display=base.getDisplay())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def update(self, base):
        try:
            ## dấu\ để xuống dòng chuỗi, format để chèn giá trị vào chuỗi
            query = "UPDATE `base` SET display = '{display}' WHERE id = {id}"\
            .format(display=base.getDisplay(), id=base.getId())       
            print(query) 
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def delete(self, base):
        try:
            query = "DELETE FROM `base` WHERE id = {id}"\
            .format(id=base.getId())        
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
    def deleteList(self, listIdBase):
        wheres = []
        for id_base in listIdBase:
             wheres.append("id = {id_base}".format(id_base=id_base))
        try:
            sub_query = " or ".join(wheres)
            query = "DELETE FROM `base` WHERE " + sub_query
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
  