import wget


HRRR_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?file=hrrr.t00z.wrfsfcf05.grib2&all_lev=on&all_var=on&subregion=&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fhrrr.20191019%2Fconus'


# hour from 0 - 18
# model is run every hour.
def buildHRRRUrl(leftLon, rightLon, topLat, bottomLat, runtime, hour, day, month, year):
        return ('https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?file=hrrr.t' +
                '%02d'%runtime +
                'z.wrfsfcf' +
                '%02d'%hour +
                '&all_lev=on&all_var=on&subregion=&leftlon=' +
                str(leftLon) +
                '&rightlon=' +
                str(rightLon) +
                '&toplat=' +
                str(topLat) +
                '&bottomlat=' +
                str(bottomLat) +
                '&dir=%2Fhrrr.' + str(year) + str(month) + str(day) + '%2Fconus')

x = buildHRRRUrl(-123,-122,38, 37, 0, 3, 12,10, 2019)
