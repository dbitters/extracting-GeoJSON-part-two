# Extracting data from a GeoJSON file (PART TWO)
This project contains a python script that extracts portions of data from a GeoJSON file.  Part one accomplished this by only using string manipulations to extract the necessary data.  In part two, the data was extracted using python's json library so the GeoJSON data could be viewed as dictionaries rather than strings.



#### Objectives
Using dictionaries:
1. Extract state names
2. Extract state FIPS codes
3. Extract the area of each state
4. Report on the following statistics:
    * Longitude Minimum
    * Longitude Maximum
    * Latitude Minimum
    * Latitude Maximum


#### Formatted Output
Showing a portion of the output:

![](img/extracted_states_img_dict)