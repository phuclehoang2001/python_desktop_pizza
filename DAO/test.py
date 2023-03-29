import sys
sys.path.insert(0,".")
from DTO import *

cate1 = CategoryDTO()
cate1.display = "test"
print(cate1.getDisplay())