# Script to pull archived HRRR for daytime hours for the region 
# around the start of the Tahiti Transpac and Los Angeles.
# Only three years of data is available. 
# This script excerpts the correct region of interest and the wind and
# pressure values, and saves a new compressed grib. We take only the t00
# forecast for every hour between around 6 am and 11 pm for the dates
# between May 20th and June 8th.

import os

y = ['2017', '2018', '2019']
t = ['06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
'18', '19', '20', '21', '22', '23']
d = ['20', '21', '22', '23','24','25', '26', '27', '28', '29', '30', '31']

for year in y:
    for day in d:
        url = 'https://pando-rgw01.chpc.utah.edu/hrrr/sfc/' + year + '05' + day
        for time in t:
            filename = year + '_05_'+ day + 'hrrr.t' + time + 'z.wrfsfcf00'
            filename_temp = filename + '_temp.grib2'
            filename_final = filename + '.grib2'
            url_to_use = url + '/hrrr.t' + time + 'z.wrfsfcf00.grib2'
            curl_string = 'curl ' + url_to_use + ' --output ' + filename_temp
            os.system(curl_string)
            os.system("wgrib2 "+ filename_temp + " -match '^(8|9|10|11|14|15|45|59|60|61):' -grib filtered.grib2")
            os.system("wgrib2 filtered.grib2  -set_grib_type c2 -small_grib -126:-116 32:35 "  + filename_final)
            os.system('rm filtered.grib2')
            os.system('rm ' + filename_temp)

dj = ['01', '02', '03', '04', '05', '06', '07']
for year in y:
    for day in dj:
        url = 'https://pando-rgw01.chpc.utah.edu/hrrr/sfc/' + year + '06' + day
        for time in t:
            filename = year + '_06_'+ day + 'hrrr.t' + time + 'z.wrfsfcf00'
            filename_temp = filename + '_temp.grib2'
            filename_final = filename + '.grib2'
            url_to_use = url + '/hrrr.t' + time + 'z.wrfsfcf00.grib2'
            curl_string = 'curl ' + url_to_use + ' --output ' + filename_temp
            os.system(curl_string)
            os.system("wgrib2 "+ filename_temp + " -match '^(8|9|10|11|14|15|45|59|60|61):' -grib filtered.grib2")
            os.system("wgrib2 filtered.grib2  -set_grib_type c2 -small_grib -126:-116 32:35 "  + filename_final)
            os.system('rm filtered.grib2')
            os.system('rm ' + filename_temp)
