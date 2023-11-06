#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo10_6.py
    Author: Shawn Hutchinson
    Description:  Example 2 of implementing a search cursor with a where clause and field delimiters.
    Date created: 09/13/2023
    Python Version: 3.9.16
"""

# Import required modules and classes:
import arcpy
from arcpy import env

# Define key environment settings:
env.workspace = "D:/GitHub/GitHub-SearchCursors/DemoData.gdb"
env.overwriteOutput = True

# Establish local variable(s)
featureClass = "parks"
fieldName = "NAME"
parkValue = "CiCo Park"
whereClause = """{0} = '{1}'""".format(arcpy.AddFieldDelimiters(featureClass, fieldName), parkValue)

# Create search cursor and iterate through all rows to find specified park and address
with arcpy.da.SearchCursor(featureClass, ["NAME", "ADDRESS"], whereClause) as cursor:
    for row in cursor:
        print("The facility {0} is located at {1}.".format(row[0], row[1]))

# Finally, confirm the structure of the where clause
print(whereClause)