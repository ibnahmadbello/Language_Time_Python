import calendar
import datetime
import time
import constants

def getTime(param):
	if type(param)== str:
		param = param
	else:
		param = param.strftime("%H:%M")

	hour = int(param.split(":")[0])
	minute = int(param.split(":")[1])
	return getTimeHour(hour, minute)


def getCurrentTime():
	return getTime(time)

def getTimeHour(hour, minute):
	if hour==0:
		hour=24
	yor_minute = ""
	if minute!=0:
		yor_minute = getMinute(minute)
	if minute > 30:
		yor_hour = getHour(hour+1)
	else:
		yor_hour = getHour(hour)
	return yor_minute + yor_hour

def getMinute(minute):
	description = constants.number30
	if minute==45:
		description = constants.number45
	elif minute > 30:
		description = constants.BEFORE_POINTER + getNumber(60 - minute) 
	elif minute==15:
		description = constants.number15
	elif minute <= 30:
		description = constants.AFTER_POINTER + getNumber(minute)

	return description;

def getHour(hour):
	if hour > 12:
		return constants.TIME_POINTER + getNumber(hour-12) 
	else:
		return constants.TIME_POINTER + getNumber(hour) 
   
def getNumber(number):
	switch = {
	1 : constants.number1,
	2 : constants.number2,
	3 : constants.number3,
	4 : constants.number4,
	5 : constants.number5,
	6 : constants.number6,
	7 : constants.number7,
	8 : constants.number8,
	9 : constants.number9,
	10 : constants.number10,
	11 : constants.number11,
	12 : constants.number12,
	13 : constants.number13,
	14 : constants.number14,
	15 : constants.number15,
	16 : constants.number16,
	17 : constants.number17,
	18 : constants.number18,
	19 : constants.number19,
	20 : constants.number20,
	21 : constants.number21,
	22 : constants.number22,
	23 : constants.number23,
	24 : constants.number24,
	25 : constants.number25,
	26 : constants.number26,
	27 : constants.number27,
	28 : constants.number28,
	29 : constants.number29,
	30 : constants.number30,
	45 : constants.number45,
	}

	return switch.get(number, "")



