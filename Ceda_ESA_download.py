# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:50:24 2019

@author: matth
"""

import numpy as np
import requests
import shutil
import urllib3
import pandas as pd 
import datetime 
import netCDF4 as nc4

start_date="1981-09-01"
end_date="1981-09-02"

path_to_save='/home/matthew/Documents/Python_scripts/Automating_downloads/'

dates = pd.date_range(start=start_date,end=end_date,freq='D')


my_url = "http://data.ceda.ac.uk/neodc/esacci/sst/data/CDR_v2/Analysis/L4/v2.1/"
short_name = "-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_CDR2.1-v02.0-fv01.0.nc"



# First generate a list of url's
print("Downloading data from OPeNDAP ... ")
print("...")
print("...")

data_url = []
cnt = 0
for i in np.arange(0,len(dates)): 
    ii = i+1
    ndays = datetime.datetime(dates[i].year,dates[i].month,dates[i].day)
    num_day =(ndays.strftime('%j'))
    n_month = (ndays.strftime('%m'))
    n_day = (ndays.strftime('%d'))
    n_hour = str(120000)

    data_url.append(my_url + str(dates[i].year) + "/" + str(n_month)+"/"+str(n_day)+"/"+str(str(dates[i].year)+str(n_month)+str(n_day)+str(n_hour))\
        +"-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_CDR2.1-v02.0-fv01.0.nc")
    
    cnt = cnt+1

# Filter out unavailable url's
url_list = data_url

# Loop though url's and download the data
count = 0
for i in url_list:
    
    local_filename = path_to_save+str(dates[count].year)+str('%02d'%dates[count].month)+str('%02d'%dates[count].day)+str(short_name)+'.nc'
    
    url = url_list[count]
    http = urllib3.PoolManager()
    with http.request('GET', url, preload_content=False) as r, open(local_filename, 'wb') as out_file:       
        shutil.copyfileobj(r, out_file)
    count = count+1
    del local_filename


