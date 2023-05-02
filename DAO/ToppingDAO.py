from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class ToppingDAO:
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

    def getByPizzaId(self, idPizza):
        result = []
        try:
            query = "SELECT * FROM topping_detail,topping WHERE pizza_id = {idPizza} AND topping_id = id"\
            .format(idPizza=idPizza)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            for topping in self.result:
                toppingDTO = Topping()
                toppingDTO.setId(topping[2])
                toppingDTO.setDisplay(topping[3])
                result.append(toppingDTO)
        except Error as error:
                print(error)
        return result
    
    #lấy tất cả 
    def getAllTopping(self):
        result = []
        try:
            query = "SELECT * FROM `topping`"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()        
            for topping in self.result:         
                toppingDTO = Topping()
                toppingDTO.setId(topping[0])
                toppingDTO.setDisplay(topping[1])
                result.append(toppingDTO)   
        except Error as error:
                print(error)
        return result