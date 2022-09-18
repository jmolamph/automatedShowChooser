# jmolamph
import logging
import random


# return list of shows for the generator (future: creates list based on characteristics like genre, rating, etc.)
def get_shows():
    """
    Returns a list of shows to the user
    :return: list of shows

    Future: Grab the shows from MyAnimeList API, storing in a dataframe
    """
    shows = ["naruto", "naruto shippuuden", "one piece", "made in abyss", "spy x family", "saiki k"]
    return shows


# given a list of shows, choose one for me to watch
def run_generator():
    """
    Calls get_shows() to retrieve a list of shows, then chooses a random show to return from that list.
    :return: string show

    Future:
    """
    try:
        shows = get_shows()
        return shows[random.randint(0, len(shows)-1)]
    except IndexError:
        logging.error("Invalid index; shows size of 0.")
