import wget
import os
import shutil


#HRRR_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d
#.pl?file=hrrr.t00z.wrfsfcf05.grib2&all_lev=on&all_var=on&subregion=&l#
#eftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fhrrr.20191019%2Fconus'
LEFTLON = -123.76
RIGHTLON = -122.0
TOPLAT = 38.0
BOTTOMLAT = 36.0
RUNTIME = 0
HOUR = 0
DAY = 28
MONTH = 10
YEAR = 2019

# hour from 0 - 18
# model is run every hour.
# day must be today or yesterday, else error.
def buildHRRRUrl(leftLon, rightLon, topLat, bottomLat, runtime, hour, day, month, year):
        return ('https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?file=hrrr.t' +
                '%02d'%runtime +
                'z.wrfsfcf' +
                '%02d'%hour +
                '.grib2&all_lev=on&all_var=on&subregion=&leftlon=' +
                str(leftLon) +
                '&rightlon=' +
                str(rightLon) +
                '&toplat=' +
                str(topLat) +
                '&bottomlat=' +
                str(bottomLat) +
                '&dir=%2Fhrrr.' + str(year) + str(month) + str(day) + '%2Fconus')

x = buildHRRRUrl(LEFTLON, RIGHTLON, TOPLAT, BOTTOMLAT, RUNTIME, HOUR, DAY, MONTH, YEAR)

filename = 'hrrr.t' + '%02d'%RUNTIME + 'z.wrfsfcf' + '%02d'%HOUR + '.grib2'
print(x)
wget.download(x)


