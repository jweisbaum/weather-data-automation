# https://www.wpc.ncep.noaa.gov/sfc/UASfcManualVersion1.pdf
import wget
import shutil

wget.download("https://ocean.weather.gov/UA/OPC_PAC.gif")
wget.download("https://ocean.weather.gov/UA/Pac_Tropics.gif")
wget.download("https://ocean.weather.gov/UA/Pac_Difax.gif")
wget.download("https://ocean.weather.gov/UA/West_coast.gif")

shutil.move('OPC_PAC.gif', 'data/OPC_PAC.gif')
shutil.move('Pac_Tropics.gif', 'data/Pac_Tropics.gif')
shutil.move('Pac_Difax.gif', 'data/Pac_Difax.gif')
shutil.move('West_coast.gif', 'data/West_coast.gif')
