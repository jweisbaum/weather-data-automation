import os
import csv
from datetime import date

def row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)

#Constants:
#Default log location for Expedition.
LOG_LOCATION = "c:\ProgramData\Expedition\log\\"
#Boat name
BOAT_NAME = "Angelique"
#Radio Callsign
RADIO_CALLSIGN = "WXPQXR"

#Get the most recent log file.
today = date.today().strftime("%Y%b%d")
filename = today + '.csv'

#Open the log and get the last line as a dictionary.
last_row = {}
with open(LOG_LOCATION + filename, 'r') as log_file:
    csv_reader = csv.DictReader(log_file, delimiter=',')
    for row in csv_reader:
        if row['Boat'] == BOAT_NAME and row['Lat'] is not None:
            last_row = row

kml_string = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>  
    <Style id="boatLocationStyle">
        <IconStyle>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/shapes/track.png</href>
            </Icon>
            <heading>~HEADING~</heading>
        </IconStyle>
    </Style>
    <Placemark>
        <styleUrl>#boatLocationStyle</styleUrl>
        <name>~BOAT~</name>
        <description>
            <h3>You are here.</h3>
            <p>Time UTC: ~TIME~</p>
            <p>Latitude: ~LATITUDE-STRING~</p>
            <p>Longitude: ~LONGITUDE-STRING~</p>
            <h4>*Derived Values*</h4>
            <p>SOG: ~SOG~</p>
            <p>COG: ~COG~</p>
            <p>AWA: ~AWA~</p>
            <p>AWS: ~AWS~</p>
            <p>TWA: ~TWA~</p>
            <p>TWS: ~TWS~</p>
            <p>TWD: ~TWD~</p>
        </description>
        <Point>
            <coordinates>~LON~,~LAT~</coordinates>
        </Point>        
    </Placemark>
</Document>
</kml>
"""

output = kml_string.replace('~HEADING~',str(row['HDG'])).replace('~LAT~',str(row['Lat'])). \
replace('~LON~', str(row['Lon'])).replace('~BOAT~', BOAT_NAME).replace('~LATITUDE-STRING~',str(row['Lat'])). \
replace('~LONGITUDE-STRING~',str(row['Lon'])).replace('~TIME~',str(row['Utc'])). \
replace('~SOG~',str(row['SOG'])). \
replace('~COG~',str(row['COG'])). \
replace('~AWA~',str(row['AWA'])). \
replace('~AWS~',str(row['AWS'])). \
replace('~TWA~',str(row['TWA'])). \
replace('~TWS~',str(row['TWS'])). \
replace('~TWD~',str(row['TWD']))
output_file = open('my_location.kml', 'w+')
output_file.write(output)

output_file.close()

# ToDo: Replace utc date string w/ helpful time.
# ToDo: Make this robust against multiple boats.
# ToDo: Parse a series of logs to a path kml.
# ToDo: Set camera zoom level so it's centered when you open it.
# ToDo: Add callsign.
# ToDo: Read boat stats from a config file.
# ToDo: Make this into an api so you can pull all the data you want. Also put it in a database so that it's more performant. Maybe rewrite in C# for Wsindows.
# ToDo: Read the string in from a template file. 
