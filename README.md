# weather_data_automation
Python scripts to grab useful weather data. 

docker build .
docker images
docker run -it --name weather --mount type=bind,source=$(pwd),target=/data 01702f91fa34 /bin/bash