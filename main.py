import ifcopenshell
from ifcopenshell.util import element

from rules import column_checkReportRule
model = ifcopenshell.open("C:/Users/Alexandra/Desktop/SCHOOL/DTU_Education/SEM1/Advanced_BIM/LECTURE 1/CES_BLD_24_06_STR.ifc")
columnResult = column_checkReportRule.checkRule(model)
print("Column result:", columnResult)



