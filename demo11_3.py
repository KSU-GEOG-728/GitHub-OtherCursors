#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo11_3.py
#    Author: Shawn Hutchinson
#    Description:  Implement a search cursor and geometry token
#    Date created: 11/06/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy
from arcpy import env

# Define key environment settings:
env.workspace = "D:/GitHub/GitHub-OtherCursors/DemoData.gdb"
env.overwriteOutput = True

# Establish local variable(s)
inFc = "kansas_wonders_1"
field = "Category"
value = "Original"
##whereClause = "'Category' = 'Original'"
whereClause = """{0} = '{1}'""".format(arcpy.AddFieldDelimiters(inFc, field), value)

# Create search cursor and retrieve/print coordinate values
with arcpy.da.SearchCursor(inFc, "SHAPE@XY", whereClause) as cursor:
    for row in cursor:
        x, y = row[0]
        print("{0}, {1}".format(x, y))