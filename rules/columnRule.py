import ifcopenshell

def checkRule(model):
    columns = model.by_type('IfcColumn')

    result = f"Column: {len(Column)}"

    return result
print("For now it is only showing how many columns there should be in the file")
