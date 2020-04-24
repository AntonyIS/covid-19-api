from bs4 import BeautifulSoup
import requests


class Scrapper:
    """
    A class that scraps data from different source and stores them into the database
    """
    def __init__(self):
        # Initializes URL_COUNTRIES variables that points to the site to be scapped
        self.URL_COUNTRIES = "https://corona.help/"

        # Initializes URL_COUNTRIES_FLAGS variables that points to the site to be scapped
        self.URL_COUNTRIES_FLAGS = "https://flaglog.com/"

    def add_countries(self):
        # scraps data about countries from source and stores it the DB
        pass

    def add_states(self):
        # scraps data about country's other states from source and stores then in DB
        pass

    def add_flags(self, country_name):
        # Scraps data(flag images) for countries from source and stores them in the images folder
        # country_name : takes country_name as argument to download the flag image
        pass
