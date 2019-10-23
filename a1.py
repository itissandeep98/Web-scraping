#Contributor : Sandeep kumar singh
'''
For getting attributes like temerature,humidity etc, 
The data from the webage is converted into string using the decode function.
Then the data is formatted and sliced as per the needs.
Specific case :-If the first string after the first split then it contains some extra line-
"{"cod":"200","message":0.0113,"cnt":40,"list":[" , to remove it another split operation is performed based on ':[' .
'''

import urllib.request 
from datetime import datetime

'''*-----------------------SOME EXTRA FUNCTIONS-----------------------*'''
def m_time():
"""
This function is used to return the least time for which you can get weather details
Return type is string in format 'XX:XX:XX'
"""
	c_time_H=datetime.now().strftime("%H") #current hour
	m_time_H='00:00:00'                    #minimum time 

	if c_time_H>='21':
		m_time_H='18:00:00' 
	elif c_time_H>='18':
		m_time_H='15:00:00'
	elif c_time_H>='15':
		m_time_H='12:00:00'
	elif c_time_H>='12':
		m_time_H='09:00:00'
	elif c_time_H>='09':
		m_time_H='06:00:00'
	elif c_time_H>='06':
		m_time_H='03:00:00'
	return m_time_H

def partoflist(d,t,l):
"""
function to search for correct part from the list divided into different time frames(and date)
as we were restricted not to use loops; so by nesting i-else statements this function became so huge
check it at your own risk
d is no. of days after today, t is time, l is no. of elements in whole list
"""

	if  m_time()=='00:00:00':
		if d==0:
			if t=='21:00:00':
				m=7
			elif t=='18:00:00':
				m=6
			elif t=='15:00:00':
				m=5
			elif t=='12:00:00':
				m=4
			elif t=='09:00:00':
				m=3
			elif t=='06:00:00':
				m=2
			elif t=='03:00:00':
				m=1
			else:
				m=0
		elif d==1:
			if t=='21:00:00':
				m=15
			elif t=='18:00:00':
				m=14
			elif t=='15:00:00':
				m=13
			elif t=='12:00:00':
				m=12
			elif t=='09:00:00':
				m=11
			elif t=='06:00:00':
				m=10
			elif t=='03:00:00':
				m=9
			else:
				m=8
		elif d==2:
			if t=='21:00:00':
				m=23
			elif t=='18:00:00':
				m=22
			elif t=='15:00:00':
				m=21
			elif t=='12:00:00':
				m=20
			elif t=='09:00:00':
				m=19
			elif t=='06:00:00':
				m=18
			elif t=='03:00:00':
				m=17
			else:
				m=16
		elif d==3:
			if t=='21:00:00':
				m=31
			elif t=='18:00:00':
				m=30
			elif t=='15:00:00':
				m=29
			elif t=='12:00:00':
				m=28
			elif t=='09:00:00':
				m=27
			elif t=='06:00:00':
				m=26
			elif t=='03:00:00':
				m=25
			else:
				m=24
		elif d==4:
			if t=='21:00:00':
				m=39
			elif t=='18:00:00':
				m=38
			elif t=='15:00:00':
				m=37
			elif t=='12:00:00':
				m=36
			elif t=='09:00:00':
				m=35
			elif t=='06:00:00':
				m=34
			elif t=='03:00:00':
				m=33
			else:
				m=32
	
	elif m_time()=='03:00:00':
		if d==0:
			if t=='21:00:00':
				m=6
			elif t=='18:00:00':
				m=5
			elif t=='15:00:00':
				m=4
			elif t=='12:00:00':
				m=3
			elif t=='09:00:00':
				m=2
			elif t=='06:00:00':
				m=1
			elif t=='03:00:00':
				m=0			
		elif d==1:
			if t=='21:00:00':
				m=14
			elif t=='18:00:00':
				m=13
			elif t=='15:00:00':
				m=12
			elif t=='12:00:00':
				m=11
			elif t=='09:00:00':
				m=10
			elif t=='06:00:00':
				m=9
			elif t=='03:00:00':
				m=8
			else:
				m=7
		elif d==2:
			if t=='21:00:00':
				m=22
			elif t=='18:00:00':
				m=21
			elif t=='15:00:00':
				m=20
			elif t=='12:00:00':
				m=19
			elif t=='09:00:00':
				m=18
			elif t=='06:00:00':
				m=17
			elif t=='03:00:00':
				m=16
			else:
				m=15
		elif d==3:
			if t=='21:00:00':
				m=30
			elif t=='18:00:00':
				m=29
			elif t=='15:00:00':
				m=28
			elif t=='12:00:00':
				m=27
			elif t=='09:00:00':
				m=26
			elif t=='06:00:00':
				m=25
			elif t=='03:00:00':
				m=24
			else:
				m=23
		elif d==4:
			if t=='21:00:00':
				m=38
			elif t=='18:00:00':
				m=37
			elif t=='15:00:00':
				m=36
			elif t=='12:00:00':
				m=35
			elif t=='09:00:00':
				m=34
			elif t=='06:00:00':
				m=33
			elif t=='03:00:00':
				m=32
			else:
				m=31
		elif d==5:
			m=39	

	elif m_time()=='06:00:00':
		if d==0:
			if t=='21:00:00':
				m=5
			elif t=='18:00:00':
				m=4
			elif t=='15:00:00':
				m=3
			elif t=='12:00:00':
				m=2
			elif t=='09:00:00':
				m=1
			else:
				m=0
		elif d==1:
			if t=='21:00:00':
				m=13
			elif t=='18:00:00':
				m=12
			elif t=='15:00:00':
				m=11
			elif t=='12:00:00':
				m=10
			elif t=='09:00:00':
				m=9
			elif t=='06:00:00':
				m=8
			elif t=='03:00:00':
				m=7
			else:
				m=6
		elif d==2:
			if t=='21:00:00':
				m=21
			elif t=='18:00:00':
				m=20
			elif t=='15:00:00':
				m=19
			elif t=='12:00:00':
				m=18
			elif t=='09:00:00':
				m=17
			elif t=='06:00:00':
				m=16
			elif t=='03:00:00':
				m=15
			else:
				m=14
		elif d==3:
			if t=='21:00:00':
				m=29
			elif t=='18:00:00':
				m=28
			elif t=='15:00:00':
				m=27
			elif t=='12:00:00':
				m=26
			elif t=='09:00:00':
				m=25
			elif t=='06:00:00':
				m=24
			elif t=='03:00:00':
				m=23
			else:
				m=22
		elif d==4:
			if t=='21:00:00':
				m=37
			elif t=='18:00:00':
				m=36
			elif t=='15:00:00':
				m=35
			elif t=='12:00:00':
				m=34
			elif t=='09:00:00':
				m=33
			elif t=='06:00:00':
				m=32
			elif t=='03:00:00':
				m=31
			else:
				m=30
		elif d==5:
			if t=='03:00:00':
				m=39
			else:
				m=38

	elif m_time()=='09:00:00':
		if d==0:
			if t=='21:00:00':
				m=4
			elif t=='18:00:00':
				m=3
			elif t=='15:00:00':
				m=2
			elif t=='12:00:00':
				m=1
			else:
				m=0
		elif d==1:
			if t=='21:00:00':
				m=12
			elif t=='18:00:00':
				m=11
			elif t=='15:00:00':
				m=10
			elif t=='12:00:00':
				m=9
			elif t=='09:00:00':
				m=8
			elif t=='06:00:00':
				m=7
			elif t=='03:00:00':
				m=6
			else:
				m=5
		elif d==2:
			if t=='21:00:00':
				m=20
			elif t=='18:00:00':
				m=19
			elif t=='15:00:00':
				m=18
			elif t=='12:00:00':
				m=17
			elif t=='09:00:00':
				m=16
			elif t=='06:00:00':
				m=15
			elif t=='03:00:00':
				m=14
			else:
				m=13
		elif d==3:
			if t=='21:00:00':
				m=28
			elif t=='18:00:00':
				m=27
			elif t=='15:00:00':
				m=26
			elif t=='12:00:00':
				m=25
			elif t=='09:00:00':
				m=24
			elif t=='06:00:00':
				m=23
			elif t=='03:00:00':
				m=22
			else:
				m=21
		elif d==4:
			if t=='21:00:00':
				m=36
			elif t=='18:00:00':
				m=35
			elif t=='15:00:00':
				m=34
			elif t=='12:00:00':
				m=33
			elif t=='09:00:00':
				m=32
			elif t=='06:00:00':
				m=31
			elif t=='03:00:00':
				m=30
			else:
				m=29
		elif d==5:
			if t=='06:00:00':
				m=39
			elif t=='03:00:00':
				m=38
			else:
				m=37

	elif m_time()=='12:00:00':
		if d==0:
			if t=='21:00:00':
				m=3
			elif t=='18:00:00':
				m=2
			elif t=='15:00:00':
				m=1
			else:
				m=0
		elif d==1:
			if t=='21:00:00':
				m=11
			elif t=='18:00:00':
				m=10
			elif t=='15:00:00':
				m=9
			elif t=='12:00:00':
				m=8
			elif t=='09:00:00':
				m=7
			elif t=='06:00:00':
				m=6
			elif t=='03:00:00':
				m=5
			else:
				m=4
		elif d==2:
			if t=='21:00:00':
				m=19
			elif t=='18:00:00':
				m=18
			elif t=='15:00:00':
				m=17
			elif t=='12:00:00':
				m=16
			elif t=='09:00:00':
				m=15
			elif t=='06:00:00':
				m=14
			elif t=='03:00:00':
				m=13
			else:
				m=12
		elif d==3:
			if t=='21:00:00':
				m=27
			elif t=='18:00:00':
				m=26
			elif t=='15:00:00':
				m=25
			elif t=='12:00:00':
				m=24
			elif t=='09:00:00':
				m=23
			elif t=='06:00:00':
				m=22
			elif t=='03:00:00':
				m=21
			else:
				m=20
		elif d==4:
			if t=='21:00:00':
				m=35
			elif t=='18:00:00':
				m=34
			elif t=='15:00:00':
				m=33
			elif t=='12:00:00':
				m=32
			elif t=='09:00:00':
				m=31
			elif t=='06:00:00':
				m=30
			elif t=='03:00:00':
				m=29
			else:
				m=28
		elif d==5:
			if t=='09:00:00':
				m=39
			elif t=='06:00:00':
				m=38
			elif t=='03:00:00':
				m=37
			else:
				m=36

	elif m_time()=='15:00:00':
		if d==0:
			if t=='21:00:00':
				m=2
			elif t=='18:00:00':
				m=1
			else:
				m=0
		elif d==1:
			if t=='21:00:00':
				m=10
			elif t=='18:00:00':
				m=9
			elif t=='15:00:00':
				m=8
			elif t=='12:00:00':
				m=7
			elif t=='09:00:00':
				m=6
			elif t=='06:00:00':
				m=5
			elif t=='03:00:00':
				m=4
			else:
				m=3
		elif d==2:
			if t=='21:00:00':
				m=18
			elif t=='18:00:00':
				m=17
			elif t=='15:00:00':
				m=16
			elif t=='12:00:00':
				m=15
			elif t=='09:00:00':
				m=14
			elif t=='06:00:00':
				m=13
			elif t=='03:00:00':
				m=12
			else:
				m=11
		elif d==3:
			if t=='21:00:00':
				m=26
			elif t=='18:00:00':
				m=25
			elif t=='15:00:00':
				m=24
			elif t=='12:00:00':
				m=23
			elif t=='09:00:00':
				m=22
			elif t=='06:00:00':
				m=21
			elif t=='03:00:00':
				m=20
			else:
				m=19
		elif d==4:
			if t=='21:00:00':
				m=34
			elif t=='18:00:00':
				m=33
			elif t=='15:00:00':
				m=32
			elif t=='12:00:00':
				m=31
			elif t=='09:00:00':
				m=30
			elif t=='06:00:00':
				m=29
			elif t=='03:00:00':
				m=28
			else:
				m=27
		elif d==5:
			if t=='12:00:00':
				m=39
			elif t=='09:00:00':
				m=38
			elif t=='06:00:00':
				m=37
			elif t=='03:00:00':
				m=36
			else:
				m=35

	elif m_time()=='18:00:00':
		if d==0:
			if t=='21:00:00':
				m=1
			else:
				m=0			
		elif d==1:
			if t=='21:00:00':
				m=9
			elif t=='18:00:00':
				m=8
			elif t=='15:00:00':
				m=7
			elif t=='12:00:00':
				m=6
			elif t=='09:00:00':
				m=5
			elif t=='06:00:00':
				m=4
			elif t=='03:00:00':
				m=3
			else:
				m=2
		elif d==2:
			if t=='21:00:00':
				m=17
			elif t=='18:00:00':
				m=16
			elif t=='15:00:00':
				m=15
			elif t=='12:00:00':
				m=14
			elif t=='09:00:00':
				m=13
			elif t=='06:00:00':
				m=12
			elif t=='03:00:00':
				m=11
			else:
				m=10
		elif d==3:
			if t=='21:00:00':
				m=25
			elif t=='18:00:00':
				m=24
			elif t=='15:00:00':
				m=23
			elif t=='12:00:00':
				m=22
			elif t=='09:00:00':
				m=21
			elif t=='06:00:00':
				m=20
			elif t=='03:00:00':
				m=19
			else:
				m=18
		elif d==4:
			if t=='21:00:00':
				m=33
			elif t=='18:00:00':
				m=32
			elif t=='15:00:00':
				m=31
			elif t=='12:00:00':
				m=30
			elif t=='09:00:00':
				m=29
			elif t=='06:00:00':
				m=28
			elif t=='03:00:00':
				m=27
			else:
				m=26
		elif d==5:
			if t=='15:00:00':
				m=39
			elif t=='12:00:00':
				m=38
			elif t=='09:00:00':
				m=37
			elif t=='06:00:00':
				m=36
			elif t=='03:00:00':
				m=35
			else:
				m=34

	elif m_time()=='21:00:00':
		if d==0:
			m=0					
		elif d==1:
			if t=='21:00:00':
				m=8
			elif t=='18:00:00':
				m=7
			elif t=='15:00:00':
				m=6
			elif t=='12:00:00':
				m=5
			elif t=='09:00:00':
				m=4
			elif t=='06:00:00':
				m=3
			elif t=='03:00:00':
				m=2
			else:
				m=1
		elif d==2:
			if t=='21:00:00':
				m=16
			elif t=='18:00:00':
				m=15
			elif t=='15:00:00':
				m=14
			elif t=='12:00:00':
				m=13
			elif t=='09:00:00':
				m=12
			elif t=='06:00:00':
				m=11
			elif t=='03:00:00':
				m=10
			else:
				m=9
		elif d==3:
			if t=='21:00:00':
				m=24
			elif t=='18:00:00':
				m=23
			elif t=='15:00:00':
				m=22
			elif t=='12:00:00':
				m=21
			elif t=='09:00:00':
				m=20
			elif t=='06:00:00':
				m=19
			elif t=='03:00:00':
				m=18
			else:
				m=17
		elif d==4:
			if t=='21:00:00':
				m=32
			elif t=='18:00:00':
				m=31
			elif t=='15:00:00':
				m=30
			elif t=='12:00:00':
				m=29
			elif t=='09:00:00':
				m=28
			elif t=='06:00:00':
				m=27
			elif t=='03:00:00':
				m=26
			else:
				m=25
		elif d==5:
			if t=='18:00:00':
				m=39
			elif t=='15:00:00':
				m=38
			elif t=='12:00:00':
				m=37
			elif t=='09:00:00':
				m=36
			elif t=='06:00:00':
				m=35
			elif t=='03:00:00':
				m=34
			else:
				m=33

	return m

