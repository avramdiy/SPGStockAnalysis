# TRG Week 22

## Stock Analysis

- Analysis of Simon Property Group ($SPG).

- $SPG is a REIT that invests in shopping malls, outlet centers, and community/lifestyle centers.

- This REIT is the largest owner of shopping malls in the USA, owning interests in 232 properties as of 2021. 

- Link To Dataset : https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

### 1st Commit

- Initiate FlaskAPI script to load initial HTML Dataframe to begin cleaning data.

### 2nd Commit

- Adjust DF to show organized columns with the correct header names of "Date" "Open" "High" "Low" "Close" "Volume" "OpenInt"

- Drop the "OpenInt" column

### 3rd Commit

- While keeping the current script, I want to visualize a new route and plot, that shows the average "Open" price for the years 2005 to 2017. The Y-axis should indicate the price, and the X-axis should indicate each year.

### 4th Commit

- While keeping the same plot and visualization, I want to visualize the same range of years, showing the yearly average "Close" price as a transparent red. I also want to change the color of the "Open" price visualization to green.

- The bar chart overlay is a poor way of communicating data. I will make both charts line plots.

- Turns out the prices of Open and Close are almost the same. I will combine the data from the average Open and Close yearly data to create a Yearly Median Average Price Plot in blue. I want to show a legend in the same chart, showing the prices for the yearly average Open and Close prices, so in-depth analysis correlates to the newly constructed line.

### 5th Commit

- From the last visualization, I can see a decline in price average from the years 2008 - 2009, and the years 2016 - 2017.

- I will create a new route and plot that charts the monthly average close price for the years of 2008 and 2016.

- The X axis will show all months from January to December. The Y-axis will show the price points.

- The 2008 data will be plotted as a red line, while the 2016 data will be plotted as a blue line on the same chart.

- You can see a clear price drop in September to the end of 2008 or the end of 2016.