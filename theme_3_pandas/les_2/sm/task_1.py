import pandas as pd
import ast

file_path = 'movies_metadata.csv'
movies = pd.read_csv(file_path)

movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')

movies['genres'] = movies['genres'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])

filtered_movies_1 = movies[movies['release_date'] > '1995-09-01']
print(filtered_movies_1[['title', 'release_date']])

print('------------------------------------------------------------------')

sorted_movies_runtime = movies.sort_values(by='runtime', ascending=True)
print(sorted_movies_runtime[['title', 'runtime']])

print('------------------------------------------------------------------')


threshold_votes = movies['vote_count'].max() * 0.5
filtered_movies_3 = movies[movies['vote_count'] > threshold_votes]
print(filtered_movies_3[['title', 'vote_count']])

print('------------------------------------------------------------------')


filtered_movies_4 = movies[movies['revenue'] > 100_000_000]
print(filtered_movies_4[['title', 'revenue']])

print('------------------------------------------------------------------')


filtered_movies_5 = movies[movies['genres'].apply(lambda genres: any(genre['name'] == 'History' for genre in genres))]
print(filtered_movies_5[['title', 'genres']])