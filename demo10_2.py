#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo10_2.py
    Author: Shawn Hutchinson
    Description:  Implement a search cursor with list of fields.
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
featureClass = "centerln"

# Create search cursor to iterate rows and sum population
with arcpy.da.SearchCursor(featureClass, ["NAME", "TYPE"]) as cursor:
    for row in cursor:
        print("Street = {0} {1}".format(row[0], row[1]))
        