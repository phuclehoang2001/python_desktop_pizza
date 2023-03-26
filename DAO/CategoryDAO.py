from mySQLConnect import sqlConnect
from mysql.connector import Error


class Category:
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

    def getByID(self, categoryID):
        obj_cate = None
        try:
            query = "SELECT * from category Where id = "+ str(categoryID)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            obj_cate = self.result
        except Error as error:
                print(error)
        return obj_cate
    
    def getAllCategory(self):
        list = []
        try:
            query = "SELECT * from category"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            list = self.result
        except Error as error:
                print(error)
        return list
    


test = Category().getAllCategory()
print(test)