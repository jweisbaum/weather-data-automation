import wget
import sys
import os
import re
import tarfile

tao_url = 'https://tao.ndbc.noaa.gov/tao/data_download/process_results.php?type=wind&reso=hres&year1=2019&mon1=10&day1=08&year2=2019&mon2=10&day2=23&format=subcdf&compression=gzip&stations=T8S170W.T5S170W.T2S170W.T0N170W.T2N170W.T5N170W.T8N170W.T8S155W.T5S155W.T2S155W.T0N155W.T2N155W.T5N155W.T8N155W.T5S140W.T2S140W.T0N140W.T2N140W.T5N140W.T9N140W.T8S125W.T5S125W.T2S125W.T0N125W.T2N125W.T5N125W.T8N125W.T8S110W.T5S110W.T2S110W.T0N110W.T2N110W.T5N110W.T8N110W'

wget.download(tao_url)
with open('process_results.php') as fp:
    content = fp.read()
    
    matches = re.findall('.*<td>Download one <a href="(cache/[0-9]*/.*\.tar\.gz)">compressed.*', content)
    url_of_data = 'https://tao.ndbc.noaa.gov/tao/data_download/' + matches[0]
    print(url_of_data)
    wget.download(url_of_data)
    filename = re.match('https://tao.ndbc.noaa.gov/tao/data_download/cache/[0-9]*/(.*\.tar\.gz)', url_of_data).group(1)
    print(filename)
    tar = tarfile.open(filename, "r:gz")
    tar.extractall('gribs')
    tar.close()
    fp.close()
    
