import csv
import random
import pandas as pd


movies = pd.read_csv('movies.csv')
movies = movies.dropna()

def search_random_movie():
	i = random.randint(1, 4250)
	movie = movies.iloc[i-2]
	return movie

def select_genre(genre):
	movie = movies[movies['genre'].str.contains(f'{genre}')]
	length = len(movie)
	i = random.randint(1, length)
	return movie.iloc[i-2] 



def find(info):
	movie = movies[movies['title'].str.contains(f'{info}')]
	if len(movie) == 0:
		movie = movies[movies['cast'].str.contains(f'{info}')]
	if len(movie) == 0:
		movie = movies[movies['film_director'].str.contains(f'{info}')]
	if len(movie) == 0:
		try:
			info = int(info)
			movie = movies[movies['year'] == info]
		except:
			pass
	length = len(movie)
	titles = movie.title
	return movie, length, titles


def main():
	pass


if __name__ == '__main__':
	main()


