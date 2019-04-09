# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:36:22 2019

@author: celia
"""
import pandas as pd
import fbprophet
from fbprophet import Prophet
datos=pd.read_csv("C:/Users/celia/OneDrive/Escritorio/aguathon/datos.csv",sep = ',')
datos=datos[['time','ZGZ_NR']]
datos.columns=['ds','y']    
date = pd.to_datetime(ds)

m = Prophet(holidays=holidays)
forecast = m.fit(df).predict(future)

m = Prophet()
m.add_regressor('precipitaciones')
m.fit(datos)


future = m.make_future_dataframe(periods=72,freq="1h")
future[24]
future.tail(1)
future.head()



pred72=future[future.index==95927]
pred48=future[future.index==95903]
pred24=future[future.index==95879]

future['precipitaciones'] = 

forecast = m.predict(pred72)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()



fig = m.plot_components(forecast)

