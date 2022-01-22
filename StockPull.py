import json
import sys
import yfinance as yf
import pandas as pd

import time
import random
import datetime

today = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
yesterday = datetime.date.today().replace(day=1) - datetime.timedelta(days=2)

stocks = ("MSFT", "MVIS", "GOOG", "SPOT", "INO", "OCGN", "ABML", "RLLCF", "JNJ", "PSFE")
for stock in stocks:	
	stockdata = yf.Ticker(stock)
	data = stockdata.history(start= yesterday, end= today, interval = '1h' )
	df = pd.DataFrame(data['Close'])
	stored_datetime = data.index
	#for row in 
	#print(stored_datetime[0])
	
	for idx,row in df.iterrows():
		jsondata = {
		'stockid' : str(stock),
		'timestamp' : str(idx),
		'CloseValue' : row['Close'],
		'52WeekHigh' : stockdata.info["fiftyTwoWeekHigh"],
		'52WeekLow' : stockdata.info["fiftyTwoWeekLow"]	
		}
		print(jsondata)

	
		
	


