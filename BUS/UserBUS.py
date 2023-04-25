import sys
import datetime

sys.path.insert(0,".")
from DAO import UserDAO
from DTO import *

## Chỉ xử lý cho các user thuộc nhóm nhân viên và admin

class UserBUS:
    listUser = []

    def readListUser(self):
        data = UserDAO()
        if(self.listUser is None):
            self.listUser = []
        self.listUser = data.getAllUser()

    
            