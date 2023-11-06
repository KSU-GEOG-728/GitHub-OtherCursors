#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo10_1.py
    Author: Shawn Hutchinson
    Description:  Implement a search cursor with a single field.
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
featureClass = "census2k"
totalPopulation = 0
recordsCounted = 0

# Create search cursor to iterate rows and sum population
with arcpy.da.SearchCursor(featureClass, "PEOPLE") as cursor:
    for row in cursor:
        totalPopulation += row[0]
        recordsCounted += 1	 

# Calculate and print average population as an integer
average = totalPopulation / recordsCounted
print("Average for field 'PEOPLE' is {0}".format(round(average, 1)))
