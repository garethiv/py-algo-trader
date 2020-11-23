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
[] Simple backtester
[] SMA - Simple Moving Average strategy
[] Compute performance from the SMA strategy

- BACKTESTER
    Pull some data from an exchange
    Feed the data into the strategy
- SERVER
    Simple moving average strategy will decide to buy/sell from that
    Position store

    
