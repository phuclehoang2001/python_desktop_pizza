import sys
import datetime

sys.path.insert(0,".")
from DAO import StatusDAO
from DTO import *








################
#test

test = StatusDAO()
list_status = test.getAllStatus()
for status in list_status:
     print(status.getId())
     print(status.getDisplay())

##
list_detail = test.getAllDetail()
for detail in list_detail:
     print(detail.getOrderId())
     print(detail.getStatusId())
     print(detail.getTimeCreated())
##
status = Status()
status.setId(6)
if test.delete(status):
    print("xóa thành công")
else:
    print("xóa thất bại")

##
detail = test.getStatusDetailById(4,1)
print(detail.getTimeCreated())
##
status_findByID = test.getById(1)
print(status_findByID.getDisplay())
##
new_detail = StatusDetail()
new_detail.setOrderId(1)
new_detail.setStatusId(1)
new_detail.setTimeCreated(datetime.datetime.now())


if test.addStatusDetail(new_detail):
    print("thêm trạng thái mới thành công")
else:
    print("thêm trạng thái mới thất bại")

#trang thai nho nhat
firstDetail = test.getFirstStatusDetail(2)
print(firstDetail.getOrderId())
print(firstDetail.getStatusId())
print(firstDetail.getTimeCreated())

## trang thai lon nhat## bug 
lastDetail = test.getLastStatusDetail(2)
print(lastDetail.getOrderId())
print(lastDetail.getStatusId())
print(lastDetail.getTimeCreated())

