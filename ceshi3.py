from time import *
from datetime import *

aaa = '2020-11-21-05'
aaa = datetime.strptime(aaa, "%Y-%m-%d-%H")
# print((datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d-%H"))
print((aaa + timedelta(days=1)).strftime("%Y-%m-%d-%H"))
