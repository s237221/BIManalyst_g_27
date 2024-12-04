**Group 27**: Ioana Alexandra Udangiu - s237221
          Yao Tong - s232288

**Focus Area**: Structural

**BIM use case**: Design Review

# Summary

**Title**: Column Dimension Verification Tool for IFC Models
**Summary**: The tutorial describes the functionalities of the code and it explains how to use the tool by providing an example. This efficiently verifies column dimensions in IFC model by comparing them against specified requirements at a designated floor level during structural design.

# Introduction

The following tool uses the data in the model to check the client's requirements of columns cross-sectional dimensions. The function is set up in a way that the user provides the floor level, the path to the ifc model and the column's width and depth required. After verifying all the columns on the specified floor, the code returns a message positive message or a negative one together with theGlobalID of the columns that do not match the requirements so they can be changed.
The tool is intended to be used at the end of the design stage by the project manager and structural engineers to quality control the design and input of the model.
The code uses ifcOpenshell modules and functions.

# Verification of column dimensions based on user specified requirements

The tutorial describes the functionalities of the code and it explains how to use the tool by providing an example. This efficiently verifies column dimensions in IFC model by comparing them against specified requirements at a designated floor level during structural design. By extracting relevant properties, it provides clear feedback on compliance while highlighting any discrepancies for correction, playing a role in design verification phases for project managers and structural engineers.

# Steps in the code

The whole verification happens in one big 'for' loop where all the columns are taken one by one and their geometrical properties are extracted using 'psets' function.

        # Retrieve the property sets (psets) of the column
        column_properties = element.get_psets(column, psets_only=True)

        # Initialize variables for Depth, Width, and floor level
        depth = None
        width = None
        floor_level = None
        global_id = column.GlobalId

        # Loop through property sets to extract Depth and Width
        for pset_name, pset_props in column_properties.items():
            if 'Depth' in pset_props:
                depth = float(pset_props['Depth'])
            if 'Width' in pset_props:
                width = float(pset_props['Width'])

Here, the depth and width are extracted for the first column. The next step is to extract the floor level in which the current column is situated. This is done by using the 'rel' function.

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

Since the 'rel' function is related to the elevation of the column in the model but the user's input is the floor level, it was necessarry to extract the floor level as a number and not an elevation. Therefore, the floor name was also extracted and converted to a float variable.
Now that the floor level and and the depth and width of the column have been extracted from the model, they can be compared with the user provided data using an 'if' function. Moreover, an array that retains the GlobalID's of the non-matching columns has been set up so it can be available for the user at the end of the verification.

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

In this section of the code, a flag variable has been defined. The purpose of the flag variable is to turn 'Flase' when a column is not matching the requirements.
Once, all the columns have been checked, a new verification is performed using the flag variable. If all the columns match the requirements, then the flag variable is 'TRUE' and the message is positive. If there is at least one column that does not match the requirments, the flag variable turns 'FALSE' and a negative message is shown to the user together with all the GlobalIDs of all the non matching columns.

             if all_columns_match == True:
        print("All columns on the specified floor match the requirements.")
    else:
        print("Some columns on the specified floor do not match the requirements.GlobalIDs of non-matching columns:", non_matching_columns)

# How to run the code

In order to get the code to run properly, the ifcOpenshell library needs to be imported and the fucntion needs to be called in a python interpreter software. The function contains four input parameters which need to be provided before calling it: the path to the model's location on the user's PC, the floor level for which the verification is performed and the required depth and width of the columns on the floor.

            #Example
            import ifcopenshell
            model = ifcopenshell.open("C:\file path\.ifc")
            specific_floor_level = 8  # Replace with the desired floor level elevation
            req_depth = 420  # Replace with the required depth for the specific floor
            req_width = 420  # Replace with the required width for the specific floor

            checkRule(model, specific_floor_level, req_depth, req_width)
 
 # Code limitations
 
 The code is currently running under the assumption that all the columns on the required floor have the same dimensions, therefore it does not handle the case when the columns on one floor have different required cross-sections.
 The code does not check whether or not the necessarry information for the verification is available beforehand.
 The code checks the required dimensions only for one floor at the time.

 # Good to know information
 
As first time users of Blender and ifcOpenshell library, we wished we would have known a bit more about how the model in itself is defined. For example, that in order to run code that interprets floor level we need to know that it actually reads elevations and not a specific floor level or how to extract specific values of the properties (the psets function).


