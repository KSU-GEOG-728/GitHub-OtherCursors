#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo11_6.py
#    Author: Shawn Hutchinson
#    Description:  Implement an insert cursor to insert a polygon into a new feature class
#    Date created: 11/06/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy, fileinput

# Establish local variable(s)
outPath = "D:/GitHub/GitHub-OtherCursors/DemoData.gdb"
outFc = "GeographyPolygon"
targetFc = "kansas_wonders_geog"
inFile = "D:/GitHub/GitHub-OtherCursors/points.txt"
array = arcpy.Array()
point = arcpy.Point()

# Define key environment settings:
arcpy.env.workspace = outPath
arcpy.env.overwriteOutput = True

# Create a new empty feature class to receive new geometry feature(s)
arcpy.CreateFeatureclass_management(outPath, outFc, "Polygon", "", "", "", targetFc)

# Create insert cursor and iterate through each line in input file
with arcpy.da.InsertCursor(outFc, "SHAPE@") as cursor:
	for line in fileinput.input(inFile):
		point.ID, point.Y, point.X = line.split()
		array.add(point)
	polygon = arcpy.Polygon(array)
	cursor.insertRow([polygon])

# Close input file
fileinput.close()