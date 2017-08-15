import webbrowser
import requests
import json

class Movie():
    """ This class provides a way to store movie related information."""    
    def __init__(self, imdb_id):
        self.title = 
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def get_movie_info(self, imdb_id):
        url = 'https://theimdbapi.org/api/movie?movie_id='+imdb_id
        response = requests.get(url)
        response_dict = json.loads(response.text)
        self.title = response_dict['title']
        self.storyline = response_dict['description']
        self.poster_image_url = response_dict['poster']['larger']
        self.trailer_video_url = 

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    
        
