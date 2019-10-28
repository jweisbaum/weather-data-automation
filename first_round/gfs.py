import wget

# see https://nomads.ncep.noaa.gov/ for more.
CC = '00'
HOUR = '000'
DAY = '01'
MONTH = '01'
YEAR = '2019'

GFS_25_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t06z.pgrb2.0p25.f001&all_lev=on&all_var=on&subregion=&leftlon=-123&rightlon=-122&toplat=38&bottomlat=37&dir=%2Fgfs.20191019%2F06'

GFS_50_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t00z.pgrb2.0p25.f009&all_lev=on&all_var=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20191019%2F00'

GFS_25_HOURLY_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?file=gfs.t00z.pgrb2.0p25.f000&all_lev=on&all_var=on&subregion=&leftlon=-123&rightlon=-122&toplat=38&bottomlat=37&dir=%2Fgfs.20191019%2F00'

GFS_1_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?file=gfs.t00z.pgrb2.1p00.f006&all_lev=on&all_var=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20191019%2F00'



SST_PACIFIC = 'https://www.ospo.noaa.gov/data/sst/contour/equatpac.REM.fc.gif'
SST_US_PACIFIC = 'https://www.ospo.noaa.gov/data/sst/contour/uspacifi.fc.gif'
SST_CAL = 'https://www.ospo.noaa.gov/data/sst/contour/californ.fc.gif'


       
# filename = wget.download(url)
# cc is run time, which for GFS is either 00, 06, 12, or 18.
# hour is a 3 digit number from 000 to 125
# resolution one of '25', '50', '25_1hr', '00'
def buildGFSUrl(leftLon, rightLon, topLat, bottomLat, resolution, cc, hour, day, month, year):
        p_value = '0p'
        if resolution is '00':
                p_value = '1p'
  
        return ('https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_' + p_value + 
                str(resolution) +
                '.pl?file=gfs.t' +
                '%02d'%cc +
                'z.pgrb2.' + p_value + 
                resolution +
                '.f' +
                '%03d'%hour +
                '&all_lev=on&all_var=on&subregion=&leftlon=' +
                str(leftLon) +
                '&rightlon=' +
                str(rightLon) +
                '&toplat=' +
                str(topLat) +
                '&bottomlat=' +
                str(bottomLat) +
                '&dir=%2Fgfs.' +
                str(year) + str(month) + str(day) + '%2F'+ '%02d'%cc)



# RTOFS: https://polar.ncep.noaa.gov/global/about/product_description.shtml

print(x)


