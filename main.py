import datetime
import time
import os
import pandas as pd
from pycoingecko import CoinGeckoAPI

def main():
    instruments = { "bitcoin" : "gbp"}
    start_date  = convert_date_to_timestamp("01/01/2020")
    end_date    = convert_date_to_timestamp("01/11/2020")

    # get data
    cg  = CoinGeckoAPI()
    res = cg.get_coin_market_chart_range_by_id('bitcoin', 'gbp', start_date, end_date)

    # normalise into data frame
    # TODO move the below line into the function also
    df  = pd.DataFrame(normalise_gecko_output_to_dataframe(res)).T
    df.columns = ['prices', 'market_caps', 'total_volumes']
    # print(df.describe())

    # inspecting the data 
    prices = df.loc[:, 'prices']
    short_roll = prices.rolling(window=20, min_periods=1).mean()
    long_roll  = prices.rolling(window=100, min_periods=1).mean()

    print(short_roll, long_roll)

def convert_date_to_timestamp(date):
    return time.mktime(datetime.datetime.strptime(date,"%d/%m/%Y").timetuple())

def convert_timestamp_date(ts, format):
    if format == 'd-m-y':
        return datetime.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')

def normalise_gecko_output_to_dataframe(data):
    out = {}
    for k,v in data.items():
        for i in v:
            if i[0] in out:
                out[i[0]].append(i[1])
            else:
                out[i[0]] = [ i[1] ]
    return out


if __name__ == "__main__":
    main()