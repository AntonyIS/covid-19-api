from api import db


def rev_normalize(country_name):
    name = country_name.lower().split()
    return "-".join(name)


class Country(db.Model):
    """
    A class that translates to be the Country table
    Defines the columns for the Country table
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    flag = db.Column(db.String(100), default="country flag")
    total_infected = db.Column(db.Integer, default=0)
    infected_today = db.Column(db.Integer, default=0)
    total_deaths = db.Column(db.Integer, default=0)
    deaths_today = db.Column(db.Integer, default=0)
    total_recovered = db.Column(db.Integer, default=0)
    recovered_today = db.Column(db.Integer, default=0)
    active = db.Column(db.Integer, default=0)
    critical = db.Column(db.Integer, default=0)
    tests = db.Column(db.Integer, default=0)
    url = db.Column(db.String)

    def __repr__(self):
        return self.name

    def serialize_country(self):
        return {
            "id": self.id,
            "name" : self.name,
            "flag" : self.flag,
            "total_infected" : self.total_infected,
            "infected_today" : self.infected_today,
            "total_deaths" : self.total_deaths,
            "deaths_today" : self.deaths_today,
            "total_recovered" : self.total_recovered,
            "recovered_today" : self.recovered_today,
            "active" : self.active,
            "critical" : self.critical,
            "tests" : self.tests,
            "url":" http://127.0.0.1:5000/covid19/api/v1/countries/{}".format(rev_normalize(self.name))

        }



class State(db.Model):
    """
    A class that translates to be the State table
    Defines the columns for the State table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    country_name = db.Column(db.String(100), index=True, nullable=False)
    total_infected = db.Column(db.Integer,  default=0)
    infected_today = db.Column(db.Integer,  default=0)
    total_deaths = db.Column(db.Integer,  default=0)
    deaths_today = db.Column(db.Integer,  default=0)
    total_recovered = db.Column(db.Integer,  default=0)
    recovered_today = db.Column(db.Integer,  default=0)
    active = db.Column(db.Integer,  default=0)
    critical = db.Column(db.Integer,  default=0)
    tests = db.Column(db.Integer,  default=0)

    def __repr__(self):
        return self.name


    def serialize_state(self, id=None):
        return {
            "id":self.id,
            "name" : self.name,
            "country_name" : self.country_name,
            "total_infected" : self.total_infected,
            "infected_today" : self.infected_today,
            "total_deaths" : self.total_deaths,
            "deaths_today" : self.deaths_today,
            "total_recovered" : self.total_recovered,
            "recovered_today" : self.recovered_today,
            "active" : self.active,
            "critical" : self.critical,
            "tests" : self.tests,
            "url": " http://127.0.0.1:5000/covid19/api/v1/countries/{}/states/{}".format(rev_normalize(self.country_name),rev_normalize(self.name))
        }