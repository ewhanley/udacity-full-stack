import media
import fresh_tomatoes

movie_titles = ['2001 space odyssey',
                'apollo 13',
                'the big lebowski',
                'life aquatic',
                'there will be blood',
                'true grit']

movies = []
for title in movie_titles:
    movies.append(media.Movie(title))

fresh_tomatoes.open_movies_page(movies)
