# mountain-traffic
How do traffic patterns differ across mountain passes in Washington state?
What is the busiest time of day to travel, and does it vary seasonally?

The ultimate goal is to make a simple app that will let the user look up
a mountain pass and see the historical traffic data for a given time of 
year. Is it more useful to group the traffic data by day of week or by 
some other variable? Knowing how to group the data is the first 
step towards making the app.

## Dependencies
- Python 3 (numpy, matplotlib, pandas, datetime, scipy, requests, zipfile)

## Data
- Traffic data comes from [Washington State Department of Transportation (WSDOT)](http://www.wsdot.wa.gov/data/tools/geoportal/?config=traffic)
- Weather data comes from [NOAA Land-Based Station Data](https://www.ncdc.noaa.gov/data-access/land-based-station-data) 

## Scripts
- `pull_data.py` - Pulls traffic and weather data from the above sources
- `hourly_traffic_I90.ipynb' - Looks at hourly traffic patterns across Snoqualmie Pass
- `weather_vs_traffic.ipynb' - Compares temperature to traffic

## Libraries
- `weatherlib.py` - Converts GHCN daily weather data to a pandas dataframe 
