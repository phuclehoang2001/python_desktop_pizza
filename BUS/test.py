import sys
sys.path.insert(0,".")
from DAO import *

cate = CategoryDAO().getAllCategory()
print(cate)