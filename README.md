# py-algo-trader

# COMPONENTS
- BACKTESTER
    HTTP calls for market data
    Feeds into the server for simulating/testing strategies
    Charting to reviewing results

- SERVER
    Event processing engine
        Storage for event history - to remember how certain events affected things
        Storage for temporary market data - to persist data for short term decisions
        Record of previous trades and performance
    Order manager
        Listen to market data
        Constructs events based on market data ticks
        Calls risk management system
    Risk management system
        Determines risk from position
        Returns a risk measure/matrix
    Market data adapter
        Normalize market data from exchange

- APPLICATION - viewer
    Strategy input tweaking
    Order/Execution monitor
    PnL & Position management
    Data retrieval

# v0.1
[x] Pull some data from an exchange
    [x] Normalize the data into pandas/numPy array
[] Build the SMA strategy
[] Apply the SMA strategy to make a buy/sell decision
[] Feed the historical data into the strategy
[] Determine the valuation of the position at the end of the strategy being performed over the data
