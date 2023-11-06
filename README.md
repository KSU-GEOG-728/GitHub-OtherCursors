# GitHub-OtherCursors
Exercise for GEOG 728 Programming for Geographic Analysis at Kansas State University

### Instructions:

Accept the GitHub Classroom assignment <code>GitHub-OtherCursors</code> and clone the new repository as a local personal repository.  Uncompress the provided ZIP file to access the ArcGIS Pro project file in your local repository workspace.  The only file which needs to be pushed to origin at the conclusion of the exercise is a single Python script.  There is no requirement to prepare and submit a script-based tool.  Should you encounter difficulties during the week, seek assistance by posting an issue in GitHub.

### Task:

Edit the provided Python file called <code>GitHub-OtherCursors.py</code> to create a new stand-alone script that includes the following features and capabilities.  For this script, there is no requirement to include user-defined inputs or any messaging, except for a custom print message should your script throw an exception (see the requirement below for a "try-except" block):

1. Incorporates an insert cursor to add five new observations of lesser prairie chickens to the existing feature class <code>tympanuchus_pallidicinctus</code>.  Alternatively, you may use the five new observations to create a new feature class and append these to the existing feature class to produce your final input.
2. Uses the Python <code>fileinput</code> module and related methods to read in the new observations in the provided text file <code>newchickens.txt</code>.
3. Incorporates an update cursor to add the species name Tympanuchus pallidicinctus to the "label" field, x- and y-coordinates of each observation to the "long" and "lat" fields, and a value of 1 to the "abundance" field of the new records in the final output.
4. Finishes by computing a minimum bounding polygon as a rough estimate of the species range.  For this, use the ArcPy function "MinimumBoundingGeometry" using the geometry type CONVEX_HULL.  Read the tool help file for this function closely, as it may have special licensing or extension requirements to account for in your script.
5. Includes at least one "try-except" block to trap geoprocessing errors.





1. Incorporates a setting that allows existing output to be overwritten.
2. Creates a list of line-based feature classes in the user-defined workspace (all of the individual major rivers).
3. Uses this list in a loop to select all counties through which at least one of the nine major rivers in the state passes then copies these selected counties to a brand new feature class. The basis for this operation should be <code>arcpy.SelectLayerByLocation_management</code>.  If you are not familiar with this function, [read the help file for it carefully](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/select-layer-by-location.htm).  Note that the input for this function requires a "layer" file and not a feature class.  Accounting for this nuance is essential in stand-alone scripts that perform selections outside of ArcGIS.
4. Prints the geoprocessing messages produced by each geoprocessing tool in the model.
6. Your script should create only one output (intermediate or final) that is written to disk - the "river" counties. Use an appropriate Python os module function to combine the variable outputWorkspace with a hard-coded filename of your choice so that the outputs are written to a workspace other than the current workspace.
7. Includes of some form of "error-trapping" (e.g., try-except, if-else) including use of the ArcPy ExecuteError class to actually trap any geoprocessing errors.
8. Uses a print statement at the successful conclusion to your script that says - “A total of ___ people in Kansas, or ___% of the total population, live in a county intersected by a major river.”  You should populate the blanks with values represented by your local variables “outValue” and “percentPop” using the Python format() function.

For this assignment, modify the script to include a search cursor that sums the total population of all counties in Kansas and the total population of counties through which a major river passes.  Then use these sums to "automate" the final print statement by computing the percentage of the total Kansas population that lives in counties intersected by a major river. Given the use of a search cursor, you do NOT need to produce an output table containing the summary statistic "SUM" from the POP2010 field of the copied counties feature class.

All code requirements outlined in the midterm practical exam also apply here.  The new features of your script will include creation of one or more a search cursor objects and any additional code and variables needed to automate adding the populations of all Kansas counties and calculating the percentage of the total population that lives in a "river county".

## Rubric:

Review the assignment rubric available on Canvas for additional details on how your work will be assessed. Double-check that your script includes a complete header section, uses good commenting, incorporates line spaces between blocks of code, and reads input and writes output to current workspace.

## Submission:

Commit your code changes for <code>GitHub-SearchCursor</code> to your assignment repository on GitHub.
