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
                user.setFullname(self.result[3])
                user.setBirth(self.result[4]) 
                user.setAddress(self.result[5]) 
                user.setPhone(self.result[6]) 
                user.setEmail(self.result[7]) 
            else:
                user = None
        except Error as error:
                print(error)
        return user
    
    #lấy tất cả 
    def getAllUser(self):
        result = []
        try:
            query = "SELECT * FROM user where group_id = 3 or group_id = 4"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            for user in self.result:
                userDTO = User()
                userDTO.setUsername(user[0]) 
                userDTO.setGroupId(user[1]) 
                userDTO.setFullname(user[3])
                userDTO.setBirth(user[4]) 
                userDTO.setAddress(user[5]) 
                userDTO.setPhone(user[6]) 
                userDTO.setEmail(user[7]) 
                result.append(userDTO)
        except Error as error:
                print(error)
        return result
    
    
    def add(self, user, password):
        username = user.getUsername()
        groupId = user.getGroupId()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        fullname = user.getFullname()
        birth = user.getBirth()
        address = user.getAddress()
        phone = user.getPhone()
        email = user.getEmail()
        try:
            query = "INSERT INTO `user`(username, group_id, password, fullname, birth, address, phone, email)\
                  VALUES ('{username}', '{groupId}', '{password}', '{fullname}', '{birth}', '{address}', '{phone}', '{email}')"\
            .format(username=username, groupId=groupId, password=hashed_password, fullname=fullname, birth=birth, address=address, phone=phone, email=email)    
            print(query)    
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            # Lấy ID của bản ghi vừa được thêm vào
            self.sqlConnect.close()
            return True
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
                SET group_id = '{groupId}', fullname = '{fullname}', birth = '{birth}', address = '{address}', phone = '{phone}', email = '{email}'\
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
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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

    def updatePermissionGroup(self, username, groupId):
        try:
            query = "UPDATE user\
                SET group_id = '{groupId}'\
                WHERE username = '{username}'"\
            .format(username=username, groupId=groupId)      
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
            if self.cursor.rowcount > 0:
                 check = bcrypt.checkpw(password.encode('utf-8'), self.result[2].encode('utf-8'))
            self.sqlConnect.close()
            return check
        except Error as error:
                print(error)
        return False
  
    
    def hasUsername(self, username):
        try:
            query = "SELECT * FROM user WHERE username = '{username}'"\
            .format(username=username)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            return self.cursor.rowcount > 0
        except Error as error:
                print(error)
        return False
    
    