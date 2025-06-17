import zipfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
#unzipping data set
zip_path = 'netflix_data.zip'
extract_dir = 'Netflix_shows_movies'
#Loading data set
df = pd.read_csv(f"{extract_dir}/netflix_data.csv")
#Data cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())
#Handling missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
#drop remaining missing values in 'duration'
df.dropna(subset=['duration'],inplace=True)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
#Data exploration
print("\nStatistical Summary:")
print(df.describe(include='all'))
#identify unique values in categorical columns
print("\nUnique values in 'type':", df['type'].unique())
print("Unique values in 'rating':", df['rating'].unique())

#visualization of data
plt.figure(figsize=(15,10))
# Most watched genres
plt.subplot(2, 2, 1)
top_genres = df['listed_in'].str.split(', ').explode().value_counts().head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, hue=top_genres.index,
            dodge=False, palette='viridis', legend=False)

# Ratings distribution
plt.subplot(2, 2, 2)
ratings_order = df['rating'].value_counts().index
sns.countplot(data=df, y='rating', order=ratings_order, hue='rating',
              palette='magma', legend=False)
plt.title('Distribution of Content Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')

# Release year distribution
plt.subplot(2, 2, 3)
sns.histplot(df['release_year'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')

# Type proportion (Movies vs TV Shows)
plt.subplot(2, 2, 4)
type_counts = df['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Proportion of Movies vs TV Shows')

plt.tight_layout()
plt.show()
