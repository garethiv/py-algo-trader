import datetime
import os
from pycoingecko import CoinGeckoAPI
from server import strategy

def main():
    cg = CoinGeckoAPI()
    res = cg.ping()
    print(res)

    strategy(2)

if __name__ == "__main__":
    main()