install.packages("ggplot2")
install.packages("readr")

library(ggplot2)
library(readr)

df <- read_csv("Netflix_shows_movies.csv")

function(df) {
  # Prepare data: Count movies/TV shows by country (top 10)
  country_counts <- head(sort(table(df$country), decreasing=TRUE), 10)
  country_df <- data.frame(Country = names(country_counts), Count = as.numeric(country_counts))
  
  # Create ggplot bar plot
  p <- ggplot(country_df, aes(x=reorder(Country, -Count), y=Count, fill=Country)) +
    geom_bar(stat="identity") +
    labs(title="Top 10 Countries by Netflix Content Production",
         x="Country", y="Number of Titles") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle=45, hjust=1),
          legend.position="none")
  gplot(df, aes(y = rating)) +
    geom_bar(fill = "steelblue") +
    labs(title = "Distribution of Ratings on Netflix",
         y = "Rating", x = "Count") +
    theme_minimal()
  
  print(p)
  return(country_df)
}
"""

