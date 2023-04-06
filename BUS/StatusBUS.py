import sys
sys.path.insert(0,".")
from DAO import StatusDAO
from DTO import Category

test = StatusDAO()
list_status = test.getAllStatus()
for status in list_status:
     print(status.getId())
     print(status.getDisplay())