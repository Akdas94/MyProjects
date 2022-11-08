#IF YOU WANT TO RUN THIS CODE, YOU CAN RUN IT ON 'GOOGLE COLAB' or ON ANY OTHER ONLINE COMPILER 
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

# With this you can add a new column in the data:
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

#With the help of the following code you can anaylse what was the change in stock price over time
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

#If you want to visualize any column, over time you can use the following code:
#Here I am visualizing the change in a stock’s volume being traded, over time :
plt.plot(df_google['Volume'])
plt.xlabel('Time')
plt.ylabel('Change in stock Volume')
plt.legend("Google")
plt.show()

plt.plot(df_apple['Volume'])
plt.xlabel('Time')
plt.ylabel('Change in stock Volume')
plt.legend("Apple")
plt.show()

plt.plot(df_micro['Volume'])
plt.xlabel('Time')
plt.ylabel('Change in stock Volume')
plt.legend("Microsoft")
plt.show()

plt.plot(df_Amazon['Volume'])
plt.xlabel('Time')
plt.ylabel('Change in stock Volume')
plt.legend("Amazon")
plt.show()

#If you want to add Daily Return Average of a stock, there a formula for that:
#Here I am taking Amazon for example:
type(df_Amazon.index)
df_Amazon['Close'].count()
maximum_price = df_Amazon['Close'].max()
print(maximum_price)
df_Amazon.Close[df_Amazon.Close == maximum_price].index

df_Amazon['Daily_Return'] = df_Amazon['Close'].pct_change()*100
df_Amazon.head()
df_Amazon
