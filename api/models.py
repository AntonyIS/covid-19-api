from api import db, jsonify


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
            "states" : [state.serialize(state) for state in State.query.filter_by(country_name=self.name).all()]

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

    def serialize(self, state, id=None):
        return {
            "id":state.id,
            "name" : state.name,
            "country_name" : state.country_name,
            "total_infected" : state.total_infected,
            "infected_today" : state.infected_today,
            "total_deaths" : state.total_deaths,
            "deaths_today" : state.deaths_today,
            "total_recovered" : state.total_recovered,
            "recovered_today" : state.recovered_today,
            "active" : state.active,
            "critical" : state.critical,
            "tests" : state.tests
        }