from ifcopenshell.util import element

def checkRule(model, specific_floor_level, req_depth, req_width):
    # Retrieve all columns from the model
    columns = model.by_type("IfcColumn")

    all_columns_match = True  # Flag to track if all columns meet requirements
    non_matching_columns = []  # List to store GlobalIDs of non-matching columns

    # Loop through each column in the model
    for column in columns:
        # Retrieve the property sets (psets) of the column
        column_properties = element.get_psets(column, psets_only=True)

        # Initialize variables for Depth, Width, and floor level
        depth = None
        width = None
        floor_level = None

        # Debug: Print column GlobalID
        global_id = column.GlobalId

        # Loop through property sets to extract Depth and Width
        for pset_name, pset_props in column_properties.items():
            if 'Depth' in pset_props:
                depth = float(pset_props['Depth'])
            if 'Width' in pset_props:
                width = float(pset_props['Width'])
            
        # Retrieve the floor level (elevation) for the column
        if column.ContainedInStructure:
            for rel in column.ContainedInStructure:
                if rel.is_a("IfcRelContainedInSpatialStructure"):
                    storey = rel.RelatingStructure
                    if storey.is_a("IfcBuildingStorey"):
                        # Attempt to get elevation; fallback to name if not found
                        try:
                            floor_level = float(storey.Name)
                        except (TypeError, ValueError):
                            # Extract floor number from the name as a fallback, if needed
                            floor_name = storey.Name
                            if floor_name and floor_name.lstrip('Level ').replace('.', '').isdigit():
                                floor_level = float(floor_name.split()[-1])
    
        # Check the requirements 
            if floor_level == specific_floor_level:
                # Check if the column dimensions match the requirements
                if depth == req_depth and width == req_width:
                    all_columns_match = True
                else:
                    all_columns_match = False  # Set flag to False
                    non_matching_columns.append(global_id)  # Store GlobalID of the non-matching column
                    print(f"The column with GlobalID {global_id} does NOT match the requirements. "
                          f"Expected: {req_depth}x{req_width}, Found: {depth}x{width}")

    # Final output message
    if all_columns_match == True:
        print("All columns on the specified floor match the requirements.")
    else:
        print("Some columns on the specified floor do not match the requirements.GlobalIDs of non-matching columns:", non_matching_columns)

import ifcopenshell
model = ifcopenshell.open("C:/Users/Alexandra/Desktop/SCHOOL/DTU_Education/SEM1/Advanced_BIM/LECTURE 1/CES_BLD_24_06_STR.ifc")

# Example
specific_floor_level = 8  # Replace with the desired floor level elevation
req_depth = 420  # Replace with the required depth for the specific floor
req_width = 420  # Replace with the required width for the specific floor

checkRule(model, specific_floor_level, req_depth, req_width)
#The code checks that all the columns on a given floor match the dimensions given by the user. It should print out a message if all match the requirements or it should print out the GlobalID of the columns tht do not together with a message.