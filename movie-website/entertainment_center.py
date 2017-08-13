import media
import fresh_tomatoes

space_odyssey = media.Movie("2001: A Space Odyssey",
                        "A classic sci-fi epic painting an image of a future with routine space "
                            " travel and artificial intelligence gone awry.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg",
                        "https://www.youtube.com/watch?v=UgGCScAV7qU"
                        )

apollo_13 = media.Movie("Apollo 13",
                        "Engineering grit returns a group of imperiled astronauts safely back to earth.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
                        "https://www.youtube.com/watch?v=KtEIMC58sZo"
                        )

big_lebowski = media.Movie("The Big Lebowski",
                           "A slacker philosopher tries to abide in a complicated world.",
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y&t=7s"
                           )

life_aquatic = media.Movie("The Life Aquatic with Steve Zissou",
                           "An oceanographer seeks to destroy the Jaguar Shark that ate his partner.",
                           "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",
                           "https://www.youtube.com/watch?v=yh401Rmkq0o"
                           )

there_will_be_blood = media.Movie("There Will Be Blood",
                                  "A self-made oil baron's greed leads to self destruction.",
                                  "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg",
                                  "https://www.youtube.com/watch?v=FeSLPELpMeM"
                                  )
                                  
true_grit = media.Movie("True Grit",
                        "A washed-up drunken U.S. Marshall helps a girl track the murderer of her father.",
                        "https://upload.wikimedia.org/wikipedia/en/c/ce/True_Grit_Poster.jpg",
                        "https://www.youtube.com/watch?v=CUiCu-zuAgM"
                        )

movies = [space_odyssey, apollo_13, big_lebowski, life_aquatic, there_will_be_blood, true_grit]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
print(media.Movie.__module__)

                


                        

                           
