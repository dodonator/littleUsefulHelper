import sys
import os
import random
import math
import time
import datetime
class timeTools(object):
	def getTime(self):
		localTime = {}
		lTime = time.localtime()
		localTime['year'] = lTime[0]
		localTime['month'] = lTime[1] 
		localTime['day'] = lTime[2]
		localTime['hour'] = lTime[3]
		localTime['minute'] = lTime[4]
		localTime['second'] = lTime[5]
		return localTime
	def formatTimeDict(self,timeDict):
		result = ''
		result = str(timeDict['hour']) + ':' + str(timeDict['minute']) + ':' + str(timeDict['second'])
		result += ' ' + str(timeDict['day']) + '.' + str(timeDict['month']) + '.' + str(timeDict['year'])
		return result
	def slS(self,sec): # sleep seconds
		time.sleep(sec)
	def slM(self,mon): # sleep minutes
		time.sleep(mon*60)
	def slH(self,hour): # sleep hours
		time.sleep(hour*3600)	
class generalTools(object):
	def repString(self,string,rep):
		result = rep*string
		return result	
	def wc(self,sec): # wait and clear
		time.sleep(sec)
		os.system('clear')
	def cw(self,sec): # clear and wait
		os.system('clear')
		time.sleep(sec)
	def CL(self): # clear
		os.system('clear')
	def conCom(self,command):
		os.system(command)
timeT = timeTools()
gT = generalTools()

