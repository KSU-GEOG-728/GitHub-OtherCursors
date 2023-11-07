#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo11_4.py
#    Author: Shawn Hutchinson
#    Description:  Implement an update cursor and geometry token
#    Date created: 11/07/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy
from arcpy import env

# Define key environment settings:
env.workspace = "D:/GitHub/GitHub-OtherCursors/DemoData.gdb"
env.overwriteOutput = True

# Establish local variable(s)
inFc = "kansas_wonders_1"
field = "Name"
value = "Kansas State University"
whereClause = """{0} = '{1}'""".format(arcpy.AddFieldDelimiters(inFc, field), value)
ptList = [[-96.583091, 39.1189715]]

# Create update cursor and update SHAPE@ with new point geometry
with arcpy.da.UpdateCursor(inFc, "SHAPE@", whereClause) as cursor:
    for row in cursor:
        for pt in ptList:
            inPoint = arcpy.Point(pt[0], pt[1])
            cursor.updateRow(arcpy.PointGeometry(inPoint))
