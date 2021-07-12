# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:43:38 2020

@author: dukel
"""

#%%

import numpy as np
import pandas as pd
import socket

ls = ['152.79.105.42',
      '152.79.113.146',
      '152.79.113.148',
      '152.79.113.150',
      '152.79.113.97',
      '152.79.113.98',
      '152.79.114.40',
      '152.79.114.51',
      '152.79.114.59',
      '152.79.160.24',
      '152.79.229.118',
      '152.79.229.232',
      '152.79.229.233',
      '152.79.229.7',
      '152.79.230.113',
      '152.79.230.150',
      '152.79.230.159',
      '152.79.230.160',
      '152.79.230.19',
      '152.79.230.65']

def ip2host(ls_input):
    """
    Parameters : list of a ip addreses
    ----------
    Returns : list of tuples, n=2, consisting of the ip and hostname
    """
    ls_output = []
    
    for ip in ls_input:
        try:
            x = socket.gethostbyaddr(ip)
            ls_output.append((ip, x[0]))
        except Exception as e:
            print('Error: ', e)
            ls_output.append((ip, None))
    return ls_output

def host2ip(ls_input):
    ls_output = []

    for hostname in ls_input:
        try:
            x = socket.gethostbyname(hostname)
            ls_output.append((hostname, x[0]))
        except Exception as e:
            print('Error: ', e)
            ls_output.append((hostname, None))
    return ls_output

ls2 = convert_ip_to_hostname(ls)
#%%
# clean
df = pd.DataFrame(data=ls2, columns=['ip', 'hostname'])
df['hostname'] = df['hostname'].str.replace('.ucdmc.ucdavis.edu','').str.upper()