def data_day(json,d=0,t='00:00:00'): 
"""
The function data_day() is used to get the whole of the specific time and data
d is the number of days after today
Return type sting
"""
	split=json.split('},{')
	l=len(split)
	m=partoflist(d,t,l)
	return split[m]



'''*----------------------REQUIRED FUNCTIONS-----------------------*'''

def has_error(json,location, API_key):
"""
This fucntion checks whether a particular query is correct or not
Return Type : Boolean
"""
	s=json.split('},{')
	y=len(s)-1
	s=s[y].split('],')
	s=s[2].split(',')
	o_city=s[1][8:].lower()  #o_city->city printed o webpage
	i_city=location + '"'
	i_city=i_city.lower()    #i_city->input city
	if i_city!=o_city and len(API_key)<32 :
		return True
	else:
		return False

def weather_response(location, API_key):
"""
This function is used to get the whole json string from the webpage for a particular location
Return type : String

"""

	json=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' %(location,API_key)).read()
	json=json.decode('ASCII')#decode is highly needed because if typecasted some extra characters will get added up which will make the program more complicated 
	return json


def get_temperature (json, d=0, t='00:00:00'):
"""
This function is used to return the temperature for specified date and time 
from the json string passed as parameter
Return type : float
"""
	if d==0 and t==m_time():
		data=data_day(json).split(':[')
		data1=data[1].split(',')
		temp=float(data1[1][15:])
	else:
		data=data_day(json,d,t).split(',')
		temp=float(data[1][15:])
	return temp 

