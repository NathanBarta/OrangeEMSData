# OrangeEMSData
Correlating rainfall with EMS response times in Orange county North Carolina.

## Doccumentation
The file (EMSDATA.py) has 3 different functions, and is a workspace, so stuff is commented out depending on what step of the process I was on.

Steps:
* Take the weather data (compiled manualy by my group mates, bless their hearts), and create a point (x,y) where x is the volume of rainfall, and y is the total EMS response time from the second the wheels on the ambulance started rolling. This was almost 1/2 a million points of data.
* Pickle the data points from the previous steps because they are going to get used a lot, and pickling is fast.
* Calculate a linear regression on the data.
* Make a plot.

## Challenges
One of the biggest challenges was working with the data, all 489657 points of it. Step 1 initialy took 1:05min per 1000 calls, but I was able to reduce it to 0:53min per 1000 calls. After I did that I was able to reduce it to a glorious 0:06min per 1000 calls, which saved me hours of computing time. I think I did this by abstracting some dataframe cleaning, something to do with string concatination, and some conditional logic - but I cannot remember. 

We also had only 3 days from start to finish to complete the analysis.

## Notes & findings & theory
I have removed the data from this project since it was not given to me to share. I can't find the charts, but I remember that we determined that EMS services are slightly corrilated with rainfall, having a small decrease in response time the more it is raining outside. We did not have access to trip distance data, but assuming the 100's of calls each day represent a decent sample our theory is that there are less people on the road to impede the ambulance, giving the driver a more efficient time. This analysis is slightly flawed of course, but its the best we could do.
