Describe the use case you have chosen. 

Our group will focus on Building #2406. The cross-sectional dimensions of columns on the specific floor which is above the ground floor will be extracted to compare with the dimensional requirements of client report 'CES_BLD_24_06_Client'. Our use case is ‘Design review’. 

Who is the use case for? 

The use case is for inspectors, structural engineers, and architects who are involved in quality insurance and verification process. 

What disciplinary (non BIM) expertise do you use to solve the use case? 

The group uses python and IFCOpenShell in order to make the code for the tool. The tool does not require any engineering knowledge. 

What IFC concepts do you need to use in your script (or would you use in the rest of the tool)? 

“ifcopenshell.open(‘file.ifc’).by_type(“IfcColumn”)” is used to get all column entities in the IFC model. This allows us to loop through each instance in the model. Then, the function 'get_psets' is used to pull property sets such as width, depth and GlobalID. The ‘rel.’ is used to get the elevation for the columns. 

What disciplinary analysis does it require? 

Structural engineering expertise is required to verify that the dimensions of the columns meet load-bearing and stability requirements. The architectural analysis ensure that column dimensions do not disrupt the intended aesthetic or functionality of the interior layout. Data analyses are required to script and implement computational checks on the extracted column dimensions and compare the extracted data against client requirement. 

What building elements are you interested in? 

The focus is the columns, as their cross-sectional dimensions are being checked to ensure they meet the client’s requirements. 

What is the input data for your use case? 

The use case relies on the column’s GlobalID present in the model as well as the element properties in order to identify the cross-sectional dimensions. The code does not check whether the information required exists already. 

What (use cases) need to be done before you can start your use case? 

Structural Analysis, Code Validation and Design Review for the other disciplines. 

What other use cases are waiting for your use case to complete? 

Digital fabrication and record modelling. 

 