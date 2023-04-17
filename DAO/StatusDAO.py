from .mySQLConnect import sqlConnect
from mysql.connector import Error
import sys
sys.path.insert(0,".")
from DTO import *

class StatusDAO:
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

    def getById(self, statusId):
        status = Status()
        try:
            query = "SELECT * FROM status WHERE id = "+ str(statusId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            status.setId(self.result[0]) 
            status.setDisplay(self.result[1]) 
        except Error as error:
                print(error)
        return status
    
    def getStatusDetailById(self, orderId, statusId):
        detail = StatusDetail()
        try:
            query = "SELECT * FROM status_detail WHERE order_id = {orderId} and status_id = {statusId}"\
            .format(orderId=orderId, statusId=statusId)   
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()
            if self.result is not None:
                detail.setOrderId(self.result[0]) 
                detail.setStatusId(self.result[1]) 
                detail.setTimeCreated(self.result[2]) 
            else:
                 detail = None
            self.sqlConnect.close()
        except Error as error:
                print(error)
        return detail


    def getAllStatus(self):
        result = []
        try:
            query = "SELECT * FROM status ORDER BY id ASC"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for status in self.result: 
                statusDTO = Status()
                statusDTO.setId(status[0])
                statusDTO.setDisplay(status[1])
                result.append(statusDTO)
        except Error as error:
                print(error)
        return result

    def getListStatusDetail(self, orderId, length):
        result = []
        try:
            for i in range(1,length+1):
                detail = self.getStatusDetailById(orderId,i)
                result.append(detail)
        except Error as error:
                print(error)
        return result

    def add(self, status):
        try:
            query = "INSERT INTO `status`(display) VALUES('{display}')"\
            .format(display=status.getDisplay())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False

    def update(self, status):
        try:
            ## dấu\ để xuống dòng chuỗi, format để chèn giá trị vào chuỗi
            query = "UPDATE `status` SET display = '{display}' WHERE id = {id}"\
            .format(display=status.getDisplay(), id=status.getId())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
    def delete(self, status):
        try:
            query = "DELETE FROM `status` WHERE id = {id}"\
            .format(id=status.getId())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False


    def getAllDetail(self):
        result = []
        try:
            query = "SELECT * FROM  status_detail"
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            
            ## tạo đối tượng DTO để thêm vào result
            for detail in self.result: 
                detailDTO = StatusDetail()
                detailDTO.setOrderId(detail[0])
                detailDTO.setStatusId(detail[1])
                detailDTO.setTimeCreated(detail[2])
                result.append(detailDTO)
        except Error as error:
                print(error)
        return result
    
    def addStatusDetail(self, statusDetail):
        try:
            query = "INSERT INTO `status_detail`(order_id, status_id, time_created) VALUES({order_id},{status_id},'{time_created}')"\
            .format(order_id=statusDetail.getOrderId(), status_id=statusDetail.getStatusId(), time_created= statusDetail.getTimeCreated())        
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            self.con.commit()
            self.sqlConnect.close()
            return True
        except Error as error:
                print(error)
        return False
    
     ## trả về statusDetail có trạng thái status_detail lớn nhất, với input là orderId
    def getLastStatusDetail(self, orderId):
        detailDTO = StatusDetail()
        try:
            query = "SELECT * FROM `status_detail` WHERE order_id = {orderId} ORDER BY status_id DESC LIMIT 1"\
            .format(orderId=orderId)  
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone() 
            if self.result is not None:
                detailDTO.setOrderId(self.result[0]) 
                detailDTO.setStatusId(self.result[1]) 
                detailDTO.setTimeCreated(self.result[2]) 
            else:
                detailDTO = None
            self.sqlConnect.close()
        except Error as error:
                print(error)
        return detailDTO
    
    ## trả về statusDetail có trạng thái status_detail nhỏ nhất, với input là orderId
    def getFirstStatusDetail(self, orderId):
        detailDTO = StatusDetail()
        try:
            query = "SELECT * FROM `status_detail` WHERE order_id = {orderId} ORDER BY status_id ASC LIMIT 1"\
            .format(orderId=orderId)  
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()  
            if self.result is not None:
                detailDTO.setOrderId(self.result[0]) 
                detailDTO.setStatusId(self.result[1]) 
                detailDTO.setTimeCreated(self.result[2]) 
            else:
                detailDTO = None
            self.sqlConnect.close()
        except Error as error:
                print(error)
        return detailDTO

   
    # lấy trạng thái lớn nhất
    def getByOrderId(self, orderId): 
        statusDTO = Status()     
        try:
            statusId = self.getLastStatusDetail(orderId).getStatusId()
            query = "SELECT * FROM status WHERE id = "+ str(statusId)
            self.cursor = self.sqlConnect.getCursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchone()   
            if self.result is not None:     
                statusDTO.setId(self.result[0]) 
                statusDTO.setDisplay(self.result[1]) 
            self.sqlConnect.close()
        except Error as error:
                print(error)
        return statusDTO