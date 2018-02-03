
def read_dyl(file,elements=['PRCP','SNOW','TMAX','TMIN','TAVG']):
    import pandas as pd
    import numpy as np
    import datetime as dt
    import calendar

    '''
    Script to pull the desired elements from a "FILE FOR DAILY GLOBAL 
    HISTORICAL CLIMATOLOGY NETWORK (GHCN-DAILY)" .dly file. The 
    format is archaic, but we'll make it work.

    Inputs:
    file: name of file
    elements: desired elements (default = ['PRCP','SNOW','TMAX','TMIN','TAVG'])

    Output:
    data: data in a pd.DataFrame
    '''

    fid = open(file,'r')
    lines = fid.readlines()
    fid.close()

    # Output columns
    columns = ['Id','Year','Month','Day','Type','Value']

    # Find date range
    date1 = dt.datetime(int(lines[0][11:15]),int(lines[0][15:17]),1)
    date2 = dt.datetime(int(lines[-1][11:15]),int(lines[-1][15:17]),28)
    days = pd.date_range(date1,date2)

    data = pd.DataFrame(index=range(len(days)*len(elements)),columns=columns)
    ind1, ind2 = 21, 25
    n = 0
    for i in range(0,len(lines)):   
        line = lines[i]
        # Only get the elements we want...
        if line[17:21] in elements:
            year, month = int(line[11:15]), int(line[15:17])
            if month == 12:
                days_in_month = (dt.date(year+1,1,1)-dt.date(year,month,1)).days
            else:
                days_in_month = (dt.date(year,month+1,1)-dt.date(year,month,1)).days
            data['Id'][n:n+days_in_month] = line[0:11]
            data['Year'][n:n+days_in_month] = int(line[11:15])
            data['Month'][n:n+days_in_month] = int(line[15:17])
            data['Type'][n:n+days_in_month] = line[17:21]
            for j in range(0,days_in_month):
                data['Day'][n+j] = j+1
                try:
                    data['Value'][n+j] = np.float(line[ind1+j*8:ind2+j*8])
                except:
                    data['Value'][n+j] = np.float('NaN')
            n = n + days_in_month

    # Get rid of extra rows
    data = data.dropna(how='all')
    
    # Get rid of missing data value
    data = data.replace(-999,np.float('NaN'))

    return data
