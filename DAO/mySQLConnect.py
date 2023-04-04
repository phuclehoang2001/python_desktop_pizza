import mysql.connector
from mysql.connector import Error

class sqlConnect:
    host = "localhost"
    database = "pizza"
    user = "root"
    password =""
    port = 3306 #default
    con = None
    myCursor = None
    myResult = None


    def getConnect(self):
        if self.con is None:
            try:       
                self.con = mysql.connector.connect(
                    host = self.host,
                    user = self.user, 
                    password=self.password, 
                    database=self.database,
                    port=self.port)
            except Error as error:
                print(error)
        return self.con
    
    def getCursor(self):
        try:                
            self.myCursor = self.con.cursor()
        except Error as error:
            print(error)
        return self.myCursor

    def close(self):
        self.con.close()
    
