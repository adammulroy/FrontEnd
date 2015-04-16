__author__ = 'adam.mulroy'
import movie
import fresh_tomatoes

toy_story = movie.Movie('Toy Story',
                        'A boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = movie.Movie('Avatar',
                     'A marine on an alien planet',
                     'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

king_kong = movie.Movie('King Kong',
                        'A big ape and a babe',
                        'http://upload.wikimedia.org/wikipedia/en/6/6a/Kingkong_bigfinal1.jpg',
                        'https://www.youtube.com/watch?v=B5j_2sRUTbU')

# movies = [toy_story, avatar, king_kong]

# fresh_tomatoes.open_movies_page(movies)

print(movie.Movie.__doc__)
print(movie.Movie.__module__)
print(movie.Movie.__name__)
