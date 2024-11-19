import ifcopenshell
from ifcopenshell.util import element

from A3 import columncheckreportRule
model = ifcopenshell.open("C:/Users/Alexandra/Desktop/SCHOOL/DTU_Education/SEM1/Advanced_BIM/LECTURE 1/CES_BLD_24_06_STR.ifc")
columnResult = columncheckreportRule.checkRule(model,10,360,360)
print("Column result:", columnResult)



