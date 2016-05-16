#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  opi.py
#  
#  Copyright 2016 Jack Zhong <ardypro@vostro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  This project is to monitor orange pi's cpu and memory usage
#

import psutil
import time
from time import gmtime,strftime
import requests

import json
valid = False	#剔除掉第一个样本

def initial():
	print '开始监控Orange Pi系统资源'
	return 0
	
def main():
	initial()
	
	api='http://api.heclouds.com/devices/1100454/datapoints?type=3'
	api_key='w2ZpZfGcjeZqRaijTM8YK9tnMeA='

	global valid

	while (True):
		try:
			cpuload = psutil.cpu_percent(interval=None)
			memload = psutil.virtual_memory()[2]
			if (valid):	
				payload={'memload':memload, 'cpuload':cpuload, 'connstatus':1}
				_data=json.dumps(payload)
				_headers={'api-key':api_key}
				r=requests.post(api, _data, headers=_headers)

				print 'cpu load ', cpuload
				print 'mem load ', memload
			
				print 'posted @ ', time.ctime()
				print ' '
	
			valid = True
			time.sleep(2)

		except Exception as e:
			print e
			pass

		finally:
			pass

	return 0

if __name__ == '__main__':
    main()
