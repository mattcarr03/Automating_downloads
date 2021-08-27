# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:58:03 2019

@author: matth
"""

# Looping through motu client and CMEMS subsetter to download multiple days
import os
from datetime import datetime, timedelta, date

## Here we define all the bits and pieces that get put in the 'runcommand' which is run by os

# Calling python 
pythoncall = 'python'

# The path where the file will be saved
pname  = '/media/matthew/Cerberus/OSTIA_5km/'

#The prefix of the file name to be saved (output)
sname = 'SST_OSTIA_5km_daily'

# Domain of interest [west, east, south, north]
domain = [-10, 60, -50, -6]

#Dates that need to be downloaded [creating date vector]
startDate = '2000-01-01 12:00:00'
endDate =   '2001-01-01 12:00:00'

# The variables to be downloaded 
varList = ['analysed_sst']

# CMEMS username and password  
usrname = ''
passwd = ''

# service id provided by cmems website (--service-id)
serv_id = 'SST_GLO_SST_L4_REP_OBSERVATIONS_010_011-TDS'

#product id provided by cmems website (--product-id)
prod_id = 'METOFFICE-GLO-SST-L4-REP-OBS-SST'

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

 
