# Evan Taylor - Final Project
# IMDB Rating Checker
# Youtube Video: https://youtu.be/yMtI3zUl-Xk

# Import the required system modules to run the program
import calendar
import os
import sys

# Import the constants file so that we may get our API keys
import constants
# Import the tmdbsimple and omdbapi modules so that we can use their functions
import tmdbsimple as tmdb
from omdbapi.movie_search import GetMovie

# Set the API keys to variables so that we can use them in the program
TMDBApiKey = constants.TMDB_API_KEY
tmdb.API_KEY = TMDBApiKey

apiKey = constants.OMDB_API_KEY
movie = GetMovie(api_key=apiKey)


# Define the main function
def main():
    # Prompt the user to input what mode they would like to use
    mode = input(
        "Please enter what mode you would like to use. [ratings|compare|actor]: "
    )
    # If the user inputs "ratings", then run the ratings mode
    if mode == "ratings":
        # Prompt the user to input the title of the movie they would like to check the ratings for
        movieTitle = input(
            "Please enter the title of the movie you would like to check the ratings for: "
        )
        # Try to get the ratings data for the movie. If the movie is not found, then print an error message
        try:
            # Run the getMovieRatingsData function, passing in the movie title, to get the ratings for the movie
            movieRatings = getMovieRatingsData(movieTitle)
            # Print the ratings for the movie
            print(
                f"{movieTitle.title()} has an IMDB rating of {movieRatings[0]} and a Rotten Tomatoes rating of {movieRatings[1]}."
            )
        # If the movie isn't found, print the error message
        except IndexError:
            print(
                f"{movieTitle.title()} was not found. Please ensure that you spelled the title correctly."
            )
    # If the user inputs compare, then run the compare mode
    elif mode == "compare":
        # Prompt the user to input the titles of the two movies they would like to compare
        movieTitle1 = input(
            "Please enter the title of the first movie you would like to compare: "
        )
        movieTitle2 = input(
            "Please enter the title of the second movie you would like to compare: "
        )
        # Run the compareMovies function, passing in the two movie titles, to compare the two movies
        decidedMovie = compareMovies(movieTitle1, movieTitle2)
        # Print the result of the comparison
        print(decidedMovie)
    # If the user inputs actor, then run the actor mode
    elif mode == "actor":
        # Prompt the user to input the name of the actor they would like to search for
        actorName = input(
            "Please enter the name of the actor you would like to search for: "
        )
        # Try to get the most notable movie for the actor. If the actor is not found, then print an error message
        try:
            # Run the searchByActor function, passing in the user provided actor name
            topMovieResult = searchByActor(actorName)
            # Set the movie date varible to the second item in the topMovieResult tuple
            movieDate = topMovieResult[2]
            # Split the movie date into year, month, and day
            year, month, day = movieDate.split("-")
            # Convert the month number that was given by the API to a month name using the calendar module
            month = calendar.month_name[int(month)]
            # Set the movie title and overview variables to the first and second items in the topMovieResult tuple
            movieTitle = topMovieResult[0]
            movieOverview = topMovieResult[1]
            # Print the most notable movie for the actor
            print(
                f"{actorName.title()}'s most famous movie is {movieTitle}, which was released on {month} {day}, {year}. Here is an overview of {movieTitle}:\n{movieOverview}."
            )
        # If the actor isn't found, print the error message
        except TypeError:
            print(
                f"{actorName.title()} was not found. Please ensure that you spelled the name correctly."
            )
    # If the user inputs anything but these three modes, then print an error message
    else:
        sys.exit("That is not a valid mode. Please try again.")


# Define the getMovieRatingsData function, passing in the movie title
def getMovieRatingsData(movieTitle):
    # Get the ratings data for the movie through the omdbapi module
    data = movie.get_movie(movieTitle)
    # If the API returns "Movie not found!", then print an error message and exit the program
    if data == "Movie not found!":
        sys.exit(
            "That movie was not found. Please ensure that you spelled the title correctly."
        )
    # Set the ratings data to a variable
    ratingsSources = data["ratings"]
    # Set the IMDB and Rotten Tomatoes ratings to variables
    IMDBData = ratingsSources[0]
    RottenTomotoesData = ratingsSources[1]
    # Get the values of both of the key-pair values in the dictionary
    RottenTomatoesRating = RottenTomotoesData["Value"]
    IMDBRating = IMDBData["Value"]
    # Return the IMDB and Rotten Tomatoes ratings
    return IMDBRating, RottenTomatoesRating

# Define the compare movies function, passing in both movie titles
def compareMovies(movieTitle1, movieTitle2):
    # Get the ratings data for both movies, using the getMovieRatingsData function
    movieRatings1 = getMovieRatingsData(movieTitle1)
    movieRatings2 = getMovieRatingsData(movieTitle2)
    # Compare the ratings of the two movies
    if movieRatings1 > movieRatings2:
        # If the first movie has a higher rating, set that result variable and provde the ratings
        result = f"{movieTitle1.title()} has a higher rating than {movieTitle2.title()}, with an IMDB rating of {movieRatings1[0]} and a Rotten Tomatoes rating of {movieRatings1[1]}."
    elif movieRatings1 < movieRatings2:
        # If the second movie has a higher rating, set the result variable and provide the ratings
        result = f"{movieTitle2.title()} has a higher rating than {movieTitle1.title()}, with an IMDB rating of {movieRatings2[0]} and a Rotten Tomatoes rating of {movieRatings2[1]}."
    # Return that result
    return result

# Define the searchByActor function, passing in the actor name
def searchByActor(actorName):
    # Search for the actor using the tmdb module
    search = tmdb.Search()
    response = search.person(query=actorName)
    # Get the most notable movie for the actor in the search results
    for s in search.results:
        # Set the movie list to the known_for value in the search results
        movieList = s["known_for"]
        # Set the movie list to the first item in the movie list, so we can get the most notable movie and only one movie.
        movieList = movieList[0]
        # Set the movie title, overview, and release date to variables
        movieTitle = movieList["title"]
        movieOverview = movieList["overview"]
        movieReleaseDate = movieList["release_date"]
        # Return the movie title, overview, and release date variables
        return movieTitle, movieOverview, movieReleaseDate

# Run the main function conditionally
if __name__ == "__main__":
    main()
