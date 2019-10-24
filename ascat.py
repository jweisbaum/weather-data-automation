import wget
import os

wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBas50.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBas51.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBas38.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBas39.png")

os.rename("WMBas50.png", "MetopA-As-WMBas50.png")
os.rename("WMBas51.png", "MetopA-As-WMBas51.png")
os.rename("WMBas38.png", "MetopA-As-WMBas38.png")
os.rename("WMBas39.png", "MetopA-As-WMBas39.png")

wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBds50.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBds51.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBds38.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopA/WINDS/cur_25km/zooms/WMBds39.png")
os.rename("WMBds50.png", "MetopA-Ds-WMBas50.png")
os.rename("WMBds51.png", "MetopA-Ds-WMBas51.png")
os.rename("WMBds38.png", "MetopA-Ds-WMBas38.png")
os.rename("WMBds39.png", "MetopA-Ds-WMBas39.png")


wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBas50.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBas51.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBas38.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBas39.png")

os.rename("WMBas50.png", "MetopB-As-WMBas50.png")
os.rename("WMBas51.png", "MetopB-As-WMBas51.png")
os.rename("WMBas38.png", "MetopB-As-WMBas38.png")
os.rename("WMBas39.png", "MetopB-As-WMBas39.png")

wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBds50.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBds51.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBds38.png")
wget.download("https://www.ospo.noaa.gov/data/atmosphere/ascat/MetopB/WINDS/cur_25km/zooms/WMBds39.png")

os.rename("WMBds50.png", "MetopB-Ds-WMBas50.png")
os.rename("WMBds51.png", "MetopB-Ds-WMBas51.png")
os.rename("WMBds38.png", "MetopB-Ds-WMBas38.png")
os.rename("WMBds39.png", "MetopB-Ds-WMBas39.png")
