import fresh_tomatoes
import media

big_trouble = media.Movie("Big Trouble in Little China",
                          "Jack Burton helps his friend rescue his fiancee from bandits",
                          "https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",
                          "https://youtu.be/592EiTD2Hgo")

_36th_chamber = media.Movie("36th Chamber of Shaolin",
                           "A young man learns Kung Fu",
                           "https://upload.wikimedia.org/wikipedia/en/9/91/The_36th_Chamber_of_Shaolin.jpg",
                           "https://youtu.be/P5_d0d-9ajU")

crouching_tiger = media.Movie("Crouching Tiger, Hidden Dragon",
                              "A man, a woman, and a legendary sword",
                              "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",
                              "https://youtu.be/gLpZ_5bHmo8")

fist_of_fury = media.Movie("Fist of Fury",
                           "A student fights to defend Chinese honor",
                           "https://upload.wikimedia.org/wikipedia/en/5/5b/FistofFuryHongKongposter.jpg",
                           "https://youtu.be/w_4RjSbSIFY")

kill_bill = media.Movie("Kill Bill Vol. 1",
                        "The bride swears vengeance on a team of assassins",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                        "https://youtu.be/7kSuas6mRpk")

drunken_master = media.Movie("Drunken Master",
                             "A young man runs into a series of troubles",
                             "https://upload.wikimedia.org/wikipedia/en/4/43/DrunkenMasterMoviePoster.jpg",
                             "https://youtu.be/KQMNllz6aE0")

movies = [big_trouble, _36th_chamber, crouching_tiger, fist_of_fury, kill_bill, drunken_master]

fresh_tomatoes.open_movies_page(movies)
