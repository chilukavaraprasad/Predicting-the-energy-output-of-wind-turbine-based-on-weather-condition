# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:49:30 2020

@author: Madhav Rathi
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import joblib

loaded_model = joblib.load('power_prediction.sav')

#X = [['Theoretical_Power_Curve (KWh)','WindSpeed(m/s)']]
print(loaded_model.predict([[416.328907824861,5.31133604049682]])[0],"KWh")

#predicted value is ['ActivePower(kW)']
