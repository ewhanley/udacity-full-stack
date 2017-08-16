import webbrowser
import requests
import json
from operator import itemgetter

class Movie():
    """ This class provides a way to store movie related information."""    
    def __init__(self, movie_id):
        api_key = {YOUR_TMDB_API_KEY}
        lang = 'en-US'
        url = "https://api.themoviedb.org/3/movie/"+movie_id+"?api_key="+api_key+"&language="+lang+"&append_to_response=videos"

        payload = "{}"
        response = requests.request("GET", url, data=payload)
        resp_dict = json.loads(response.text)
        video_key = self.get_video_key(resp_dict)
        
        self.title = resp_dict['original_title']
        self.storyline = resp_dict['overview']
        self.poster_image_url = "https://image.tmdb.org/t/p/w342/"+resp_dict['poster_path']
        self.trailer_youtube_url = "https://www.youtube.com/embed/"+video_key+'?autoplay=1&html5=1'
        
        

    def get_video_key(self, response_dict):
        video_key = None
        sorted_dict = sorted(response_dict['videos']['results'], key=itemgetter('size'), reverse=True)
        
        for video in sorted_dict:
            if video['type'] == "Trailer" and video['size'] < 1080:
                video_key = video['key']
                return video_key
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

