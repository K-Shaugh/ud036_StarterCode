import fresh_tomatoes
import media

#Creates instances of media.Movie with title, movie poster url, and
#youtube url attributes

napolean_dynamite = media.Movie("Napolean Dynamite",
                                                "https://upload.wikimedia.org/wikipedia/en/8/87/Napoleon_dynamite_post.jpg",  # NOQA
                                                "https://youtu.be/ZHDi_AnqwN4")

tropic_thunder = media.Movie("Tropic Thunder",
                                             "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Tropic_thunder_ver3.jpg/220px-Tropic_thunder_ver3.jpg",  # NOQA
                                             "https://youtu.be/T-6YhRZowgc")

high_noon = media.Movie("High Noon",
                                       "https://upload.wikimedia.org/wikipedia/en/5/54/High_Noon_poster.jpg",  # NOQA
                                       "https://youtu.be/Gh-vOc-gwZs")                     

fight_club = media.Movie("Fight Club",
                                      "https://vignette1.wikia.nocookie.net/fightclub/images/6/6a/Fight-club-dvd.jpg/revision/latest?cb=20081116042426",  # NOQA
                                      "https://youtu.be/SUXWAEX2jlg")

new_hope = media.Movie("Star Wars: A New Hope",
                                      "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
                                      "https://youtu.be/1g3_CFmnU7k")

matrix = media.Movie("The Matrix",
                                 "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                                 "https://youtu.be/vKQi3bBA1y8") 

pick_of_destiny = media.Movie("Pick of Destiny",
                                              "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Tenacious_d_in_the_pick_of_destiny_ver3.jpg/220px-Tenacious_d_in_the_pick_of_destiny_ver3.jpg",  # NOQA
                                              "https://youtu.be/TXxQFMG86HA")

dodgeball = media.Movie("Dodgeball",
                                      "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Movie_poster_Dodgeball_A_True_Underdog_Story.jpg/220px-Movie_poster_Dodgeball_A_True_Underdog_Story.jpg",  # NOQA
                                      "https://youtu.be/W-XbDZUnUmw") 

good_will_hunting = media.Movie("Good Will Hunting",
                                                "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg",  # NOQA
                                                "https://youtu.be/nH9LZOXBMUE")

#open_movies_page function creates HTML page displaying
#the movies from the movies list

movies = [napolean_dynamite, tropic_thunder, high_noon,
                fight_club, new_hope, matrix, pick_of_destiny,
                dodgeball, good_will_hunting]

fresh_tomatoes.open_movies_page(movies)    

