# Project 1: Movie Trailer Website

This is server-side code to store a list of some of my favorite movies. The list of movies is used to gather metadata about the movies from [The Movie DB's](https://www.themoviedb.org/) API. The metadata includes the movie's official title, plot summary, poster URL, and trailer URL. The metadata for all of the movies in the list is used to generate a website where visitors can browse the movie posters and watch their respective trailers.

## Motivation

This project is the first in a series of projects I am completing for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Getting Started

These instructions will get explain how to get a copy of this project running on your local machine.

### Prerequisites

* Python 2.x
* API Key from [www.themoviedb.org](https://www.themoviedb.org/documentation/api) 

### How to Run Project
1. Download or clone this repository to your machine:

        ```bash
        > git clone https://github.com/ewhanley/udacity-full-stack.git
        
        ```
2. Get an API key from TMDb by following the instructions [here](https://www.themoviedb.org/faq/api)
3. Once you have an API key, replace ```{YOUR_TMDb_API_KEY}``` with your key in line 29 of ```media.py```:
    
        ```python
        api_key = '{YOUR_TMDb_API_KEY}'
        
        ```
  
4. Save the changes to ```media.py``` and run ```entertainment_center.py``` from the command line:
  
        ```bash
        > python entertainment_center.py
        ```
5. Enjoy the movie trailers or add your own by title to ```entertainment_center.py```:

        ```python
        movie_titles = ['2001 space odyssey',
                        'apollo 13',
                        'the big lebowski',
                        'life aquatic',
                        'there will be blood',
                        'true grit',
                        '{YOUR MOVIE TITLE HERE}']
        ```

## Miscellaneous
* The file ```fresh_tomatoes.py``` is a slightly modified version a file supplied by Udacity as part of this project.
* This product uses the TMDb API but is not endorsed or certified by [TMDb](https://www.themoviedb.org).
* This README document is based on [this](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) template.

