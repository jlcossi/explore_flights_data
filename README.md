# Explore flights Data

## Dataset

The data consisted of 73546 records of flights, for the US, over 5 years, 
from 1987 to 1992. As the original files were too big, I created some random 
samples for this learning study. 
There are time variables (mainly expected times and delays), numeric variables 
and text variables such are origins, destinations and carriers' names.   
Those data files have been selected from [here](http://stat-computing.org/dataexpo/2009/the-data.html).  
A detailed presentation of the data is available [here](https://www.transtats.bts.gov/Fields.asp?Table_ID=236).  



## Summary of Findings

Starting with the exploration, I found that 1.1% of the flights were cancelled.  
Chicago was the top number one city, home for more cancellations. 
US Airways appeared to be the carrier having the most cancelled flight.
While trying to find another feature related to the cancellation or the 
delaying, I found out that the arrival delays was a right skewed distribution. 
I applied zooming and axis limits to be able to focus on the bulk of the data. 
It visually showed flights delays from -40 minutes (earlier arrivals) to 80 minutes. 
Next, regarding cancelled flights, I dived into relationships between 
destinations and carriers codes. Indeed, for Chicago as arrival city, 
American Airlines and United Airlines are the carriers with the most 
cancelled flights. For Boston, US Airways appears to be the one 
with the most cancelled flights. For Atlanta, Easten Airlines and Delta 
Airlines are also the carriers with the most cancelled flights.
I explored the same relationships for delayed flights, examining 
destinations versus carriers codes. For all the arrival cities with delays, 
the top three carriers which are the mostly late are American Arilines, 
AS Airways and Delta Airlines.
Back to cancelled fligths again, I explored a third feature: the planned 
flight durations. Eastern Airlines and Delta Airlines cancelled flights, mostly 
planned for Atlanta are short and medium-haul flights. American Airlines and 
United Airlines cancelled flights, mostly planned 
for Chicago are also short and medium-haul flights. 
The third feature I explored for delayed flights (on arrival) was departure delays. 
I noticed that, especially for Chicago and Atlanta, we have departure delays for all the 
carriers. 
Indeed there other parameters - meteo for example - which could also give 
more explanations, but are not covered in this short study.


## Key Insights for Presentation

For the presentation, first, I focused on just the influence of carriers and the cities 
on the cancellations. I started by examining cancellations, cities and carriers 
as categorical variables one by one. Then I dived in to their relationships, 
cancellations and cities, then cancellations with carriers. Finally I 
observed the influence of the planned flights duration as a third feature, on 
the cancellations.
Regarding delayed flights, I started also with the influence of carriers and cities.
Then I added a third parameter, which is the departure delays.
