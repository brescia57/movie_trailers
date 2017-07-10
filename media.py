import webbrowser


"""class Movie() is used as a way to store the attributes that
 we will use on all the different movies we elect to include in our program."""


class Movie():
    # __init__ is a built in function that allows us to initialize our method.
    # it is why we can use self to represent the object
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    # show_trailer makes use of the modal that pops out the movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
