FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install tesseract-ocr -y \
        python3 \
    	python-setuptools \
    	python3-pip \
    	gfortran \
    	gcc \
	wget \
	make \
	build-essential \
	checkinstall \
	libx11-dev \
	libxext-dev \
	zlib1g-dev \
	libpng12-dev \
	libjpeg-dev \
	libfreetype6-dev \
	libxml2-dev \
    && apt-get clean \
    && apt-get autoremove \
    && wget http://www.ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz

ENV CC gcc
ENV FC gfortran
ENV USE_NETCDF3 0
ENV USE_NETCDF4 0

RUN tar -xzf wgrib2.tgz \
  && cd grib2 \
  && make
RUN cp grib2/wgrib2/wgrib2 /usr/local/bin

RUN cd /opt \
    && wget http://www.imagemagick.org/download/ImageMagick.tar.gz \
    && tar xvzf ImageMagick.tar.gz \
    && cd ImageMagick-7.0.9-1 \
    && touch configure \
    && ./configure \
    && make \
    && make install \
    && ldconfig /usr/local/lib \
    && make check

VOLUME weather

