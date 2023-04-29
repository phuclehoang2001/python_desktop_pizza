import sys
import datetime

sys.path.insert(0,".")
from DAO import StatusDAO
from DAO import CategoryDAO
from DAO import PizzaDAO
from DAO import StatisticDAO
from DTO import *

class StatisticBUS:

    def category():
        categoryDAO = CategoryDAO()
        statisticDAO = StatisticDAO()
        statusDAO = StatusDAO()
        
        details = statisticDAO.revenueCategory()
        categories = categoryDAO.getAllCategory()

        statisticByCategory = {}
        statisticByCategory["Categories"] = categories
        statisticByCategory["TotalActualRevenue"] = 0
        statisticByCategory["TotalExpectedRevenue"] = 0
        statisticByCategory["TotalActualSales"] = 0
        statisticByCategory["TotalExpectedSales"] = 0
        statisticByCategory["ActualRevenue"] = []
        statisticByCategory["ExpectedRevenue"] = []
        statisticByCategory["ActualSales"] = []
        statisticByCategory["ExpectedSales"] = []
        for category in categories:
            # doanh thu
            actual1 = 0
            expected1 = 0
            # so luong ban
            actual2 = 0
            expected2 = 0
            for detail in details:
                orderId = detail["orderId"]
                categoryId = detail["categoryId"]
                price = detail["price"]
                quantity = detail["quantity"]
                if categoryId != category.getId():
                    continue
                statusDetail = statusDAO.getLastStatusDetail(orderId)
                if statusDetail.getStatusId() == 6:
                    actual1 += price * quantity
                    actual2 += quantity
                if statusDetail.getStatusId() < 6:
                    expected1 += price * quantity
                    expected2 += quantity
            statisticByCategory["ActualRevenue"].append(actual1)
            statisticByCategory["ActualSales"].append(actual2)
            statisticByCategory["ExpectedRevenue"].append(expected1)
            statisticByCategory["ExpectedSales"].append(expected2)
            statisticByCategory["TotalActualRevenue"] += actual1
            statisticByCategory["TotalActualSales"] += actual2
            statisticByCategory["TotalExpectedRevenue"] += expected1
            statisticByCategory["TotalExpectedSales"] += expected2
        
        return statisticByCategory
    

    def searchCategory(startDay = None, endDay = None): 
        categoryDAO = CategoryDAO()
        statisticDAO = StatisticDAO()
        statusDAO = StatusDAO()
        
        details = statisticDAO.revenueCategoryByTime(startDay, endDay)
        categories = categoryDAO.getAllCategory()

        searchDate = ""
        if startDay and endDay:
            searchDate = 'Từ ' + str(startDay) +' đến ' + str(endDay)
        elif startDay:
            searchDate = 'Từ ' + str(startDay) 
        elif endDay: 
            searchDate = 'Đến ' + str(endDay)

        statisticByCategory = {}
        statisticByCategory["Categories"] = categories
        statisticByCategory["TotalActualRevenue"] = 0
        statisticByCategory["TotalExpectedRevenue"] = 0
        statisticByCategory["TotalActualSales"] = 0
        statisticByCategory["TotalExpectedSales"] = 0
        statisticByCategory["ActualRevenue"] = []
        statisticByCategory["ExpectedRevenue"] = []
        statisticByCategory["ActualSales"] = []
        statisticByCategory["ExpectedSales"] = []
        statisticByCategory["searchDate"] = searchDate
        for category in categories:
            # doanh thu
            actual1 = 0
            expected1 = 0
            # so luong ban
            actual2 = 0
            expected2 = 0
            for detail in details:
                orderId = detail["orderId"]
                categoryId = detail["categoryId"]
                price = detail["price"]
                quantity = detail["quantity"]
                if categoryId != category.getId():
                    continue
                statusDetail = statusDAO.getLastStatusDetail(orderId)
                if statusDetail.getStatusId() == 6:
                    actual1 += price * quantity
                    actual2 += quantity
                if statusDetail.getStatusId() < 6:
                    expected1 += price * quantity
                    expected2 += quantity
            statisticByCategory["ActualRevenue"].append(actual1)
            statisticByCategory["ActualSales"].append(actual2)
            statisticByCategory["ExpectedRevenue"].append(expected1)
            statisticByCategory["ExpectedSales"].append(expected2)
            statisticByCategory["TotalActualRevenue"] += actual1
            statisticByCategory["TotalActualSales"] += actual2
            statisticByCategory["TotalExpectedRevenue"] += expected1
            statisticByCategory["TotalExpectedSales"] += expected2
        
        return statisticByCategory  

    def pizza():
        pizzaDAO = PizzaDAO()
        statisticDAO = StatisticDAO()
        statusDAO = StatusDAO()
        
        details = statisticDAO.revenuePizza()
        pizzas = pizzaDAO.getAllPizza()

        statisticByPizza = {}
        statisticByPizza["Pizzas"] = pizzas
        statisticByPizza["TotalActualRevenue"] = 0
        statisticByPizza["TotalExpectedRevenue"] = 0
        statisticByPizza["TotalActualSales"] = 0
        statisticByPizza["TotalExpectedSales"] = 0
        statisticByPizza["ActualRevenue"] = []
        statisticByPizza["ExpectedRevenue"] = []
        statisticByPizza["ActualSales"] = []
        statisticByPizza["ExpectedSales"] = []
        for pizza in pizzas:
            # doanh thu
            actual1 = 0
            expected1 = 0
            # so luong ban
            actual2 = 0
            expected2 = 0
            for detail in details:
                orderId = detail["orderId"]
                pizzaId = detail["pizzaId"]
                price = detail["totalPrice"]
                quantity = detail["totalQuantity"]
                if pizzaId != pizza.getId():
                    continue
                statusDetail = statusDAO.getLastStatusDetail(orderId)
                if statusDetail.getStatusId() == 6:
                    actual1 += price
                    actual2 += quantity
                if statusDetail.getStatusId() < 6:
                    expected1 += price 
                    expected2 += quantity
            statisticByPizza["ActualRevenue"].append(actual1)
            statisticByPizza["ActualSales"].append(actual2)
            statisticByPizza["ExpectedRevenue"].append(expected1)
            statisticByPizza["ExpectedSales"].append(expected2)
            statisticByPizza["TotalActualRevenue"] += actual1
            statisticByPizza["TotalActualSales"] += actual2
            statisticByPizza["TotalExpectedRevenue"] += expected1
            statisticByPizza["TotalExpectedSales"] += expected2
        
        return statisticByPizza

    def searchPizza(startDay = None, endDay = None):
        pizzaDAO = PizzaDAO()
        statisticDAO = StatisticDAO()
        statusDAO = StatusDAO()
        
        details = statisticDAO.revenuePizzaByTime(startDay, endDay)
        pizzas = pizzaDAO.getAllPizza()
        
        searchDate = ""
        if startDay and endDay:
            searchDate = 'Từ ' + str(startDay) +' đến ' + str(endDay)
        elif startDay:
            searchDate = 'Từ ' + str(startDay) 
        elif endDay: 
            searchDate = 'Đến ' + str(endDay)


        statisticByPizza = {}
        statisticByPizza["Pizzas"] = pizzas
        statisticByPizza["TotalActualRevenue"] = 0
        statisticByPizza["TotalExpectedRevenue"] = 0
        statisticByPizza["TotalActualSales"] = 0
        statisticByPizza["TotalExpectedSales"] = 0
        statisticByPizza["ActualRevenue"] = []
        statisticByPizza["ExpectedRevenue"] = []
        statisticByPizza["ActualSales"] = []
        statisticByPizza["ExpectedSales"] = []
        statisticByPizza["searchDate"] = searchDate
        for pizza in pizzas:
            # doanh thu
            actual1 = 0
            expected1 = 0
            # so luong ban
            actual2 = 0
            expected2 = 0
            for detail in details:
                orderId = detail["orderId"]
                pizzaId = detail["pizzaId"]
                price = detail["totalPrice"]
                quantity = detail["totalQuantity"]
                if pizzaId != pizza.getId():
                    continue
                statusDetail = statusDAO.getLastStatusDetail(orderId)
                if statusDetail.getStatusId() == 6:
                    actual1 += price
                    actual2 += quantity
                if statusDetail.getStatusId() < 6:
                    expected1 += price 
                    expected2 += quantity
            statisticByPizza["ActualRevenue"].append(actual1)
            statisticByPizza["ActualSales"].append(actual2)
            statisticByPizza["ExpectedRevenue"].append(expected1)
            statisticByPizza["ExpectedSales"].append(expected2)
            statisticByPizza["TotalActualRevenue"] += actual1
            statisticByPizza["TotalActualSales"] += actual2
            statisticByPizza["TotalExpectedRevenue"] += expected1
            statisticByPizza["TotalExpectedSales"] += expected2
        
        return statisticByPizza
