# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:58:03 2019

@author: matth
"""

"""
This is a script to automate the download of OSTIA SST from Copernicus Marine Service (CMEMS). The script is setup to download a regional subset over a time period selected by the user. The script is currently setup to download OSTIA SST but can be used to download any CMEMS product by change the users inputs. The script requires a username and password which is obtain we signed up to CMEMS (https://marine.copernicus.eu/), this is free.

If the size request is too big "[ERROR] 010-7 : The result file size, 1049.0Mb, is too big and shall be less than 1024.0Mb. Please narrow your request." please use the script CMEMS_OSTIA_subset_NC_per_day.py.

The user inputs are as follows: 

pname - the path where the file will be saved 
sname - the prefix of the file name to be saved (output file name)
domain - the domain of interest [west, east, south, north]
startDate/endDate - the date range that need to be downloaded 
varList - the variable to be download 
serv_id - the service id of the product to be downloaded, this is provided by cmems website  
prod_id = the product id of the product to be downloaded, this is provided by cmems website  

The intial setup/python packages required are:

motuclient -  python3 -m pip install motuclient==1.8.4 --no-cache-dir
(https://help.marine.copernicus.eu/en/articles/4796533-what-are-the-motu-client-motuclient-and-python-requirements#h_3d33beaafc)

datetime -  python3 -m pip install datetime 
(https://pypi.org/project/DateTime/)

"""

##############
# User inputs
##############

# The path where the file will be saved
pname  = '/home/matthew/Documents/Python_scripts/Automating_downloads/Github/'

#The prefix of the file name to be saved (output)
sname = 'SST_OSTIA_5km_daily'

# Domain of interest [west, east, south, north]
domain = [-10, 60, -50, -6]

#Dates that need to be downloaded [creating date vector]
startDate = '2000-01-01 12:00:00'
endDate =   '2000-01-01 12:00:00'

# The variables to be downloaded 
varList = ['analysed_sst']

# CMEMS username and password  
usrname = 'mcarr'
passwd = '7WfaUsfyfE'

# service id provided by cmems website (--service-id)
serv_id = 'SST_GLO_SST_L4_REP_OBSERVATIONS_010_011-TDS'

#product id provided by cmems website (--product-id)
prod_id = 'METOFFICE-GLO-SST-L4-REP-OBS-SST'

# Calling python 
pythoncall = 'python3'

#####################################
#Importing neccessary python packages
#####################################

import os
from datetime import datetime, timedelta, date

##############################
#Building and excuting command
##############################

#Building the command to run motu client and download the subset (Building the excutable command)
runcommand = pythoncall+' -m motuclient --quiet'+ \
    ' --user '+usrname+' --pwd '+passwd+ \
    ' --motu https://my.cmems-du.eu/motu-web/Motu'+ \
    ' --service-id ' +str(serv_id)+ \
    ' --product-id ' +str(prod_id)+ \
    ' --longitude-min '+str(domain[0])+' --longitude-max '+str(domain[1])+ \
    ' --latitude-min '+str(domain[2])+' --latitude-max '+str(domain[3])+ \
    ' --date-min "'+str(startDate)+'" --date-max "'+str(endDate)+'"'+ \
    ' --variable '+varList[0]+ \
    ' --out-dir '+pname+' --out-name '+sname+'.nc'

# Run command
print('fetching SST from CMEMS')
print(startDate+'_to_'+endDate)
print('Saving to '+pname+sname+'.nc')
#Running the ecutable
os.system(runcommand)

 
