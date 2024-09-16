
import ifcopenshell

def checkRule(model):

    columns_required = 764
    columns_in_model = len(model.by_type("IfcColumn"))
    
    print(f"\nThere are {columns_in_model} columns in the model")
    
    if columns_required is columns_in_model:
        print ('RESULT: The number of columns is correct')
    else:
        print ('RESULT: The number of columns is wrong')
        
    #Calculating the total length of columns
    total_beam_Length = 0
    
    for entity in model.by_type("IfcBeam"):
        #we need to get the attributes
       for relDefinesByProperties in entity.IsDefinedBy:
            for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                #and then get the attribute we are looking for
                if prop.Name == 'Length':
                    #add the length to the total length
                    total_beam_Length += prop.NominalValue.wrappedValue
    
    print(f"\nThere are {total_beam_Length} meters of beam in the model")
    
    #Getting the properties of columns
    column = model.by_type('IfcColumn')[0]
    for definition in column.IsDefinedBy:
        # To support IFC2X3, we need to filter our results.
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            # Might return Pset_WallCommon
            print(property_set.Name)


    return result
print("For now it is only showing how many columns there should be in the file")
