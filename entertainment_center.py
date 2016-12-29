from fresh_tomatoes import open_movies_page
from media import Movie


# Individual movie data
the_ridiculous_6 = Movie(
    'The Ridiculous 6',
    'https://upload.wikimedia.org/wikipedia/en/0/0d/The_Ridiculous_6_poster.jpg',
    'https://www.youtube.com/watch?v=qUp7Qgimn38'
)

train_to_busan = Movie(
    'Train To Busan',
    'https://upload.wikimedia.org/wikipedia/en/9/95/Train_to_Busan.jpg',
    'https://www.youtube.com/watch?v=pyWuHv2-Abk'    
)

xmen_apocalypse = Movie(
    'X-Men Apocalypse',
    'https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg',
    'https://www.youtube.com/watch?v=Jer8XjMrUB4'
)

dirty_grandpa = Movie(
    'Dirty Grandpa',
    'https://upload.wikimedia.org/wikipedia/en/6/62/Dirty_Grandpa_teaser_poster.jpg',
    'https://www.youtube.com/watch?v=aZSzMIFZT7Q'
)

ghostbusters = Movie(
    'Ghostbusters',
    'https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png',
    'https://www.youtube.com/watch?v=w3ugHP-yZXw'
)

the_man_who_knew_infinity = Movie(
    'The Man Who Knew Infinity',
    'https://upload.wikimedia.org/wikipedia/en/d/d8/The_Man_Who_Knew_Infinity_%28film%29.jpg',
    'https://www.youtube.com/watch?v=oXGm9Vlfx4w'
)


# Create movie webpage and open in the browser
open_movies_page([
    the_ridiculous_6, train_to_busan, xmen_apocalypse, dirty_grandpa,
    ghostbusters, the_man_who_knew_infinity,
])
