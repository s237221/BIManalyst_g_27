import ifcopenshell
from ifcopenshell.util import element

from rules import column_AreaRule
#from .rules import windowRule
#from .rules import doorRule

model = ifcopenshell.open("C:/Users/Alexandra/Desktop/SCHOOL/DTU Education/SEM1/Advanced BIM/LECTURE 1/CES_BLD_24_06_STR.ifc")

#windowResult = windowRule.checkRule(model)
#doorResult = doorRule.checkRule(model)
columnResult = column_AreaRule.checkRule(model)

#print("Window result:", windowResult)
#print("Door result:", doorResult)
print("Column result:", columnResult)
