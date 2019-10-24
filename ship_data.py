import wget
import sys
import os
import re
from datetime import datetime, timedelta


url = 'https://www.ndbc.noaa.gov/ship_obs.php?uom=E&time=12'
wget.download(url)


filename = 'shipreport'
new_file = """<?xml version="1.0" encoding="UTF-8"?>
         <kml xmlns="http://www.opengis.net/kml/2.2"> <Folder>"""

with open('ship_obs.php') as fp:
   for line in fp:
      if '<span style="background-color: #fffff0">SHIP' in line or '<span style="background-color: #f0f8fe">SHIP' in line:
         
         z = re.match('.*SHIP\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+V*R*B*\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+(\+*-*[0-9]*\.*[0-9]*-*)\s+.*', line)
         if z is None:
            print(line)
    
         description = ('Time: ' + z.group(1) + ' UTC\nWind Direction: ' + z.group(4) + ' Deg CW from true N\nWind Speed: ' + z.group(5) + ' kts \nWind Gust: ' + z.group(6) + ' \nWaveheight: ' + z.group(7) + ' ft\nPressure: ' + z.group(9)) + ' in'
         new_file = new_file + """<Placemark>
             <name>Ship Report</name>
             <description>""" + description + """</description>
             <Point> +
               <coordinates>""" + z.group(3) + "," + z.group(2)+"""</coordinates>
             </Point>
           </Placemark>"""
new_file = new_file + "</Folder></kml>"
file = open(filename+'.kml', 'w')
file.write(new_file)
file.close()
      
