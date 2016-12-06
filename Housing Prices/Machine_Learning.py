import pandas as pd
import numpy as np
import quandl
import matplotlib.pyplot as plt
import pickle
import datetime
from sklearn.linear_model import LinearRegression
plt.style.use('ggplot')

api_key = open('quandlAPIKEY.txt').read()

# Web scrap a list of state abbreviated names from wikipedia
def state_list():
    
    fifthy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

    # Collect the column contains the abbreviations without the header
    return fifthy_states[0][0][1:]

# Collect housing price index (HPI) values for each state
def grab_state_data():
    states = state_list()
    master_df = pd.DataFrame()

    # Add the necessary string
    for i in states:
        # Add FMAC/HPI to each state
        # Check out an individual state
        # df = quandl.get('FMAC/HPI_AK', authtoken=api_key)

        state = "FMAC/HPI_"+str(i)
        # Pull data from quandl
        df = quandl.get(state,authtoken=api_key)
        # Rename the column value with it's state name
        df.rename(columns={'Value':str(i)}, inplace = True)
        # Percent change from the original
        # pd.pct_change()
        df[i] = (df[i]-df[i][0])/df[i][0]*100.0
        # Join each array with the current data frame
        if master_df.empty:
            master_df = df
        else:
            master_df = master_df.join(df)

    # Pickle the results, so we dont want to make constant calls to quandl
    # wb for write
    pickle_out = open('fifthy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# Collect housing price index value reported by the country
def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    # Calculate percent range
    df['United States'] = (df['Value']-df['Value'][0])/df['Value'][0]*100.0
    return df

# Get S&P 500 data
def sp500_data():
    df = quandl.get('YAHOO/INDEX_GSPC', trim_start = '1990-01-01',
                    authtoken=api_key)
    df['Adjusted Close'] = (df['Adjusted Close']-df['Adjusted Close'][0])/df['Adjusted Close'][0]*100.0
    df.rename(columns ={'Adjusted Close': 'SP500'}, inplace = True)
    df = df['SP500']
    df = df.resample('M').mean()
    return df

# Get gross domestic product(GDP)
def us_gdp():
    df = quandl.get('BCB/4385', trim_start='1990-01-01',
                    authtoken=api_key)
    df['Value'] = (df['Value']-df['Value'][0])/df['Value'][0]*100.0
    df.rename(columns ={'Value': 'GDP'}, inplace = True)
    df = df['GDP']
    df = df.resample('M').mean()
    return df

# Get US unemployment data
def us_unemployment():
    df = quandl.get('ECPI/JOB_G', trim_start='1990-01-01',
                    authtoken=api_key)
    df['Unemployment Rate'] = (df['Unemployment Rate']-df['Unemployment Rate'][0])/df['Unemployment Rate'][0]*100.0
    df.rename(columns ={'Value': 'GDP'}, inplace = True)
    df = df.resample('M').mean()
    return df

# Get 30 year mortgage prices
def mortgage_30yr():
    df = quandl.get('FMAC/MORTG', trim_start='1990-01-01', authtoken=api_key)
    df['Value'] = (df['Value']-df['Value'][0])/df['Value'][0]*100.0
    df.rename(columns = {'Value':'M30'}, inplace = True)
    df = df.resample('M').mean()
    return df

def state_HPI(HPI,state):
    HPI['State'] = HPI[state].resample('M').mean()
    HPI['State'].plot(label ='Housing Price Index')
    plt.legend(loc = 2)
    start = datetime.datetime(2009,1,1)
    end = datetime.datetime(2010,1,1)
    plt.xlim(start,end)
    plt.ylim(500,600)
    plt.title('Housing Price 2015-2016')
    plt.legend(loc=2)
    plt.show()
    
if __name__=='__main__':
    m30 = mortgage_30yr()
    HPI_data = pd.read_pickle('fifthy_states3.pickle')
    HPI_benchmark = HPI_Benchmark()
    sp500 = sp500_data()
    gdp = us_gdp()
    unemployment = us_unemployment()
    HPI = HPI_data.join([m30,sp500,gdp,unemployment,HPI_benchmark])
    HPI.dropna(inplace = True)
    HPI.to_pickle('HPI_pickle.pickle')
    HPI = pd.read_pickle('HPI_pickle.pickle')
    print(HPI.tail())
    state_HPI(HPI,'NY')



""" If a viewer is interested in their state housing price index """
    
