from .mySQLConnect import sqlConnect
from mysql.connector import Error
import bcrypt
import sys
sys.path.insert(0,".")
from DTO import *

class UserDAO:
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

    def getByUsername(self, username):
        user = User()
        try:
            query = "SELECT * FROM user WHERE username = '{username}'"\
            .format(username=username)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                user.setUsername(self.result[0]) 
                user.setGroupId(self.result[1]) 
                user.setFullName(self.result[2])
                user.setBirth(self.result[3]) 
                user.setAddress(self.result[4]) 
                user.setPhone(self.result[5]) 
                user.setEmail(self.result[6]) 
            else:
                user = None
        except Error as error:
                print(error)
        return user
    
    def getBySearch(self, username, arrGroup):
        pass
    
    #lấy tất cả 
    def getAllUser(self):
        result = []
        try:
            query = "SELECT * FROM user"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                userDTO = User()
                userDTO.setUsername(self.result[0]) 
                userDTO.setGroupId(self.result[1]) 
                userDTO.setFullName(self.result[2])
                userDTO.setBirth(self.result[3]) 
                userDTO.setAddress(self.result[4]) 
                userDTO.setPhone(self.result[5]) 
                userDTO.setEmail(self.result[6]) 
                result.append(userDTO)
        except Error as error:
                print(error)
        return result
    
    
    def add(self, user, password):
        username = user.getUsername()
        groupId = user.getGroupId()
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        fullname = user.getFullname()
        birth = user.getBirth()
        address = user.getAddress()
        phone = user.getPhone()
        email = user.getEmail()
        try:
            query = "INSERT INTO `user`(username, group_id, password, fullname, birth, address, phone, email)\
                  VALUES ('{username}', {groupId, '{password}', '{fullname}', '{birth}', '{address}', '{phone}', '{email}')"\
            .format(username=username, groupId=groupId, password=hashed_password, fullname=fullname, birth=birth, address=address, phone=phone, email=email)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            # Lấy ID của bản ghi vừa được thêm vào
            newId = self.cursor.lastrowid
            self.sqlConnect.close()
            return newId
        except Error as error:
                print(error)
        return False

    def update(self, user):
        username = user.getUsername()
        groupId = user.getGroupId()
        fullname = user.getFullname()
        birth = user.getBirth()
        address = user.getAddress()
        phone = user.getPhone()
        email = user.getEmail()
        try:
            query = "UPDATE user\
                SET group_id = {groupId}, fullname = '{fullname}', birth = '{birth}', address = '{address}', phone = '{phone}', email = '{email}'\
                WHERE username = '{username}'"\
            .format(username=username, groupId=groupId,fullname=fullname, birth=birth, address=address, phone=phone, email=email)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def updatePassword(self, username, password):
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        try:
            query = "UPDATE user\
                SET password = '{password}'\
                WHERE username = '{username}'"\
            .format(username=username, password=hashed_password)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False


    def check(self, username, password):
        try:
            query = "SELECT * FROM user WHERE username='{username}'"\
            .format(username=username)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            check = False
            if self.result.rowcount > 0:
                 check = bcrypt.checkpw(password.encode('utf-8'), self.result["password"])
            self.sqlConnect.close()
            return check
        except Error as error:
                print(error)
        return False
  
   