import media
import fresh_tomatoes

terminator_movie = media.Movie("Terminator 2: Judgment Day 3D Trailer #2 (2017)","T2","https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Terminator2poster.jpg/220px-Terminator2poster.jpg","https://www.youtube.com/watch?v=VVZQ39i5G1s")

rough_movie = media.Movie("Rough Night Trailer #1 (2017)","RNT","https://upload.wikimedia.org/wikipedia/en/0/03/Rough_Night.png","https://www.youtube.com/watch?v=kyIlMQvv-qk")

nerve_movie = media.Movie("Nerve Official Trailer #1 (2016)","NO","https://upload.wikimedia.org/wikipedia/en/thumb/3/3a/Nerve_2016_poster.png/220px-Nerve_2016_poster.png","https://www.youtube.com/watch?v=AX1BTiHzq-I")

#terminator_movie.show_trailer()

movies_arr = [terminator_movie,rough_movie,nerve_movie]

fresh_tomatoes.open_movies_page(movies_arr) 