def get_humidity(json, d=0,t='00:00:00'):
"""
This function is used to return the humidity for specified date and time 
from the json string passed as parameter
Return type : float
"""

	if d==0 and t==m_time():
		data=data_day(json,d,t).split(':[')
		data1=data[1].split(',')
		hum=float(data1[7][11:])
	else:
		data=data_day(json,d,t).split(',')
		hum=float(data[7][11:])
	return hum

def get_pressure(json, d=0,t='00:00:00'):
"""
This function is used to return the pressure level for specified date and time 
from the json string passed as parameter
Return type : float
"""

	if d==0 and t==m_time():
		data=data_day(json,d,t).split(':[')
		data1=data[1].split(',')
		press=float(data1[4][11:])
	else:	
		data=data_day(json,d,t).split(',')
		press=float(data[4][11:])
	return press

def get_wind(json, d=0,t='00:00:00'):
"""
This function is used to return the wubd speed for specified date and time 
from the json string passed as parameter
Return type : float
"""

	if d==0 and t==m_time():
		data=data_day(json,d,t).split(':[',1)
		data1=data[1].split(',')
		wind=float(data1[14][16:])
	else:
		data=data_day(json,d,t).split(',')
		wind=float(data[14][16:])
	return wind

def get_sealevel(json, d=0,t='00:00:00'):
"""
This function is used to return the sea level for specified date and time 
from the json string passed as parameter
Return type : float
"""

	if d==0 and t==m_time():
		data=data_day(json,d,t).split(':[')
		data1=data[1].split(',')
		sea_l=float(data1[5][12:])
	else:
		data=data_day(json,d,t).split(',')
		sea_l=float(data[5][12:])
	return sea_