# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv") 
print(netflix_df.head())
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
print(netflix_subset)
netflix_movies=netflix_subset[['title', 'country','genre','release_year','duration']]
print(netflix_movies)
short_movies=netflix_movies[netflix_movies["duration"] < 60]
print(short_movies.head(20))
colors=[]
for  index,row in netflix_movies.iterrows():
    genre = row['genre']
    
    # Checking for specific genres and assigning colors accordingly
    if 'Children' in genre:
        colors.append('blue')
    elif 'Documentaries' in genre:
        colors.append('green')
    elif 'Stand-Up' in genre:
        colors.append('red')
    else:
        colors.append('orange')  # For other genres
    
# Ensure the colors list matches the length of the DataFrame
print(len(colors))
colors[:20]

fig=plt.figure(figsize=(12,8))
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()
answer = "maybe"
