import ifcopenshell

from .rules import columnRule
#from .rules import windowRule
#from .rules import doorRule

model = ifcopenshell.open("C:\Users\Alexandra\Desktop\SCHOOL\DTU Education\SEM1\Advanced BIM\LECTURE 1")

#windowResult = windowRule.checkRule(model)
#doorResult = doorRule.checkRule(model)
columnResult = columnRule.checkRule(model)

#print("Window result:", windowResult)
#print("Door result:", doorResult)
print("Column result:", columnResult)
