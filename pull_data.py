# Pulls and saves traffic data from Washington State Traffic GeoPortal in a local 
# directory called 'traffic_data'. If that directory does not exist, the 
# directory is created.
#
# Laura Kehrl, UW, 2 Feb 2018

import requests, zipfile, io, os
import weatherlib

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



