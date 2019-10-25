import wget
import os
import subprocess

grids = ['50']
ascat_urls = ['https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMB',
  'https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMB',
  'https://manati.star.nesdis.noaa.gov/ascat_images/cur_25km_METC/zooms/WMB']
as_des = ['as','ds']

newname = ''
oldname = ''
for index in grids:
    filenumber = 0;
    for url in ascat_urls:
        for direction in as_des:
            to_use = url + direction + index +'.png'
            wget.download(to_use)
            newname = index + '_'  + str(filenumber) + '.png'
            oldname = 'WMB' + direction + index + '.png'
            os.system('convert ' + oldname + ' -transparent white ' + newname)
            os.remove(oldname)
            if(filenumber > 0):
                previous = index + '_'  + str(filenumber-1) + '.png'
                os.system('convert ' + previous + ' ' + newname + ' -gravity center -compose over -composite temp.png')
                os.remove(previous)
                os.remove(newname)
                os.rename('temp.png', newname)
            filenumber+=1
    os.rename(newname, index + '_composite.png')
          
 

#wget.download("https://ftp.opc.ncep.noaa.gov/data/ascat_ab/latest_ascat_swath_data.grb2")
