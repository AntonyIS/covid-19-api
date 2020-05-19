from bs4 import BeautifulSoup
import requests
from api import db, jsonify
from api.models import Country,State
import time

def rename(name):
    name = name.split()
    if name is None:
        return False
    elif len(name) == 1:
        return name[0].lower()
    elif len(name) == 2:
        item1 = name[0].lower()
        item2 = name[1].lower()
        return "{}-{}".format(item1,item2)

    elif len(name) == 3:
        item1 = name[0].lower()
        item2 = name[1].lower()
        item3 = name[2].lower()
        return "{}-{}-{}".format(item1, item2, item3)

    else:
        return False


class Scrapper:
    """
    A class that scraps data from different source and stores them into the database
    """
    def __init__(self):
        # Initializes URL_COUNTRIES variables that points to the site to be scapped
        self.URL_COUNTRIES = "https://corona.help/"

        # Initializes URL_COUNTRIES_FLAGS variables that points to the site to be scapped
        self.URL_COUNTRIES_FLAGS = "https://flaglog.com/"

        # Initializes URL_COUNTRIES_FLAGS variables that points to the site to be scapped
        self.URL_MORTALITY = "https://coronavirus.jhu.edu/data/mortality/"

    def add_states(self, country_name):
        name = country_name
        # scraps data about country's states from source and stores then in DB
        country_name = rename(country_name)
        try:
            page = requests.get(self.URL_COUNTRIES + "country/" + country_name)
            soup = BeautifulSoup(page.content, 'html.parser')
            tbody = soup.find("tbody")
            for tr in tbody.find_all("tr"):
                tds = tr.find_all("td")
                state_sample = State(
                    name= (tds[0].text).strip(),
                    country_name = name,
                    total_infected= int((tds[1].text).replace(',', '')),
                    infected_today = int((tds[2].text).replace(',', '')),
                    total_deaths = int((tds[3].text).replace(',', '')),
                    deaths_today = int((tds[4].text).replace(',', '')),
                    total_recovered = int((tds[5].text).replace(',', '')),
                    recovered_today = int((tds[6].text).replace(',', '')),
                    active = int((tds[7].text).replace(',', '')),
                    critical = int((tds[8].text).replace(',', '')),
                    tests = int((tds[9].text).replace(',', '')),
                )
                db.session.add(state_sample)
                db.session.commit()
                print(name,(tds[0].text).strip(),"...")
        except:
            return False

    def add_countries(self):
        # scraps data about countries from source and stores it the DB
        page = requests.get(self.URL_COUNTRIES)
        soup = BeautifulSoup(page.content, 'html.parser')
        tbody = soup.find("tbody")
        for tr in tbody.find_all("tr"):
            tds = tr.find_all("td")
            name = (tds[0].text).strip()
            country_sample = Country(
                name = name,
                flag = "flag",
                total_infected=int((tds[1].text).replace(',', '')),
                infected_today=int((tds[2].text).replace(',', '')),
                total_deaths=int((tds[3].text).replace(',', '')),
                deaths_today=int((tds[4].text).replace(',', '')),
                total_recovered=int((tds[5].text).replace(',', '')),
                recovered_today=int((tds[6].text).replace(',', '')),
                active=int((tds[7].text).replace(',', '')),
                critical=int((tds[8].text).replace(',', '')),
                tests =int((tds[9].text).replace(',', '')),
            )
            print(name,"...")
            db.session.add(country_sample)
            db.session.commit()
            self.add_states(name)

    def add_flags(self, country_name):
        # Scraps data(flag images) for countries from source and stores them in the images folder
        # country_name : takes country_name as argument to download the flag image
        pass


class Serializer:
    """
    Fetches data from the database tables and return serialized data
    """
    def __init__(self):
        self.countries = Country.query.all()
        self.states = State.query.all()

    def get_countries(self):
        # serialize countries
        # return jsonify(country=[c.serialize_country() for c in self.countries])
        for c in self.countries:
            # print(c.serialize_country())
            pass

    def get_country(self, country_id):
        # serialize country with given ID
        country = Country.query.get(country_id)
        return country.serialize_country

    def get_states_(self):
        return jsonify(state=[s.serialize for s in self.states])


    def job(self):
        print("Start task...")
        start = time.time()
        scrapper = Scrapper()
        db.drop_all()
        db.create_all()
        scrapper.add_countries()
        end = time.time()
        print("Ending Tasks...{}".format(end-start))

scrapper = Scrapper()
