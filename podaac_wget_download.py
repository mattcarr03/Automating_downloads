# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:50:24 2019

@author: matth
"""

"""
This is a script to automate the download of JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1 from PODAAC JPL (https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1?ids=&values=&search=MUR&provider=PODAAC). The script is currently setup to download the full domain and the date range can be changed with the users inputs. The script can also be changed to any SST product by adding the url and short name in user inputs.

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

wget must be installed on your computer
https://www.gnu.org/software/wget/
"""

#####################################
#Importing neccessary python packages
#####################################

import numpy as np
import pandas as pd 
import datetime 
import netCDF4 as nc4
import os

##############
# User inputs
##############

start_date="2002-06-01"
end_date="2002-06-02"

path_to_save='/home/matthew/Documents/Python_scripts/Automating_downloads/Github/'

my_url = " https://podaac-tools.jpl.nasa.gov/drive/files/allData/ghrsst/data/GDS2/L4/GLOB/JPL/MUR/v4.1/"
short_name = "-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1"

user = ''
password = ''

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
    n_day = (ndays.strftime('%j'))
    n_day_normal = (ndays.strftime('%d'))
    n_hour = str(90000)

    data_url.append(my_url + str(dates[i].year) + "/" +str(n_day)+"/"+str(str(dates[i].year)+str(n_month)+str(n_day_normal)+str(0)+str(n_hour))\
        +short_name+'.nc')
    
    cnt = cnt+1

# Filter out unavailable url's
url_list = data_url

# Loop though url's and download the data
count = 0
for i in url_list:
    
    local_filename = path_to_save+str(dates[count].year)+str('%02d'%dates[count].month)+str('%02d'%dates[count].day)+str(short_name)+'.nc'
    
    url = url_list[count]
    os.system('wget '+' --user='+user+' --password='+password+url)


