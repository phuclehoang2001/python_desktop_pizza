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

    def getByGroup(self, groupId, permission):
        groupPermission = GroupPermission()
        try:
            query = "SELECT * FROM group_permission WHERE `group_id`='{groupId}' AND permission='{permission}'"\
            .format(groupId=groupId, permission=permission)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                groupPermission.setId(self.result[0]) 
                groupPermission.setGroupId(self.result[1]) 
                groupPermission.setPermission(self.result[2]) 
                groupPermission.setValue(self.result[3]) 
        except Error as error:
                print(error)
        return groupPermission

    def isSet(self, id, permission):
        try:
            query = "SELECT * FROM group_permission WHERE group_id='{id}' AND permission='{permission}'"\
            .format(id=id, permission=permission)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            return self.result.rowcount > 0
        except Error as error:
                print(error)
        return False
    
    def has(self, id, permission):
        return self.getByGroup(id,permission).getValue()
    
    def set(self, groupId, permission, value):
        try:
            query = "SELECT * FROM group_permission WHERE group_id='{groupId}' AND permission='{permission}'"\
            .format(groupId=groupId, permission=permission)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            if self.result.rowcount > 0:
                query = "UPDATE group_permission SET value = '{value}' WHERE group_id = '{groupId}' AND permission = '{permission}'"\
                .format( value=value, groupId=groupId, permission=permission)
                self.cursor = self.con.cursor()
                self.cursor.execute(query)
                self.con.commit()
            else:
                query = "INSERT INTO group_permission(group_id, permission, value) VALUES ('{groupId}', '{permission}', '{value}')"\
                .format(groupId=groupId, permission=permission, value=value)
                self.cursor = self.con.cursor()
                self.cursor.execute(query)
                self.con.commit()
            self.sqlConnect.close()
        except Error as error:
                print(error)
        return False