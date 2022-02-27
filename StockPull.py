
import json
import sys

from multiprocessing.pool import CLOSE
from sqlite3 import Timestamp
from traceback import print_tb

import yfinance as yf
import pandas as pd

import time
import random
import datetime

import plotly.express as px

from pymongo import MongoClient


today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)

stocks = ("MSFT", "MVIS", "GOOG", "SPOT", "INO", "OCGN", "ABML", "RLLCF", "JNJ", "PSFE")
for stock in stocks:	
	stockdata = yf.Ticker(stock)
	data = stockdata.history(start= yesterday, end= today, interval = '1h' )
	df = pd.DataFrame(data['Close'])
	stored_datetime = data.index
	Kichaum={}
	TIMESTAMP=[]
	CLOSEVALUE=[]
	
	for idx,row in df.iterrows():
		jsondata = {
		'stockid' : str(stock),
		'timestamp' : str(idx),
		'CloseValue' : row['Close'],
		'52WeekHigh' : stockdata.info["fiftyTwoWeekHigh"],
		'52WeekLow' : stockdata.info["fiftyTwoWeekLow"]	
		}
		
		TIMESTAMP.append(jsondata["timestamp"])
		CLOSEVALUE.append(jsondata["CloseValue"])
  
		Kichaum['timEstamp']=TIMESTAMP
		Kichaum['closEvalue']=CLOSEVALUE
  
		dff=pd.DataFrame(Kichaum, columns=['timEstamp','closEvalue'])
		#print(dff)
		#print(f'{jsondata["timestamp"} : {jsondata["CloseValue"]}')
		figures = px.line(x=TIMESTAMP, y=CLOSEVALUE, labels={'x':'Timestamp', 'y':'CloseValue'})
		figures.show()
		
		
