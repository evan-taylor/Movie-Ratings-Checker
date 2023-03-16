# Evan Taylor - Final Project
from project import getMovieRatingsData, compareMovies, searchByActor

# Test the getMovieRatingsData function by inputting Cars and Cars 2 and verifying the ratings are correct
def test_getMovieRatingsData():
    assert getMovieRatingsData("Cars") == ('7.2/10', '74%')
    assert getMovieRatingsData("Cars 2") == ('6.2/10', '39%')
    assert getMovieRatingsData("Cars") != "Pizza 🍕"

# Test the compareMovies function by inputting Cars and Cars 2 and verifying that Cars is the better movie
def test_compareMovies():
    assert compareMovies("Cars", "Cars 2") == "Cars has a higher rating than Cars 2, with an IMDB rating of 7.2/10 and a Rotten Tomatoes rating of 74%."
    assert compareMovies("Cars", "Cars 3") == "Cars has a higher rating than Cars 3, with an IMDB rating of 7.2/10 and a Rotten Tomatoes rating of 74%."
    assert compareMovies("Cars", "Forrest Gump") != "Cars is a better movie."

# Test the searchByActor function by inputting Owen Wilson and Paul Newman, and verifying that Cars is returned
def test_searchByActor():
    assert searchByActor("Owen Wilson") == ('Cars', "Lightning McQueen, a hotshot rookie race car driven to succeed, discovers that life is about the journey, not the finish line, when he finds himself unexpectedly detoured in the sleepy Route 66 town of Radiator Springs. On route across the country to the big Piston Cup Championship in California to compete against two seasoned pros, McQueen gets to know the town's offbeat characters.", '2006-06-08')
    assert searchByActor("paul newman") == ('Cars', "Lightning McQueen, a hotshot rookie race car driven to succeed, discovers that life is about the journey, not the finish line, when he finds himself unexpectedly detoured in the sleepy Route 66 town of Radiator Springs. On route across the country to the big Piston Cup Championship in California to compete against two seasoned pros, McQueen gets to know the town's offbeat characters.", '2006-06-08')
    assert searchByActor("Paul Newman") != "Cars 2"