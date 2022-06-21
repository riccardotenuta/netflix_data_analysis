import pandas as pd
import numpy as np
import csv

df = pd.read_csv('./drive/MyDrive/titles.csv')

movies_list = df.to_dict(orient = 'records')
from ast import literal_eval

from google.colab import drive
drive.mount('/content/drive')

len(movies_list)

movies_cleaned = []
final_list = []

def addCleanRow(newRow):
  movies_cleaned.append(newRow)
  
movies_genres_clean = []
# expand rows to have every row with one genre (and not array of string)
for movie in movies_list:
  genres = movie['genres']
  genres = literal_eval(genres)
   
  for genre in genres:
    newMovie = dict.copy(movie)
    newMovie['genre'] = genre
    
    addCleanRow(newMovie)
    
# expand rows to have evry row with one genre (and not array of string)
for movie in movies_cleaned:
  countries = movie['production_countries']
  countries = literal_eval(countries)
  
  for country in countries:
    newMovie = dict.copy(movie)
    newMovie['production_country'] = country
    
    final_list.append(newMovie)
    
    
header = ['id', 'title', 'type', 'description', 'release_year', 'age_certification', 'runtime', 
          'genres', 'production_countries', 'seasons', 'imdb_id', 'imdb_score', 'imdb_votes',
          'tmdb_popularity', 'tmdb_score']

with open('netflix_titles.csv', 'w', encoding='UTF8') as f:

  writer = csv.writer(f)

  # write the header
  writer.writerow(header)

  for row in final_list:
    
    row_file = [row['id'], row['title'], row['type'], row['description'], row['release_year'], 
                row['age_certification'], row['runtime'], row['genre'], row['production_country'], row['seasons'], 
                row['imdb_id'], row['imdb_score'], row['imdb_votes'], row['tmdb_popularity'], row['tmdb_score']]

    writer.writerow(row_file)
