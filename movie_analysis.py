
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv('movies1.csv')

# Display the first few rows to understand the structure
df.head()

# Descriptive statistics for the budget column
budget_stats = df['budget'].describe()
print(budget_stats)

# Filter and count movies
us_pg13_count = df[(df['country'] == 'US') & (df['rating'] == 'PG-13')].shape[0]
print("Number of top-rated movies produced in the US with PG-13 rating:", us_pg13_count)

# Check if any movies meet the criteria
not_us_in_2014 = df[(df['year'] == 2014) & (df['country'] != 'United States')].shape[0] > 0
print("Any top-rated movies produced in 2014 that were not produced in the US:", not_us_in_2014)


# Define a function to count genres per movie
def count_genres(genres):
    if isinstance(genres, str):
        return len(genres.split(','))
    else:
        return 1  # or any other default value you want to assign to integer values

# Apply the function to the 'genres' column
genre_counts = df['genres'].apply(count_genres)

# Calculate percentages
total_movies = len(df)
genre_percentages = df.groupby('genres')['genres'].count() / total_movies * 100

print(genre_percentages)

df['budget'] = pd.to_numeric(df['budget'], errors='coerce')  # coerce will convert non-numeric values to NaN

# Convert budget and gross values to millions
df['budget_millions'] = df['budget'] / 1000000
df['gross_millions'] = df['gross'] / 1000000

# Round down to 2 decimal places
df['budget_millions'] = df['budget_millions'].apply(lambda x: round(x, 2))
df['gross_millions'] = df['gross_millions'].apply(lambda x: round(x, 2))

# Display the dataframe
df

# Calculate profit and sort
df['profit'] = df['gross'] - df['budget']
top_10_profit_movies = df.nlargest(10, 'profit')
print(top_10_profit_movies[['profit']])

# Assuming actors are in a column 'actors'
all_actors = df['actors'].str.split(', ').explode().unique()
all_actors_sorted = sorted(all_actors, key=lambda x: x.split()[0])  # Sort by first name
print(all_actors_sorted)

top_actors = df['actors'].str.split(', ').explode().value_counts().nlargest(3)
print("Top 3 actors by number of top-rated movies:", top_actors)

country_counts = df['country'].value_counts()
country_counts.plot(kind='bar', xlabel='Country', ylabel='Number of Movies', title='Top-rated Movies Production by Country')
plt.show()

# Find the country that produced the most top-rated movies
most_movies_country = country_counts.idxmax()
print("Country that produced the most top-rated movies:", most_movies_country)


country_counts = df['country'].value_counts()
country_counts.plot(kind='bar', xlabel='Country', ylabel='Number of Movies', title='Top-rated Movies Production by Country')
plt.show()

# Find the country that produced the most top-rated movies
most_movies_country = country_counts.idxmax()
print("Country that produced the most top-rated movies:", most_movies_country)









