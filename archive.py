import os

t = ['06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
'18', '19', '20', '21', '22']

d = ['25', '26', '27', '28', '29', '30', '31']
i = 0
for day in d:
    url = 'https://pando-rgw01.chpc.utah.edu/hrrr/sfc/201705' + day
    for time in t:
        url_to_use = url + '/hrrr.t' + time + 'z.wrfsfcf00.grib2'
        curl_string = 'curl ' + url_to_use + ' --output temp.grib2'
        os.system(curl_string)
        os.system('wgrib2 temp.grib2 -small_grib -126:-116 31:35 ' +   '2017_05_' + day + '_' + time + '_small.grib2')
        os.system('rm temp.grib2')


