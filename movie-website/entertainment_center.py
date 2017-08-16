import media
import fresh_tomatoes

space_odyssey = media.Movie('62')

apollo_13 = media.Movie('568')

big_lebowski = media.Movie('115')

life_aquatic = media.Movie('421')

there_will_be_blood = media.Movie('7345')
                                  
true_grit = media.Movie('44264')

movies = [space_odyssey, apollo_13, big_lebowski, life_aquatic, there_will_be_blood, true_grit]
fresh_tomatoes.open_movies_page(movies)

