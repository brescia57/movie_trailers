"""I imported fresh_tomatoes and media as seperate files.
fresh_tomatoes was pre-packaged, and media was one i created."""  
import fresh_tomatoes
import media

# each film has the same attributes based on what was defined in the media file
# i used bitly to shorten the image urls
big_trouble = media.Movie("Big Trouble in Little China",
                          "Jack Burton helps his friend rescue his fiancee",
                          "http://bit.ly/2uaR3vs",
                          "https://youtu.be/592EiTD2Hgo")

_36th_chamber = media.Movie("36th Chamber of Shaolin",
                            "A young man learns Kung Fu",
                            "http://bit.ly/2tGYXtg",
                            "https://youtu.be/P5_d0d-9ajU")

crouching_tiger = media.Movie("Crouching Tiger, Hidden Dragon",
                              "A man, a woman, and a legendary sword",
                              "http://bit.ly/2tGCTiD",
                              "https://youtu.be/gLpZ_5bHmo8")

fist_of_fury = media.Movie("Fist of Fury",
                           "A student fights to defend Chinese honor",
                           "http://bit.ly/2uantWN",
                           "https://youtu.be/w_4RjSbSIFY")

kill_bill = media.Movie("Kill Bill Vol. 1",
                        "The bride swears vengeance on a team of assassins",
                        "http://bit.ly/2tGGtt3",
                        "https://youtu.be/7kSuas6mRpk")

drunken_master = media.Movie("Drunken Master",
                             "A young man runs into a series of troubles",
                             "http://bit.ly/2uaQ8Le",
                             "https://youtu.be/KQMNllz6aE0")

# the movie titles were stored as an array named movies
movies = [big_trouble, _36th_chamber, crouching_tiger, fist_of_fury, kill_bill,
          drunken_master]

# movies was then recalled using the method open_movies_page from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
