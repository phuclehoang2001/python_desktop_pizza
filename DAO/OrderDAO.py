from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class OrderDAO:
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

    def getById(self, orderId):
        order = Order()
        try:
            query = "SELECT * FROM `order` WHERE id = "+ str(orderId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            order.setId(self.result[0]) 
            order.setCustomer(self.result[1]) 
            order.setHandler(self.result[2]) 
            order.setTotalPrice(self.result[3]) 
            order.setQuantity(self.result[4]) 
            order.setFullname(self.result[5]) 
            order.setAddress(self.result[6]) 
            order.setPhone(self.result[7])  
            order.setPaymentType(self.result[8]) 
            order.setOrderType(self.result[9]) 
            order.setOrderTime(self.result[10]) 
            order.setNote(self.result[11]) 
        except Error as error:
                print(error)
        return order

    def getByUsername(self, username):
        result = []
        try:
            query = "SELECT * FROM `order` WHERE customer = '{username}' ORDER BY id DESC"\
            .format(username=username)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            for order in self.result: 
                orderDTO = Order()
                orderDTO.setId(order[0]) 
                orderDTO.setCustomer(order[1]) 
                orderDTO.setHandler(order[2]) 
                orderDTO.setTotalPrice(order[3]) 
                orderDTO.setQuantity(order[4]) 
                orderDTO.setFullname(order[5]) 
                orderDTO.setAddress(order[6]) 
                orderDTO.setPhone(order[7])  
                orderDTO.setPaymentType(order[8]) 
                orderDTO.setOrderType(order[9]) 
                orderDTO.setOrderTime(order[10]) 
                orderDTO.setNote(order[11]) 
                result.append(orderDTO)
        except Error as error:
                print(error)
        return result

    def getByUsernameAndId(self, username, orderId):
        result = []
        try:
            query = "SELECT * FROM `order` WHERE customer = '{username}' AND id = {orderId} ORDER BY id DESC"\
            .format(username=username, orderId=orderId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            for order in self.result: 
                orderDTO = Order()
                orderDTO.setId(order[0]) 
                orderDTO.setCustomer(order[1]) 
                orderDTO.setHandler(order[2]) 
                orderDTO.setTotalPrice(order[3]) 
                orderDTO.setQuantity(order[4]) 
                orderDTO.setFullname(order[5]) 
                orderDTO.setAddress(order[6]) 
                orderDTO.setPhone(order[7])  
                orderDTO.setPaymentType(order[8]) 
                orderDTO.setOrderType(order[9]) 
                orderDTO.setOrderTime(order[10]) 
                orderDTO.setNote(order[11]) 
                result.append(orderDTO)
        except Error as error:
                print(error)
        return result

    def getAllOrder(self):
        result = []
        try:
            query = "SELECT * FROM `order`"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for order in self.result: 
                orderDTO = Order()
                orderDTO.setId(order[0]) 
                orderDTO.setCustomer(order[1]) 
                orderDTO.setHandler(order[2]) 
                orderDTO.setTotalPrice(order[3]) 
                orderDTO.setQuantity(order[4]) 
                orderDTO.setFullname(order[5]) 
                orderDTO.setAddress(order[6]) 
                orderDTO.setPhone(order[7])  
                orderDTO.setPaymentType(order[8]) 
                orderDTO.setOrderType(order[9]) 
                orderDTO.setOrderTime(order[10]) 
                orderDTO.setNote(order[11]) 
                result.append(orderDTO)
        except Error as error:
                print(error)
        return result

    def getAllDetail(self):
        result = []
        try:
            query = "SELECT * FROM  order_detail"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for detail in self.result: 
                detailDTO = OrderDetail()
                detailDTO.setId(detail[0])
                detailDTO.setOrderId(detail[1])
                detailDTO.setPizzaDetailId(detail[2])
                detailDTO.setPrice(detail[3])
                detailDTO.setQuantity(detail[4])
                result.append(detailDTO)
        except Error as error:
                print(error)
        return result
    
    def getListOrderDetail(self, orderId):
        result = []
        try:
            query = "SELECT * FROM `order_detail` WHERE order_id = {orderId} ORDER BY id DESC"\
            .format(orderId=orderId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for detail in self.result: 
                detailDTO = OrderDetail()
                detailDTO.setId(detail[0])
                detailDTO.setOrderId(detail[1])
                detailDTO.setPizzaDetailId(detail[2])
                detailDTO.setPrice(detail[3])
                detailDTO.setQuantity(detail[4])
                result.append(detailDTO)
        except Error as error:
                print(error)
        return result

    def addOrder(self, order):
        customer = order.getCustomer()
        totalPrice = order.getTotalPrice()
        quantity = order.getQuantity()
        fullname = order.getFullname()
        address = order.getAddress()
        phone = order.getPhone()
        paymentType = order.getPaymentType()
        orderType = order.getOrderType()
        orderTime = order.getOrderTime()
        note = order.getNote()
        try:
            query = "INSERT INTO `order`(customer, handler, total_price, quantity, fullname, address, phone, payment_type, order_type, order_time, note)\
                VALUES ('{customer}', null,'{totalPrice}','{quantity}', '{fullname}', '{address}', '{phone}', '{paymentType}', '{orderType}', '{orderTime}', '{note}')"\
            .format(customer=customer, totalPrice=totalPrice, quantity=quantity, fullname=fullname, address=address, phone=phone, paymentType=paymentType,\
                    orderType=orderType, orderTime=orderTime, note=note)      
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def addDetail(self, orderDetail):
        orderId = orderDetail.getOrderId()
        pizzaDetailId = orderDetail.getPizzaDetailId()
        price = orderDetail.getPrice()
        quantity = orderDetail.getQuantity()
        try:
            query = "INSERT INTO order_detail(order_id, pizza_detail_id, price, quantity)\
                VALUES ('{orderId}','{pizzaDetailId}','{price}', '{quantity}')"\
            .format(orderId=orderId, pizzaDetailId=pizzaDetailId, price=price, quantity=quantity)        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def update(self, order):
        try:
            query = "UPDATE `order` SET handler = '{handler}' WHERE id = {id}"\
            .format(handler=order.getHandler(), id=order.getId())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False