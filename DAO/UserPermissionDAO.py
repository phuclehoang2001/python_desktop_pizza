from .mySQLConnect import sqlConnect
from mysql.connector import Error
import bcrypt
import sys
sys.path.insert(0,".")
from DTO import *

class UserPermissionDAO:
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

    def getByUsername(self, username, permission):
        userPermission = UserPermission()
        try:
            query = "SELECT * FROM user_permission WHERE username ='{username}' AND permission='{permission}'"\
            .format(username=username, permission=permission)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.cursor.rowcount > 0:
                userPermission.setId(self.result[0]) 
                userPermission.setUsername(self.result[1]) 
                userPermission.setPermission(self.result[2]) 
                userPermission.setValue(self.result[3]) 
            else:
                userPermission = None
        except Error as error:
                print(error)
        return userPermission

    def isSet(self, username, permission):
        try:
            query = "SELECT * FROM user_permission WHERE username='{username}' AND permission='{permission}'"\
            .format(username=username, permission=permission)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            return self.cursor.rowcount > 0
        except Error as error:
                print(error)
        return False
    
    def has(self, username, permission):
        return self.getByUsername(username,permission).getValue()
    
    def _set(self, username, permission, value):
        try:
            if int(value) == -1:
                query = "DELETE FROM user_permission WHERE username='{username}' AND permission='{permission}'"\
                .format(username=username, permission=permission) 
                print(query)  
                self.cursor = self.con.cursor()
                self.cursor.execute(query)
                self.con.commit()        
                return
            query = "SELECT * FROM user_permission WHERE username='{username}' AND permission='{permission}'"\
            .format(username=username, permission=permission)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            if self.cursor.rowcount > 0:
                query = "UPDATE user_permission SET value = '{value}' WHERE username = '{username}' AND permission = '{permission}'"\
                .format( value=value, username=username, permission=permission)
                self.cursor = self.con.cursor()
                self.cursor.execute(query)
                self.con.commit()
            else:
                query = "INSERT INTO user_permission(username, permission, value) VALUES ('{username}', '{permission}', '{value}')"\
                .format(username=username, permission=permission, value=value)
                self.cursor = self.con.cursor()
                self.cursor.execute(query)
                self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False