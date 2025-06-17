# Netflix-Assignment
## Importing libraries
I started by importing the necessary libraries which are :pandas,seaborn,matplotlib and seaborn.os enabled me interact with the operating system to read the CSV file which I saved in the same directory as my pycharm file.
### Unzipping data set
I created a function to unzip the file as required by the assignment.However,the file I downloaded was a CSV file and did not require unzipping.I created a function to read the CSV file and load the data set.
#### Cleaning data
I wrote a print function that prints missing values .I handled missing values by using fillna to fill the null(N/A) values.I dropped the remaining missing values in the subset of duration.This removed rows where duration column had missing values.I also generated descriptive statistics for release year,rating and type.After this,I listed all distinct values for type and rating

##### Data visualization
I plotted the most watched genres,ratings,release year distribution and type proportion graphs.

###### R script
I used ggplot library tp plot a bar plot graph showing the top 10 countries by Netflix content production.I also plotted a graph showing the distribution of ratings on netflix
