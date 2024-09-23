import ifcopenshell
from ifcopenshell.util import element

from rules import column_AreaRule
model = ifcopenshell.open("C:/Users/Alexandra/Desktop/SCHOOL/DTU Education/SEM1/Advanced BIM/LECTURE 1/CES_BLD_24_06_STR.ifc")
columnResult = column_AreaRule.checkRule(model)
print("Column result:", columnResult)
