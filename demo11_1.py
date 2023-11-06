#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo11_1.py
#    Author: Shawn Hutchinson
#    Description:  Implement an insert cursor
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

# Create insert cursor and add a row
with arcpy.da.InsertCursor(inFc, fields) as cursor:
    cursor.insertRow(["ADD NAME", "ADD CATEGORY", "ADD DESCRIPTION"])    