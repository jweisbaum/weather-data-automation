FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install tesseract-ocr -y \
        python3 \
    	python-setuptools \
    	python3-pip \
    	gfortran \
    	gcc \
	wget \
    && apt-get clean \
    && apt-get autoremove \
    && wget http://www.ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz \
    && gunzip wgrib2.tgz \
    && tar -xvf wgrib2.tar \
    && cd grib2 \
    && export CC=gcc \
    && make \
    && cp grib2/wgrib2/wgrib2 /usr/local/bin


CMD ["python3","OCRRun.py"]