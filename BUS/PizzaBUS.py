import sys
import datetime

sys.path.insert(0,".")
from DAO import PizzaDAO
from DTO import *

class PizzaBUS:
    listPizza = []
    listPizzaDetail = []
   
    def readListPizza(self):
        data = PizzaDAO()
        if(self.listPizza is None):
            self.listPizza = []
        self.listPizza = data.getAllPizza()

    def readListPizzaDetail(self):
        data = PizzaDAO()  
        if(self.listPizzaDetail is None):
            self.listPizzaDetail = []
        self.listPizzaDetail = data.getAllPizzaDetail() 
        

    #Tìm theo tên (display)
    def findPizzaByDisplay(self, display):
        data = PizzaDAO()  
        return data.search(display)
    
    
    def delete(self, pizza):
        data = PizzaDAO()  
        return data.delete(pizza)
    
   
    

    
    
    
 