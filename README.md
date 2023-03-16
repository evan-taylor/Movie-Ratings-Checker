# Movie Data Checker

By Evan Taylor

## Description:

> This project is an interactive Python tool to search for movie ratings, decide what movie to watch based on which  has higher ratings, and search for an actor's most notable movie. This project utilizes the Open Movie Database (OMDb) API for a majority of the source ratings, and utilizes The Movie Database (TMDb) API to gather an actor's most notable movies.

## Usage:
> Begin by opening a terminal window with Python 3 installed. First, run `pip install -r requirements.txt` to install the dependencies for this project. You must then obtain an OMDb API key [here](https://www.omdbapi.com/apikey.aspx), and a TMDb API key [here](https://developers.themoviedb.org/3/getting-started/introduction). Please note that with the free access of the OMDb API you will be limited to 1,000 API requests per day. These keys are to be placed accordingly in the file named constants.py, to the corresponding variables OMDB_API_KEY and TMDB_API_KEY. You may then run python project.py, and select a mode.

## Available Modes:
There are three available modes, named ratings, compare, and actor. the program will prompt you to input a mode, and following the mode, will prompt you for either a movie name, two movie names to compare, or an actor's name

##### Ratings Mode:
> This mode will simply search the Open Movie Database and return both the IMDb rating and the Rotten Tomatoes rating for the movie.

##### Compare Mode:
> This mode will prompt you for two movies, inputted seperately, and will tell you which movie is rated higher and what the specific ratings are.

##### Actor Search Mode:
> This mode will prompt you to input an actor, and will return the actor's most notable movie, the release date, and a short synopsis of the film.



## Unit Testing:
> This project utilizes unit testing to verify that all of the functions are working as they are supposed to. All of the unit tests can be found in test_project.py.

Thank you for reading!
