from imdbpie import Imdb
from requests.exceptions import HTTPError


def imdb_movie_search(movie_name):
    imdb = Imdb()
    return imdb.search_for_title(movie_name)


def get_imdb_movie(imdb_id):
    imdb = Imdb()
    try:
        movie = imdb.get_title_by_id(imdb_id)
    except HTTPError as e:
        return None

def imdb_person_search(person_name):
    imdb = Imdb()
    return imdb.search_for_person(person_name)


def get_imdb_person(imdb_id):
    imdb = Imdb()
    try:
        movie = imdb.get_person_by_id(imdb_id)
    except HTTPError as e:
        return None