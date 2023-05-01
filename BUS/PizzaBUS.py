import sys
import datetime

sys.path.insert(0,".")
from DAO import PizzaDAO, CategoryDAO, ToppingDAO, BaseDAO, SizeDAO
from DTO import *

class PizzaBUS:
    listPizza = []

   
    def readListPizza(self):
        pizzaDAO = PizzaDAO()
        categoryDAO = CategoryDAO()
        if self.listPizza is None:
            self.listPizza = []
        ##Nam xóa dòng này để cập nhật lại Table
        for pizza in pizzaDAO.getAllPizza():
            pizza_overview = {}
            pizza_overview["IdPizza"] = pizza.getId()
            pizza_overview["PizzaName"] = pizza.getDisplay()
            pizza_overview["CategoryName"] = categoryDAO.getByID(pizza.getCategoryId()).getDisplay()
            self.listPizza.append(pizza_overview)

    def getInfoPizza(self, idPizza):
        info = {}
        pizzaDAO = PizzaDAO()
        categoryDAO = CategoryDAO()
        toppingDAO = ToppingDAO()
        baseDAO = BaseDAO()
        sizeDAO = SizeDAO()

        allSizes = sizeDAO.getAllSize()
        allBases = baseDAO.getAllbase()
        pizza = pizzaDAO.getById(idPizza)
        
        info["ListSize"] = []  
        for size in allSizes:
            checkSize = pizzaDAO.checkSize(pizza.getId(),size.getId())
            if checkSize:
                sizeInfo = {}
                sizeInfo["SizeName"] = size.getDisplay()
                sizeInfo["ListBase"] = []           
                for base in allBases:
                    checkBase = pizzaDAO.checkBase(pizza.getId(),size.getId(), base.getId())
                    if checkBase:
                        baseInfo = {}
                        data = pizzaDAO.getPriceAndQuantity(pizza.getId(),size.getId(), base.getId())
                        baseInfo["BaseName"] = base.getDisplay()
                        baseInfo["Price"] = data["Price"]
                        baseInfo["Quantity"] = data["Quantity"]
                        sizeInfo["ListBase"].append(baseInfo)
                info["ListSize"].append(sizeInfo)

        info["PizzaName"] = pizza.getDisplay()
        info["Image"] = pizza.getImage()
        info["Description"] = pizza.getDescription()
        info["CategoryName"] = categoryDAO.getByID(pizza.getCategoryId()).getDisplay()
        info["ListTopping"] = toppingDAO.getByPizzaId(pizza.getId())

        
        return info
        

    def findPizzaByName(self, name):
        listPizza = []
        for pizza in self.listPizza:
            if name.upper() in pizza["PizzaName"].upper():
                listPizza.append(pizza)    
        return listPizza
    
    def delete(self, pizzaId):
        data = PizzaDAO()  
        result = ""
        order = data.hasOrder(pizzaId)
        if order:
            result = "Không thể xóa bánh vì đã có đơn hàng!"
        else:
            ## thuc hien xoa
            
            if data.delete(pizzaId):
                result = "Xóa thành công"
            else:
                result = "Xóa thất bại"
        return result
    
    def addPizza(self, pizza_dict):
        pass

    
    

    
    
    
 