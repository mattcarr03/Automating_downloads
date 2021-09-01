# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:50:24 2019

@author: matth
"""

"""
This is a script to automate the download of ESA Sea Surface Temperature Climate Change Initiative (https://catalogue.ceda.ac.uk/uuid/62c0f97b1eac4e0197a674870afe1ee6). The script is currently setup to download the full domain and the date range can be changed with the users inputs.

The user inputs are as follows: 

start_date/end_date - the date range that need to be downloaded 
path_to_save - the path to the file where the data should be stored
my_url = the url where the data is stored
short_name = the name used to identify the product

The intial setup/python packages required are:

datetime - pip install datetime 
(https://pypi.org/project/DateTime/)

pandas - pip install pandas
(https://pandas.pydata.org/)

numpy - pip install numpy 
(https://numpy.org/)

netCDF4 - pip install netCDF4
(https://pypi.org/project/netCDF4/)


"""

#####################################
#Importing neccessary python packages
#####################################

import numpy as np
import requests
import shutil
import urllib3
import pandas as pd 
import datetime 
import netCDF4 as nc4

##############
# User inputs
##############

start_date="1981-09-01"
end_date="1981-09-02"

path_to_save='/home/matthew/Documents/Python_scripts/Automating_downloads/Github/'

my_url = "http://data.ceda.ac.uk/neodc/esacci/sst/data/CDR_v2/Analysis/L4/v2.1/"
short_name = "-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_CDR2.1-v02.0-fv01.0.nc"

#Creating date range
dates = pd.date_range(start=start_date,end=end_date,freq='D')

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
        +short_name)
    
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


