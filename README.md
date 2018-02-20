# mountain-traffic
How do traffic patterns differ across mountain passes in Washington state?
What is the busiest time of day to travel, and does it vary seasonally?

The ultimate goal is to make a simple app that will let the user input
a particular date and see the predicted traffic patterns for that day. 
Thus far, I have focused on data wrangling, determining patterns in the data, 
and determining possible features to describe those patterns. I have determined 
that the following features will be important for the model: daylight hours, 
holiday, ski area open, week day, and travel direction. The next step is to use 
supervised learning, starting with multi-target regression, to determine hourly 
vehicle counts for a training dataset, followed by model validation.

Feedback is appreciated!

## Dependencies
- Python3 (numpy, matplotlib, scipy, pandas, requests, zipfile, html2text, datetime, calendar,)

## Data
- Traffic data (hourly speed, vehicle count, and vehicle type) from [Washington State Department of Transportation (WSDOT)](http://www.wsdot.wa.gov/data/tools/geoportal/?config=traffic)
- Weather data from [NOAA Land-Based Station Data](https://www.ncdc.noaa.gov/data-access/land-based-station-data) 
- Sunrise and Sunset times from [USNO Sun or Moon Rise/Set Table for One Year](http://aa.usno.navy.mil/data/docs/RS_OneYear.php#forma)
- Geospatial Data from [WSDOT GIS Data Download](http://www.wsdot.wa.gov/mapsdata/geodatacatalog/)

## Scripts
- `pull_data.py` - Pulls traffic and weather data from the above sources
- `hourly_traffic_*.ipynb` - Looks at hourly traffic patterns
- `weather_vs_traffic_*.ipynb` - Compares temperature to traffic
- `monthly_patterns.ipynb` - Bins traffic data by month, travel direction, and day of week

## Libraries
- `weatherlib.py` - Converts GHCN daily weather data to a pandas dataframe 
