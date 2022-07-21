# Markowitz Portfolio Python
 - The general idea for this project was born out of my fascination with the excel analysis we did in for our second problem set. I wanted to take it a step further and I knew that using the excel solver was the constraining factor so I decided to look into ways to conduct Markowitz Portfolio optimization with Python/C (Python proved more fruitful). 
 - I loosely followed the form laid out in [this](https://plotly.com/python/v3/ipython-notebooks/markowitz-portfolio-optimization/) blog post by Dr. Thomas Stark if you want to learn more about my methodology
## Data Collection Methodology
 - I came up with a basket of 20 stocks. I selected part of them based on my own experience as an amatuer investor and biased my selection towards the companies which have brought me profits. Additionally, I grabbed some Buffet stocks in order to try to bring the volatility of my portfolio down. 
 - I wanted to focus on the historical performance of stocks right before the pandemic up until the present. I figure this has been an incredibly volatile time in the market and due to the limited time horizon I thought this was wise. 
	-  *I experimented with daily returns but the analysis was not particularly insightful. I found weekly returns to be the best balance of generating a large sample of observations while allowing for the stocks to move.* 
## Assumptions
 - I chose a risk free rate of **.00119** based off of the 1 month T-bill rate from when I was conducting my analysis. 
## Code Logic
 - I read the historical excess returns which I formatted by hand into a Pandas Data Frame
 - I generate either a million or ten million weights that sum up to 1 from the uniform distribution over the inteval [0,1). 
 - For each portfolio I then calculate the descriptive statistics (mean, standard deviation, and covariance)
 - Then for each of these portfolios I calculate the Sharpe Ratio
 - Finally I plot all of the points on our typical graph of standard deviation and mean return
## Results
 1.  I attached two of the graphs from my 10 million portfolio runs. It is fascinating to see that the points nearly align with one another. I did not end up using the results of the graphs because they were based on daily returns, but I still find the sheer size and clear similarity between the graphs fascinating. I have attached both graphs below:

![enter image description here](https://gist.githubusercontent.com/RyanLee64/aef5122978c686a6a169c720d5bfeaa5/raw/181b97453bc08c010e6d9cc45adbae6b93950f87/10mil_1.png)
![enter image description here](https://gist.githubusercontent.com/RyanLee64/aef5122978c686a6a169c720d5bfeaa5/raw/181b97453bc08c010e6d9cc45adbae6b93950f87/10mil_2.png)
2. I also will copy the result of my 1 million trial portfolios. The two yielded identical Sharpe Ratio with precision down to the thousandths place. I simply selected the portoflio out of the two I liked the most and constructed my Stock Track portfolio accordingly. I chose the second one 😃. 

PORT 1

sharp is: 0.24095153023196955

sharp std is 0.048466129028347564

sharp return is 0.012867987953800425

AAPL 7.921141857657061 %

BRK-A 1.064651568916461 %

CHWY 13.456444575441296 %

DAL 0.34704551081804796 %

EXPE 2.9425983449547033 %

F 8.64658846453009 %

JPM 2.3492752808964728 %

KO 0.5418920907373767 %

MDB 6.7129990029001565 %

MSFT 6.064913982167887 %

PTON 14.10674047422005 %

ROKU 2.4229708866957553 %

SEE 12.03706003672667 %

SPOT 3.259270992624958 %

STZ 1.5073538336008163 %

T 3.75236076900251 %

TT 6.1738542624799955 %

TWTR 1.5666686797777545 %

VMW 0.5986819235227606 %

Z 4.527487462329128 %

0.9999999999999993

-----------------------

PORT 2

sharp is: 0.24152649187956304

sharp std is 0.04963301798210808

sharp return is 0.013177688714613833

AAPL 4.200351851285923 %

BRK-A 2.880993213644299 %

CHWY 12.757326889219838 %

DAL 0.3569900037661306 %

EXPE 1.4079452894399702 %

F 4.189768018429537 %

JPM 3.523560407018205 %<D-d>

KO 6.165354705367957 %

MDB 3.6209416928359315 %

MSFT 4.652967522920829 %

PTON 13.280419709610053 %

ROKU 12.755963782580546 %

SEE 1.1901877138360435 %

SPOT 12.681584433473676 %

STZ 1.0581966680546526 %

T 0.2134153479052024 %

TT 10.816611479261736 %

TWTR 1.3784390729417422 %

VMW 1.3512315871960054 %

Z 1.517750611211738 %

1.0000000000000002
