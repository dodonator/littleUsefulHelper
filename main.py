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
	def creListAl(self,demand):
		alph = {}
		bigAlph = [] # Large character (A,B,C ... Z)
		litAlph = [] # Small character (a,b,c ...z)
		for i in range(26):
			litAlph.append(chr(65+i))
		i = 0
		for i in range(26):
			bigAlph.append(chr(97+i))
		alph['l'] = bigAlph
		alph['s'] = litAlph
		if demand == 's' or demand == 'S':
			return alph['s']
		elif demand == 'l' or demand == 'L':
			return alph['l']
		else:
			return alph	
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
class fileTools(object):
	def readF(self,filename):
		file1 = open(filename,'r')
		f1 = file1.read()
		file1.close()
		return f1
	def addF(self,filename,text):
		file1 = open(filename,'a')
		f1 = file1.write(text)
		file1.close()
	def writeF(self,filename,text):
		file1 = open(filename,'w')
		f1 = file1.write(text)
		file1.close()
timeT = timeTools()
gT = generalTools()
fT = fileTools()
