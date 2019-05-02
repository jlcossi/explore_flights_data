# Explore flights Data

## Dataset

The data consisted of 73546 records of flights, for the US, over 5 years. 
There are time variables (mainly expected times and delays), numeric variables 
and text variables such are origins, destinations and carriers' names. 
Those data files have been selected from [here](http://stat-computing.org/dataexpo/2009/the-data.html)
A detailed presentation of the data is available [here](https://www.transtats.bts.gov/Fields.asp?Table_ID=236)
As the original files were too big, I created a random sample 
of the original files I chose to use.


## Summary of Findings

In the exploration, I found that for the 1.1% of the cancelled, the most 
arrival city was Chicago. US Airways appeared to be the one having the 
most cancelled flight.
While trying to find another feature related the cancellation of the 
delaying, I found out that the arrival delays was a right skewed distribution. 
I applied zooming and axis limits to be able to focus on the bulk of the data. 
It visually showed flights delays from -40 minutes to 80 minutes. 
Next, for cancelled flights, I dived into relationships between 
destinations and carriers codes. Indeed, for Chicago as arrival city, 
American Airlines and United Airlines are the carriers with the most 
cancelled flights. For Boston, US Airways appears to be the one 
with the most cancelled flights. For Atlanta, Easten Airlines and Delta 
Airlines are the carriers with the most cancelled flights.
I explored the same relationships for delayed flights, examining 
Destinations versus carriers codes. For all the arrival cities with delays, 
the top three carriers which are the mostly late are American Arilines, 
AS Airways and Delta Airlines.
Back to cancelled fligths again, I explored a. third feature: the planned 
flight durations. EA and DL cancelled flights, mostly planned for Atlanta 
are short and medium-haul flights. AA and AU cancelled flights, mostly planned 
for Chicago are also short and medium-haul flights. CO, US and NW cancelled 
flights, mostly planned for Boston are rather short-haul flights.
The third feature I explored for delayed flights (on arrival) was departure delays. 
I noticed that, especially for Chicago, we have departure delays for all the 
carriers. For Denver (as arrival city) we have departure delays mainly for 
American Airlines and Delta Airlines.
Indeed there other parameters - meteo for example - which could also give 
more explanations.


## Key Insights for Presentation

For the presentation, First, I focus on just the influence of carrier and the city 
on the cancellations. I started by examining cancellations, cities and carriers 
as categorical variables one by ones. Then I dived in to their relationships, 
cancellations and cities, then cancellations with carriers and finally I 
observed the influence of the planned flights duration as a third feature.
Regarding delayed flights, I started also with the influence of carriers and cities.
Then I added a third parameter, which is the departure delays.
