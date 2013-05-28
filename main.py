# coding: utf-8
import sys
import os
import random
import math
import time
import datetime
import getpass

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
		'''
		repString(string,rep)
		Repeat a Sting rep times
		#####################################
		Parameter:
		string : the string to Repeat
		rep    : the number of repetition
		#####################################
		Examples:
		string : "#"
		rep    : 5
		Result:
		"#####"
		#####################################
		'''
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
		'''
		Clear the console and wait x seconds
		Leert die Konsole und wartet x Sekunden
		'''
		os.system('clear')
		time.sleep(sec)
		
	def CL(self): # clear 
		os.system('clear')
		
	def conCom(self,command):
		'''
		Execute a bash command
		###################################################
		Parameter:
		command : the command to Execute
		###################################################
		Example:
		command : "echo 'foo'"
		Result: "foo"
		###################################################
		'''
		os.system('clear')
		os.system(command)
		
	def CLRI(self,length,start,end,typ): # Create List of Random Integer
		'''
		This function create a list of random Integer
		CLRI(length,start,end,typ)
		#############################################
		Parameter: 
		length: Length of the created list
		start: start of the random range
		end: end of the random range
		#############################################
		Example:
		CLRI(5,1,4)
		Result: 
		[1,4,3,2,1]
		'''
		if typ == 'a':
			result = []
			for i in range(length):
				result.append(random.randint(start,end))
		elif typ == 'd':
			result = {}
			for i in range(length):			
				result[i] = random.randint(start,end)
		return result # Can return list or dict
		
	def secretKey(self,passphrase,numMistakes):
			access = False
			key = ''
			while key != passphrase:
				key = getpass.getpass('Geben sie das Passwort ein: \n')
				if counter <= numMistakes:
					pass
				else:
					access = False
					return access
				counter += 1
			access = True
			return access
			
	def CTTL(self,tupel): # Convert tuppel to list
		result = []
		for i in range(len(tupel)):
			result.append(tupel[i])
		return result
	
	def STC(self):
		'''
		Shutdown the Computer!
		'''
		os.system('clear | sudo shutdown now')

	def LTTLG(self,timelimit,comand): # Lightning Talk Time Limit Guide
		'''
		For Lightning Talks or other time limited Talks
		############################################################
		Parameter:
		timelimit : the time in seconds until the Action
		command   : the bash command, which work after the timelimit
		############################################################
		Examples:
		timelimit : 300 (5 Minutes)
		command : "sudo shutdown now"
		After 5 Minutes the program will shutdown the Computer
		'''
		t = timelimit
		for i in range(t):
			os.system('clear')
			print "Action in: " + str(int((t-i)/60)) + ':' + str((t-i)%60)
			time.sleep(1)
		os.system('clear')
		os.system(comand)

	def cube(self,size): # Würfel
		result = random.randint(1,size)
		return result

	def multiCube(self,size,number): # mehr Würfel
		result = []
		for i in range(number):
			result.append(random.randint(1,size))	
		return result
	
	def TANE(self,ex): # throw a nice Exception
		raise Exception(ex)

	def KINAF(self,message): # Kill it nice and fast
		'''
		A method to quit the program
		#################################################
		Parameter:
		message: Message for the user, which will shown
		         while the killing of the program.
		#################################################
		'''
		sys.exit(message)

	def ATD(self,key,value,dictonary):
		'''
		Add To dictonary
		ATD(key,value,dictonary)
		###############################################
		Parameter:
		key       : key for addition
		value     : value to add
		dictonary : dictonary of operation
		###############################################
		Example:
		key : "x"
		value : 3
		dictonary : {"y":2}
		Result:
		{"x":3,"y":2}
		###############################################
		'''
		dictonary[key] = value
		return dictonary
	
	def G2DL(self,number): # Generate 2-Dimesional List
		result = []
		for i in range(number):
			result.append([])
		return result
	
	def SH(self,func):
		'''
		show the help of a function
		SH(func)
		#########################################
		Parameter:
		func : the function for your help
		#########################################
		'''
		print help(func)
	def ranPerPro(self,*probs): # Random per Probabilities
		base = []
		result = []
		#base = probs
		i = 0
		testResult = 0
		for i in probs:
			base.append(i)
		i = 0
		for i in base:
			testResult += i
		if testResult != 100:
			raise Exception('ERR. 001: The sum of your probabilities must be 100.')
		i = 0
		testResult = []
		for i in base:
			testResult.append([])
		i = 0
		counter = 0
		print base
		for i in base:
			for p in range(i):
				testResult[counter].append(counter)
			counter += 1
		i = 0
		p = 0
		for i in testResult:
			for p in i:
				result.append(p)
		if len(result) != 100:
			raise Exception('There is an Error you stupid idiot.')
		else:
			r = random.randint(0,99)
			return result[r]
			

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