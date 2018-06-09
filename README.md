# Stock Prices via Quand API

This is *Matteo Casadei* milestone project aimed at showing what was learned from the 12-day course taken as 
preliminary step for *Data Incubator 2018's summer session*.

By exploiting several technologies, such as Flask, JSON, Pandas,
Requests, Heroku, GIT, Bokeh for visualization and leveraging on the 
[QUANDL](https://www.quandl.com/) public API to access data related to US stock marker, we devised a lightweight 
Web app to show the trend of several price measures for any available US stock ticker.

The running app can be found at [https://tdi-stockprices.herokuapp.com](https://tdi-stockprices.herokuapp.com).

## Installation and Execution

In order to install the app make sure to follow these steps:

1. Make sure you have Python 3 installed;
2. install all the dependencies specified in [requirements.txt](requirements.txt);
3. define the environment variable ```QUANDL_KEY``` setting it to the corresponding API key obtained on Quandl (e.g. on Linux systems ```export QUANDL_KEY=<YOUR_API_KEY_HERE>```);
4. finally, to run the app, you should launch the script ```app.py``` on the python 3 interpreter. 