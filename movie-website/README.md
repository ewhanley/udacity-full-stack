# Project 1: Movie Trailer Website

## Synopsis

This is server-side code to store a list of some of my favorite movies. The list of movies is used to gather metadata about the movies from [The Movie DB's](https://www.themoviedb.org/) API. The metadata includes the movie's official title, plot summary, poster URL, and trailer URL. The metadata for all of the movies in the list is used to generate a static web page that lets visitors browse the movie posters and watch their respective trailers.

## Motivation

This project is the first in a series of projects I am completing for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). 

## Required Libraries and Dependencies

* Python 2.x
* API Key from [www.themoviedb.org](https://www.themoviedb.org/documentation/api) 

## How to Run Project
1. Get an API key from TMDb by following the instructions [here](https://www.themoviedb.org/faq/api)
2. Once you have an API key, replace ```{YOUR_TMDb_API_KEY}``` with your key in line 29 of ```media.py```:

    ```python
    api_key = '{YOUR_TMDb_API_KEY}'
    ```
  
3. Save the changes to ```media.py``` and run ```entertainment_center.py``` from the command line:
  
    ```bash
    python entertainment_center.py
    ```



## Extra Credit Description



## Miscellaneous

