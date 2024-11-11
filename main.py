import ifcopenshell
from ifcopenshell.util import element

from A3 import try_out_A3_WORKS
model = ifcopenshell.open("C:/Users/Alexandra/Desktop/SCHOOL/DTU_Education/SEM1/Advanced_BIM/LECTURE 1/CES_BLD_24_06_STR.ifc")
columnResult = try_out_A3_WORKS.checkRule(model,10,360,360)
print("Column result:", columnResult)



