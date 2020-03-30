import datetime
import os
from alpha_vantage.cryptocurrencies import CryptoCurrencies


def main():
    cc = CryptoCurrencies(key='MNAHYDQBT3NM3QOI',output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='GBP')
    print(data)


if __name__ == "__main__":
    main()