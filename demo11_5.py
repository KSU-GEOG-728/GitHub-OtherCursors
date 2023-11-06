#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo11_5.py
#    Author: Shawn Hutchinson
#    Description:  Implement an insert and update cursor to add row with attributes and geometry
#    Date created: 11/06/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy
from arcpy import env

# Define key environment settings:
env.workspace = "D:/GitHub/GitHub-OtherCursors/DemoData.gdb"
env.overwriteOutput = True

# Establish local variable(s)
inFc = "kansas_wonders_2"
fields = ["NAME", "CATEGORY", "DESCRIPTION", "SHAPE@"]
value = "ADD NAME"
whereClause = """{0} = 'ADD NAME'""".format(arcpy.AddFieldDelimiters(inFc, fields[0]))
ptList = [[-96.583091, 39.1189715]]

# Create insert cursor and insert a new row with "starter" attributes
with arcpy.da.InsertCursor(inFc, fields[0]) as cursor:
    cursor.insertRow([value])

# Create point geometry object
for pt in ptList:
    inPoint = arcpy.Point(pt[0], pt[1])

# Create update cursor and update attributes and SHAPE@ with new point geometry
with arcpy.da.UpdateCursor(inFc, fields, whereClause) as cursor:
    for row in cursor:
        row[0] = "Kansas State University"
        row[1] = "Education"
        row[2] = "Kansas State University was established in 1863 and is the nation's first operational land grant university."
        row[3] = inPoint
        cursor.updateRow(row)