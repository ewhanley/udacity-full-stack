import webbrowser
import requests
import json
from operator import itemgetter


class Movie():

    """This class stores information about a movie.

    This class retrieves and stores data about movies from the
    www.themoviedb.org API. The class takes a movie title search string
    in as an argument and retrieves information about the movie including
    title, storyline, poster, and trailer.

    Atributes:
        title: A string that is the official title of the movie.
        storyline: A string that is a brief plot synopsis of the movie.
        poster_image_url: A string url for the movie poster.
        trailer_youtube_url: A string Youtube url for the movie trailer.

    Todo:
        * Add error handling to gracefully deal with movies with no
        response from API.
        * Check Youtube API to see if it supplies a value to determine
        whether or not a video can be embedded.
    """

    api_key = '{YOU_TMDb_API_KEY}'

    def __init__(self, movie_title):
        """Inits Movie with title, storyline, poster url, and trailer url.

        Args:
            movie_title (str): Movie title for API request
        """

        movie_id = self.get_movie_id(movie_title)
        response_dict = self.get_movie_info(movie_id)
        video_key = self.get_video_key(response_dict)

        self.title = response_dict['original_title']
        self.storyline = response_dict['overview']
        self.poster_image_url = ("https://image.tmdb.org/t/p/w342/" +
                                 response_dict['poster_path'])
        self.trailer_youtube_url = ("https://www.youtube.com/embed/" +
                                    video_key +
                                    '?autoplay=1&html5=1')

    def get_movie_id(self, movie_title):
        """This method gets the movie id by searching for the movie title.

        The themoviedb.org API can search movies by title, but this function
        retrives the id (integer) for the movie. The id can be used to request
        metadata about the specific movie as well as request the trailer.

        Args:
            movie_title (str): Movie title for API request

        Returns:
            Movie id converted to string for use in url construction

        """

        url = ("https://api.themoviedb.org/3/search/movie?api_key=" +
               Movie.api_key +
               "&language=en-US&query=" +
               movie_title +
               "&page=1&include_adult=false")

        payload = "{}"
        response = requests.request("GET", url, data=payload)
        response_dict = json.loads(response.text)

        # It is possible that a given search on movie title will return more
        # than one result. The following line sorts the results by the number
        # of themoviedb.org user votes.
        sorted_dict = sorted(response_dict['results'],
                             key=itemgetter('vote_count'),
                             reverse=True)

        # The id is selected for the movie with the highest vote count.
        movie_id = sorted_dict[0]['id']

        return str(movie_id)

    def get_movie_info(self, movie_id):
        """This method requests information for a given movie id

        Args:
            movie_id (str): themoviedb.org API unique id for movie

        Returns:
            Movie information (JSON) converted to Python dictionary

        """

        url = ("https://api.themoviedb.org/3/movie/" +
               movie_id +
               "?api_key=" +
               Movie.api_key +
               "&language=en-US&append_to_response=videos")

        payload = "{}"
        response = requests.request("GET", url, data=payload)
        response_dict = json.loads(response.text)
        return response_dict

    def get_video_key(self, response_dict):
        """This method gets the Youtube video key from the movie information.

        Args:
            response_dict (dict): API response containing movie information

        Returns:
            Youtube key (str) for movie trailer

        """

        video_key = None

        # Many movies return multiple available videos. The following line
        # sorts the results by the size (resolution) of the videos.
        sorted_dict = sorted(response_dict['videos']['results'],
                             key=itemgetter('size'),
                             reverse=True)

        # Not all available videos are trailers. The following iterates over
        # the results, selecting the first of the sorted videos that is a
        # trailer.  The second conditional selects only videos below 1080
        # resolution.  Several 1080 HD videos were restricted to only play on
        # Youtube and thus could not be embedded. This is a hacky way of
        # avoiding this issue.
        for video in sorted_dict:
            if video['type'] == "Trailer" and video['size'] < 1080:
                video_key = video['key']
                return video_key
