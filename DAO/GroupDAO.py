from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class GroupDAO:
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

    def getById(self, groupId):
        group = Group()
        try:
            query = "SELECT * FROM `group` WHERE id = {groupId}"\
            .format(groupId=groupId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                group.setId(self.result[0]) 
                group.setDisplay(self.result[1]) 
        except Error as error:
                print(error)
        return group
    
    # trả về một list theo tên
    def getByDisplay(self, display):
        result = []
        try:
            query = "SELECT * FROM `group` WHERE display LIKE '%{display}%'"\
            .format(display=display)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
          
            for group in self.result:
                groupDTO = Group()
                groupDTO.setId(group[0])
                groupDTO.setDisplay(group[1])
                result.append(groupDTO)
        except Error as error:
                print(error)
        return result
    
    #lấy tất cả 
    def getAllGroup(self):
        result = []
        try:
            query = "SELECT * FROM `group`"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()        
            for group in self.result:         
                groupDTO = Group()
                groupDTO.setId(group[0])
                groupDTO.setDisplay(group[1])
                result.append(groupDTO)   
        except Error as error:
                print(error)
        return result
    
    
    def add(self, group):
        try:
            query = "INSERT INTO `group`(display) VALUES('{display}')"\
            .format(display=group.getDisplay())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def update(self, group):
        try:
            ## dấu\ để xuống dòng chuỗi, format để chèn giá trị vào chuỗi
            query = "UPDATE `group` SET display = '{display}' WHERE id = {id}"\
            .format(display=group.getDisplay(), id=group.getId())       
            print(query) 
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def delete(self, group):
        try:
            query = "DELETE FROM `group` WHERE id = {id}"\
            .format(id=group.getId())        
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
    def deleteList(self, listIdGroup):
        wheres = []
        for id_group in listIdGroup:
             wheres.append("id = {id_group}".format(id_group=id_group))
        try:
            sub_query = " or ".join(wheres)
            query = "DELETE FROM `group` WHERE " + sub_query
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
  