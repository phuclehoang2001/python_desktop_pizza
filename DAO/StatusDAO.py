from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class StatusDAO:
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

    def getById(self, statusId):
        obj_cate = None
        try:
            query = "SELECT * FROM status WHERE id = "+ str(statusId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            obj_cate = self.result
        except Error as error:
                print(error)
        return obj_cate
    
    
    def getAllStatus(self):
        result = []
        try:
            query = "SELECT * FROM status"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for status in self.result: 
                statusDTO = Status()
                statusDTO.setId(status[0])
                statusDTO.setDisplay(status[1])
                result.append(statusDTO)
        except Error as error:
                print(error)
        return result
    
    
    def add(self, status):
        try:
            query = "INSERT INTO `status`(display) VALUES('{display}')"\
            .format(display=status.getDisplay())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def update(self, status):
        try:
            ## dấu\ để xuống dòng chuỗi, format để chèn giá trị vào chuỗi
            query = "UPDATE `status` SET display = '{display}' WHERE id = {id}"\
            .format(display=status.getDisplay(), id=status.getId())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def delete(self, status):
        try:
            query = "DELETE FROM `status` WHERE id = {id}"\
            .format(id=status.getDisplay())        
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
    

