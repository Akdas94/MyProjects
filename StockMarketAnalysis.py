!pip install --upgrade pandas-datareader
!pip install --upgrade pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
!pip install yfinance
import yfinance as yf
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import pandas_datareader.data as web
import datetime

# How to Read the Data from Yahoo finance website directly:
# Here I am Reading data of Apple, Google, Microsoft & Amazon 

start = datetime.datetime(2022, 6, 1)
end = datetime.datetime(2022, 6, 30)
source = 'yahoo'
df_apple = web.DataReader("AAPL", source, start, end)
df_apple
df_apple.head()

df_google = web.DataReader("GOOG", source, start, end)
df_google.head()

df_micro = web.DataReader("MSFT", source, start, end)
df_micro

df_Amazon = web.DataReader("AMZN", source, start, end)
df_Amazon

# With you this can add a new c 
df_Amazon["company_name"]='AMAZON'
df_Amazon.head()

df_google.info()
df_google["company_name"]='GOOG'
df_google.head()

# Here I am combining data from both Amazon & Google:
df_combined =  pd.concat([df_Amazon,df_google])
df_combined.head()
df_combined.tail()
df_combined.shape
df_combined["company_name"].unique()
df_google.loc[:,"Volume"]

#With the help of thebfollowing code you anaylse what was the change in stock price over time
amzn = yf.download('AMZN',start,end)
aapl = yf.download('AAPL',start,end)
msft = yf.download('MSFT',start,end)
tsla = yf.download('TSLA',start,end)
amzn['Open'].plot(label = 'AMZN', figsize = (15,7))
aapl['Open'].plot(label = 'AAPL')
msft['Open'].plot(label = 'MSFT')
tsla['Open'].plot(label = 'GOOG')
plt.title('Stock Prices of AMZN,AAPL,MSFT and GOOG')
plt.legend()

df_apple = df_apple.round(2)
df_apple.head(2)
df_apple.shape
df_apple.isnull().sum()
df_apple.dropna(inplace = True, axis = 0)
df_apple.dtypes
