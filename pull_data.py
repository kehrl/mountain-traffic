# Pulls and saves traffic data from Washington State Traffic GeoPortal in a local 
# directory called 'traffic_data'. If that directory does not exist, the 
# directory is created. It also pulls weather data from a local station
# in Seattle and gets sunrise/sunset times.
#
# Laura Kehrl, UW, 2 Feb 2018

import requests, zipfile, io, os
import weatherlib
import numpy as np
import html2text

# Traffic Sites
I90 = ['S901','R039W','S903','B04']
SR2 = ['R038','R058E','R047WW']

# Weather sites
weather_sites = ['USW00024233','USS0021B55S']

# Check to see if the local data directory exists
if not(os.path.isdir('traffic_data')):
    os.mkdir('traffic_data')
    os.mkdir('weather_data')

# Download weather data
for site in weather_sites:
    url = 'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/all/'+site+'.dly'
    os.system('curl -o weather_data/'+site+'.dyl '+url)
    weather_data = weatherlib.read_dyl('weather_data/'+site+'.dyl')
    weather_data.to_csv('weather_data/'+site+'.csv')

# Download sunrise/sunset data
years = np.arange(2007,2018)
for year in years:
    url = 'http://aa.usno.navy.mil/cgi-bin/aa_rstablew.pl?ID=AA&year='+str(year)+\
            '&task=0&state=WA&place=Seattle'
    resp = requests.get(url,allow_redirects=True)
    fid = open('weather_data/sunrise_sunset'+str(year)+'.csv','w')
    fid.write(html2text.html2text(resp.text))
    fid.close()

# Download and unzip traffic data
for site in I90+SR2:
    print("Pulling data for traffic site "+site)
    url_zip_file = 'https://www.wsdot.wa.gov/Traffic/API/PermanentTrafficRecorder/'+\
        'api/data/'+site+'/2007/1/2017/12/TrafficVolumeByVehicleByHour'
    resp = requests.get(url_zip_file, stream=True)
    z = zipfile.ZipFile(io.BytesIO(resp.content))
    z.extractall('traffic_data')
    z.close()

# Get some geospatial data for plotting

# Location of freeway exits
url_zip_file = 'http://www.wsdot.wa.gov/mapsdata/geodatacatalog/Maps/noscale/DOT_Cartog/FGTSWA.zip'
resp = requests.get(url_zip_file, stream=True)
z = zipfile.ZipFile(io.BytesIO(resp.content))
z.extractall('traffic_data')
z.close()

# WA highway map
url_zip_file = 'http://www.wsdot.wa.gov/mapsdata/geodatacatalog/maps/NOSCALE/DOT_TDO/LRS/24KLRS_2016.zip'
resp = requests.get(url_zip_file, stream=True)
z = zipfile.ZipFile(io.BytesIO(resp.content))
z.extractall('traffic_data')
z.close()

# Mileage markers
url_zip_file = 'http://www.wsdot.wa.gov/mapsdata/geodatacatalog/Maps/noscale/DOT_TDO/stateroutemileposts.zip'
resp = requests.get(url_zip_file, stream=True)
z = zipfile.ZipFile(io.BytesIO(resp.content))
z.extractall('traffic_data')
z.close()
