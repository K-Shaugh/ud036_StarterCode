import webbrowser

class Movie():

    def __init__(self, movie_title, poster_image, trailer_youtube):
        #Initializes Movie class with title, poster image, and youtube trailer
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        #defines function to open the youtube trailer
        webbrowser.open(self.trailer_youtube_url)
