from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import json

#change the directory later 
key =  open("/Users/teppei/Desktop/apikey.hidden.txt").read().strip()

get_new_data = False

if get_new_data:
    ts = TimeSeries(key)
    data, meta_data = ts.get_intraday('GOOGL')
    outfile = open("saved.json", "w")
    json.dump(data, outfile)
    outfile.close()
    outfile = open("meta_data.json", "w")
    json.dump(meta_data, outfile)
    outfile.close()
#loading
else:
    datafile = open("saved.json", "r")
    data = json.load(datafile)
    datafile.close()


#for crypto stuff
#cc = CryptoCurrencies(key)
#data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='AUD')
#data['4b. close (USD)'].plot()
#plt.tight_layout()
#plt.title('Daily close value for bitcoin (BTC)')
#plt.grid()
#plt.show()
