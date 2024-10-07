# About the group

Students:
    -Ioana Alexandra Udangiu: s237221
    -Yao Tong: s232288
'I am confident coding in Python': 1
Group's 27 focus area is "Structural". The group will focus on column related information processing. The group is an analyst group focusing on designing a tool.

# Claim

The group will focus on Building #2406. The claim that will be checked can be found on page 20 of the document 'CES_BLD_24_06_Client'. The verification consists of checking whether or not the cross sectional dimensions of the columns on a specific floor match the client's dimensional requirements for the specific floor. The claim focuses on the floors above groundfloor. The importance of the check is closely related to visual aspects of the space on each floor as well as structural integrity of the building.

# Use Case
 * How would you check this claim?
 The group will create a function that has as input the model of the building. Inside the function, an array containing the client's requirements for column dimensions will be used to compare this data with the one from the model. A 'for loop' will be used to extract the column dimensions for each floor from the model and perform the comparison with the client's data. The function will return a message stating which columns do not match the dimensions or that all dimensions fulfill the criteria.
 * When will this claim be checked?
 The claim will be checked after all the column dimesnions have been updated in the model, after the final design phase.
  * What information does this claim rely on?
 The claim relies on the column names and the GlobalID present in the model as well as the element properties in order to idetify the depth and width of the cross section.
  * What phase? planning, design, build or operation.
 The tool is meant to be used in the design phase as a verification of the client's requirements.
  * What BIM purpose is required? Gather, generate, analyse, communicate or realise?
 In order to check the claim, it is required to analyse the existing data in order to communicate whether or not the client's requirements are fulfilled.
  * Review use case examples - do any of these help?, What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one.
  The most relevant existing BIM use case is '07 Design Review'.
  
# Tool Idea
 * Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python.
The tool will check the existing data from the model with the client's requirements. In this case, we will focus on the column's cross sectional area for each floor.
 * What is the business and societal value of your tool?
 The tool will reduce the chance of making possible mistakes in the design phase and review phases, which could lead to reduce costs of redesign.
 
# Information Requirements
 * Where is this in IFC?
 The information can be found under the 'Attributes' and 'Property Sets' for each column. From there, the Level, columnID and dimensions can be extracted for the analysis.
 * Is it in the model?
 Yes, the existing model has been checked and all the required data should be provided by the model.
 * Do you know how to get it in ifcOpenShell?
 The following function will be used to get the property sets for the columns: 'ifcopenshell.util.element.get_psets(column, psets_only=True)'. The depth, width and GlobalID will be stored in different arrays in order to be checked.
 * What will you need to learn to do this?
 It will be required to learn element of arrays extraction and comparison and further use of the 'get_psets' function of ifcopenshell.
 * Software license
 The license used will be 'Academic Free License v3.0' as it preserves the intelectual propertity of the creator and it also allows for modification and distribution of the software in both original and used forms.

 

