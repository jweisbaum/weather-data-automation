# https://www.starpath.com/downloads/Sat-Image-Briefing.pdf
# GOES infrared satellite images of the Pacific. Updated every 6 hours.
import wget

wget.download("https://tgftp.nws.noaa.gov/fax/evpz11.jpg")
wget.download("https://tgftp.nws.noaa.gov/fax/evps11.jpg")
wget.download("https://tgftp.nws.noaa.gov/fax/evpn10.jpg")

