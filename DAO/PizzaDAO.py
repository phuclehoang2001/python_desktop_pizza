from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class PizzaDAO:
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

    def getById(self, pizzaId):
        pizza = Pizza()
        try:
            query = "SELECT * FROM pizza WHERE id = "+ str(pizzaId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            pizza.setId(self.result[0]) 
            pizza.setCategoryId(self.result[1]) 
            pizza.setDisplay(self.result[2]) 
            pizza.setDescription(self.result[3]) 
            pizza.setImage(self.result[4]) 
        except Error as error:
                print(error)
        return pizza

    def getByPizzaDetailId(self, pizzaDetailId):
        detail = PizzaDetail()
        try:
            query = "SELECT * FROM `pizza_detail` WHERE id = '{pizzaDetailId}'"\
            .format(pizzaDetailId=pizzaDetailId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            
            detail.setId(self.result[0]) 
            detail.setPizzaId(self.result[1]) 
            detail.setSizeId(self.result[2]) 
            detail.setBaseId(self.result[3]) 
            detail.setPrice(self.result[4]) 
            detail.setQuantity(self.result[5]) 
        except Error as error:
                print(error)
        return detail


    def getAllPizza(self):
        result = []
        try:
            query = "SELECT * FROM pizza"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for pizza in self.result: 
                pizzaDTO = Pizza()
                pizzaDTO.setId(pizza[0]) 
                pizzaDTO.setCategoryId(pizza[1]) 
                pizzaDTO.setDisplay(pizza[2]) 
                pizzaDTO.setDescription(pizza[3]) 
                pizzaDTO.setImage(pizza[4])  
                result.append(pizzaDTO)
        except Error as error:
                print(error)
        return result

    def getAllDetail(self):
        result = []
        try:
            query = "SELECT * FROM  pizza_detail"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for detail in self.result: 
                detailDTO = PizzaDetail()
                detailDTO.setId(detail[0])
                detailDTO.setPizzaId(detail[1])
                detailDTO.setSizeId(detail[2])
                detailDTO.setBaseId(detail[3])
                detailDTO.setPrice(detail[4])
                detailDTO.setQuantity(detail[5])
                result.append(detailDTO)
        except Error as error:
                print(error)
        return result
    
    def getListPizzaDetail(self, pizzaId):
        result = []
        try:
            query = "SELECT * FROM `pizza_detail` WHERE pizza_id = {pizzaId}"\
            .format(pizzaId=pizzaId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for detail in self.result: 
                detailDTO = PizzaDetail()
                detailDTO.setId(detail[0])
                detailDTO.setPizzaId(detail[1])
                detailDTO.setSizeId(detail[2])
                detailDTO.setBaseId(detail[3])
                detailDTO.setPrice(detail[4])
                detailDTO.setQuantity(detail[5])
                result.append(detailDTO)
        except Error as error:
                print(error)
        return result

    def addPizza(self, pizza):
        id = pizza.getId()
        categoryId = pizza.getCategoryId()
        display = pizza.getDisplay()
        description = pizza.getDescription()
        image = pizza.getImage()
        
        try:
            query = "INSERT INTO `pizza`(id, category_id, display, description, image)\
                VALUES ('{id}', '{categoryId}','{display}', '{description}', '{image}')"\
            .format(id=id, categoryId=categoryId, display=display, description=description, image=image)      
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def getPizzaDetail(self, pizzaId, sizeId, baseId):
        detail = PizzaDetail()
        try:
            query = "SELECT * FROM `pizza_detail` WHERE pizza_id = '{pizzaId}' AND size_id = '{sizeId}' AND base_id = '{baseId}'"\
            .format(pizzaId=pizzaId, sizeId=sizeId, baseId=baseId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()   
            if self.result is not None:            
                detail.setId(self.result[0]) 
                detail.setPizzaId(self.result[1]) 
                detail.setSizeId(self.result[2]) 
                detail.setBaseId(self.result[3]) 
                detail.setPrice(self.result[4]) 
                detail.setQuantity(self.result[5]) 
            else:
                 detail = None
        except Error as error:
                print(error)
        return detail
    
    def updatePizzaDetail(self, pizzaDetail):
        try:
            query = "UPDATE `pizza_detail` SET pizza_id = '{pizzaId}', size_id = '{sizeId}', base_id = '{baseId}',\
            price = '{price}', quantity = '{quantity}' WHERE id = {id}"\
            .format(pizzaId=pizzaDetail.getPizzaId(), sizeId=pizzaDetail.getSizeId(), baseId=pizzaDetail.getBaseId(),\
                     price=pizzaDetail.getPrice(), quantity=pizzaDetail.getQuantity(),id=pizzaDetail.getId())       
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def addPizzaDetail(self, pizzaDetail):
        try:
            query = "INSERT INTO `pizza_detail`(pizza_id, size_id, base_id, price, quantity)\
                VALUES ('{pizzaId}','{sizeId}','{baseId}', '{price}', '{quantity}')"\
            .format(pizzaId=pizzaDetail.getPizzaId(), sizeId=pizzaDetail.getSizeId(), baseId=pizzaDetail.getBaseId(), price=pizzaDetail.getPrice(), quantity=pizzaDetail.getQuantity())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def addOrUpdatePizzaDetail(self, pizzaDetail):
        try:
            currentDetail = self.getPizzaDetail(pizzaDetail.getPizzaId(), pizzaDetail.getSizeId(), pizzaDetail.getBaseId())
            if currentDetail is None:
                self.addPizzaDetail(pizzaDetail)
            else:
                currentDetail.setPrice(pizzaDetail.getPrice())
                currentDetail.setQuantity(pizzaDetail.getQuantity())
                self.updatePizzaDetail(currentDetail)
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def add(self, categoryId, display, description, image):
        try:
            query = """INSERT INTO pizza(category_id, display, description, image) VALUES
                    ('{categoryId}', '{display}', '{description}', '{image}')"""\
            .format(categoryId=categoryId,display=display,description=description,image=image)    
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            pizzaId = self.cursor.lastrowid
            self.con.commit()
            self.sqlConnect.close()
            return pizzaId
        except Error as error:
                print(error)
        return False

    def checkSize(self, idPizza, idSize):
        result = False
        try:
            query = "SELECT * FROM pizza_detail WHERE pizza_id = {idPizza} AND size_id = {idSize}"\
            .format(idPizza=idPizza,idSize=idSize)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            result = self.cursor.rowcount > 0
            self.sqlConnect.close()
            return result
        except Error as error:
                print(error)
        return False
   
    def checkBase(self, idPizza, idSize, idBase):
        result = False
        try:
            query = "SELECT * FROM pizza_detail WHERE pizza_id = {idPizza} AND size_id = {idSize} AND base_id = {idBase}"\
            .format(idPizza=idPizza,idSize=idSize, idBase=idBase)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            result = self.cursor.rowcount > 0
            self.sqlConnect.close()
            return result
        except Error as error:
                print(error)
        return False
    
    def getPriceAndQuantity(self, idPizza, idSize, idBase):
        data = {}
        try:
            query = "SELECT price,quantity FROM pizza_detail WHERE pizza_id = {idPizza} AND size_id = {idSize} AND base_id = {idBase}"\
            .format(idPizza=idPizza,idSize=idSize, idBase=idBase)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            data["Price"] = self.result[0]
            data["Quantity"] = self.result[1]
            self.sqlConnect.close()
            return data
        except Error as error:
                print(error)
        return data

    def deletePizzaDetail(self, pizzaId):
        try:
            query = "DELETE FROM `pizza_detail` WHERE pizza_id = {pizzaId}"\
            .format(pizzaId=pizzaId)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True            
        except Error as error:
                print(error)
        return False  

    def deleteToppingDetail(self, pizzaId):
        try:
            query = "DELETE FROM `topping_detail` WHERE pizza_id = {pizzaId}"\
            .format(pizzaId=pizzaId)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True            
        except Error as error:
                print(error)
        return False  
    
    def addToppingDetail(self, pizzaId, toppingId):
        try:
            query = """INSERT INTO topping_detail(pizza_id, topping_id) VALUES
                            ('{pizzaId}', '{toppingId}')"""\
            .format(pizzaId=pizzaId, toppingId=toppingId)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True            
        except Error as error:
                print(error)
        return False  
    
    def delete(self, pizzaId):
        try:
            if not self.deletePizzaDetail(pizzaId) or not self.deleteToppingDetail(pizzaId):
                 return False
            query = "DELETE FROM `pizza` WHERE id = {pizzaId}"\
            .format(pizzaId=pizzaId)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False  
        

    def search(self, display):
        listPizza = self.getAllPizza()
        if display is not None:
           newlist = []
           for pizza in listPizza:
               if display.upper() in pizza.getDisplay().upper():
                    newlist.append(pizza)
           return newlist
        return listPizza
    
    def hasOrder(self, pizzaId):
        result = False
        try:
            query = "SELECT * FROM order_detail, pizza_detail WHERE pizza_detail_id = pizza_detail.id AND pizza_id = {pizzaId}"\
            .format(pizzaId=pizzaId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            result = self.cursor.rowcount > 0
            self.sqlConnect.close()
            return result
        except Error as error:
                print(error)
        return False