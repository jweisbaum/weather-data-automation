# https://www.starpath.com/downloads/Sat-Image-Briefing.pdf
# GOES infrared satellite images of the Pacific. Updated every 6 hours.
import wget
import os
import shutil

wget.download("https://tgftp.nws.noaa.gov/fax/evpz11.jpg")
wget.download("https://tgftp.nws.noaa.gov/fax/evps11.jpg")
wget.download("https://tgftp.nws.noaa.gov/fax/evpn10.jpg")

os.rename('evpz11.jpg', 'goes_pacific_1.jpg')
shutil.move('goes_pacific_1.jpg', 'data/goes_pacific_1.jpg')

os.rename('evps11.jpg', 'goes_pacific_2.jpg')
shutil.move('goes_pacific_2.jpg', 'data/goes_pacific_2.jpg')

os.rename('evpn10.jpg', 'goes_pacific_3.jpg')
shutil.move('goes_pacific_3.jpg', 'data/goes_pacific_3.jpg')
