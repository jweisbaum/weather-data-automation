# weather-data-automation
Python scripts to grab useful weather data.

Run these scripts using [this Docker image.](github.com/jweisbaum/weather-and-gis-docker)  

These scripts and data sources are meant to help ocean navigators prepare for offshore races.  

# Contents
## server.py
This runs locally on your Windows machine on port 8080 (not on Docker). Submitting a GET request to the server returns a bunch of information about your boat such as COG, SOG, LAT, LON, etc. The information comes from the Expedition DLL so you must be running Expedition. This enables anyone with Expedition to build custom apps accessible over their local wifi. 

## scripts/expedition_to_kml.py
Finds the last entry of your expedition log for your boat and generates a KML file to view in Google Earth. 

## scripts/get_hrrr_tahiti_start_archive.py
Downloads the hrrr t00 forecast for daylight and evening hours for May 20th - June 7th, for the years 2017, 2018, and 2019. Parses and saves the wind and pressure data for the region around Los Angeles and deletes everything else. 

## data/ybcodes.csv
A list of over 1000 YB codes for numerous ocean races, legs and returns. 

# Use at your own risk.

Be advised: these scripts are used at your own risk, and I take no responsibility for any issues arrising from using them to navigate. 
- There are no formal testing or validation procedures in place.  
- It is possible that a script:
    - Bricks your computer,  
    - Messes up your Expedition log,  
    - Downloads so much data that your computer becomes slow,  
    - Downloads so much data that your satellite internet bill is astronomical,  
    - Gives you the wrong information, such as an outdated location or heading,  
    - Gets your IP banned from a weather data server,
    - Has some other bug that makes you have a really bad day in an unforseen way.  

I am not responsible for any of the above, though I am developing these for my own purposes.  Please take the time to understand these scripts before you use them or alter them for your needs.



