from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class StatisticDAO:
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

    def revenueCategory(self):
        orderDetails = []
        try:
            query = """SELECT `order_detail`.order_id, category.id as category_id, order_detail.price, order_detail.quantity FROM `order_detail` 
            INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
            INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
            INNER JOIN category ON pizza.category_id = category.id
            INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
            WHERE status_detail.status_id = 1"""
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            for row in self.result:
                orderDetail = {}
                orderDetail["orderId"] = row[0]
                orderDetail["categoryId"] = row[1]
                orderDetail["price"] = row[2]
                orderDetail["quantity"] = row[3]
                orderDetails.append(orderDetail)
        except Error as error:
                print(error)
        return orderDetails
    
    def revenueCategoryByTime(self, startDay, endDay):
        orderDetails = []
        try:
            query = ""
            if not startDay and not endDay:
                 query = """SELECT `order_detail`.order_id, category.id as category_id, order_detail.price, order_detail.quantity FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN category ON pizza.category_id = category.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1"""
            elif startDay and endDay:
                query = """SELECT `order_detail`.order_id, category.id as category_id, order_detail.price, order_detail.quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN category ON pizza.category_id = category.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1 AND time_created >= '{startDay}' AND time_created <= '{endDay}'"""\
                .format(startDay=startDay, endDay=endDay)
            elif startDay: 
                query = """SELECT `order_detail`.order_id, category.id as category_id, order_detail.price, order_detail.quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN category ON pizza.category_id = category.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1 AND time_created >= '{startDay}'"""\
                .format(startDay=startDay)
            else:
                query = """SELECT `order_detail`.order_id, category.id as category_id, order_detail.price, order_detail.quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN category ON pizza.category_id = category.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1 AND time_created <= '{endDay}'"""\
                .format(endDay=endDay)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            for row in self.result:
                orderDetail = {}
                orderDetail["orderId"] = row[0]
                orderDetail["categoryId"] = row[1]
                orderDetail["price"] = row[2]
                orderDetail["quantity"] = row[3]
                orderDetails.append(orderDetail)
        except Error as error:
                print(error)
        return orderDetails
    
    def revenuePizza(self):
        orderDetails = []
        try:
            query = """SELECT `order_detail`.order_id, pizza.id as pizza_id, SUM(order_detail.price * order_detail.quantity) as total_price, SUM(order_detail.quantity) as total_quantity
            FROM `order_detail` 
            INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
            INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
            INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
            WHERE status_detail.status_id = 1
            GROUP BY order_id, pizza_id"""
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            for row in self.result:
                orderDetail = {}
                orderDetail["orderId"] = row[0]
                orderDetail["pizzaId"] = row[1]
                orderDetail["totalPrice"] = row[2]
                orderDetail["totalQuantity"] = row[3]
                orderDetails.append(orderDetail)
        except Error as error:
                print(error)
        return orderDetails
    
    def revenuePizzaByTime(self, startDay, endDay):
        orderDetails = []
        try:
            query = ""
            if not startDay and not endDay:
                 query = """SELECT `order_detail`.order_id, pizza.id as pizza_id, SUM(order_detail.price * order_detail.quantity) as total_price, SUM(order_detail.quantity) as total_quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1
                GROUP BY order_id, pizza_id"""
            elif startDay and endDay:
                query = """SELECT `order_detail`.order_id, pizza.id as pizza_id, SUM(order_detail.price * order_detail.quantity) as total_price, SUM(order_detail.quantity) as total_quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1 AND time_created >= '{startDay}' AND time_created <= '{endDay}'
                GROUP BY order_id, pizza_id"""\
                .format(startDay=startDay, endDay=endDay)
            elif startDay: 
                query = """SELECT `order_detail`.order_id, pizza.id as pizza_id, SUM(order_detail.price * order_detail.quantity) as total_price, SUM(order_detail.quantity) as total_quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1 AND time_created >= '{startDay}'
                GROUP BY order_id, pizza_id"""\
                .format(startDay=startDay)
            else:
                query = """SELECT `order_detail`.order_id, pizza.id as pizza_id, SUM(order_detail.price * order_detail.quantity) as total_price, SUM(order_detail.quantity) as total_quantity
                FROM `order_detail` 
                INNER JOIN pizza_detail ON order_detail.pizza_detail_id = pizza_detail.id
                INNER JOIN pizza ON pizza_detail.pizza_id = pizza.id
                INNER JOIN status_detail ON order_detail.order_id = status_detail.order_id
                WHERE status_detail.status_id = 1 AND time_created <= '{endDay}'
                GROUP BY order_id, pizza_id"""\
                .format(endDay=endDay)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            for row in self.result:
                orderDetail = {}
                orderDetail["orderId"] = row[0]
                orderDetail["pizzaId"] = row[1]
                orderDetail["totalPrice"] = row[2]
                orderDetail["totalQuantity"] = row[3]
                orderDetails.append(orderDetail)
        except Error as error:
                print(error)
        return orderDetails