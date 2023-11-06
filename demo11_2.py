#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo11_2.py
#    Author: Shawn Hutchinson
#    Description:  Implement an update cursor
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
fields = ["NAME", "CATEGORY", "DESCRIPTION"]
##whereClause = "'Name' = 'ADD NAME'"
whereClause = """{0} = 'ADD NAME'""".format(arcpy.AddFieldDelimiters(inFc, fields[0]))

# Create update cursor and update row values
with arcpy.da.UpdateCursor(inFc, fields, whereClause) as cursor:
    for row in cursor:
        row[0] = "Kansas State University"
        row[1] = "Education"
        row[2] = "Kansas State University was established in 1863 and is the nation's first operational land grant university."
        cursor.updateRow(row)