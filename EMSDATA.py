# coding: utf-8
import datetime as datetime
import numpy as np
import pandas as pd
import seaborn
import statsmodels
from matplotlib import pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression

# df = pd.read_csv("emsCleaned.csv")
# weatherData = pd.read_csv("Weather - Weather.csv")
# weatherDataLength = 2865
# df length: 489657

print("INITIATED")

# Corrilate response times to rainfall
responseTimeByRainX = []  # Rainfall that call
responseTimeByRainY = []  # Time to respond

# for call in range(0, 489656):
#   dateQuery = datetime.datetime.strptime(df["calltime"][call], "%m/%d/%Y %H:%M")  # Convert call time into datetime
#   dateQueryString = dateQuery.strftime("%m/%d/%Y")  # Strip to m/d/y format
#
#   precipitation = weatherData[weatherData['Date'] == dateQueryString]['Precipitation']
#
#   if len(precipitation) != 0:
#     p = precipitation.to_list()[0]
#     if p == "T":
#       responseTimeByRainX.append(0.0)  # TRACE (Ground wet)
#       responseTimeByRainY.append(df["secsdi2ar"][call] + df["secsdi2en"][call] + df["secs2lc"][call] + df["secs2tr"][call] + df["secs2ar"][call])
#     else:
#       responseTimeByRainX.append(float(p))
#       responseTimeByRainY.append(df["secsdi2ar"][call] + df["secsdi2en"][call] + df["secs2lc"][call] + df["secs2tr"][call] + df["secs2ar"][call])



# with open('responseTimeByRainX.pkl', 'wb') as f:
#   pickle.dump(responseTimeByRainX, f)
#
# with open('responseTimeByRainY.pkl', 'wb') as f:
#   pickle.dump(responseTimeByRainY, f)

with open('responseTimeByRainX.pkl', 'rb') as f:
  responseTimeByRainX = pickle.load(f)

with open('responseTimeByRainY.pkl', 'rb') as f:
  responseTimeByRainY = pickle.load(f)


  # +df["secs2en"][call]+df["secs2di"][call]+df["secs2rt"][call]) # Find seconds to get on scence

# print("Standard Deviation " + str(np.std(responseTimeByRainY, axis=0)))

print("CALCULATIONS START")

print(len(responseTimeByRainX), len(responseTimeByRainY))
responseTimeByRainX = np.asarray([responseTimeByRainX], dtype=np.float32).reshape(-1, 1)
#responseTimeByRainY = np.asarray([responseTimeByRainY], dtype=np.float32)
print(len(responseTimeByRainX), len(responseTimeByRainY))

model = LinearRegression()
model.fit(responseTimeByRainX, responseTimeByRainY)

print('intercept:', model.intercept_)
print('slope:', model.coef_)
print('R^2:', model.score(responseTimeByRainX, responseTimeByRainY))


# axes = plt.gca()
# axes.set_ylim([3000.0, 8000.0])
# 
# plt.xlabel("Rain Fall")
# plt.ylabel("Seconds")
# plt.title("Response by Rain")
# seaborn.regplot(responseTimeByRainX, responseTimeByRainY, color="red", robust=True, ci=0)
# 
# plt.show()

# PROGRAM SPEED: 1:05min per 1000 calls -> :53min per 1000 calls -> 0:06 per 1000 calls
