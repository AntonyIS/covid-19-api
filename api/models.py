from api import db


class Country(db.Model):
    """
    A class that translates to be the Country table
    Defines the columns for the Country table
    """
    __tablename__ = "countries"
    name = db.Column(db.Integer,index=True, primary_key=True)
    flag = db.Column(db.String(255), nullable=True)
    total_infected = db.Column(db.Integer, nullable=False)
    infected_today = db.Column(db.Integer, nullable=False)
    total_deaths = db.Column(db.Integer, nullable=False)
    deaths_today = db.Column(db.Integer, nullable=False)
    total_recovered = db.Column(db.Integer, nullable=False)
    recovered_today = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)
    critical = db.Column(db.Integer, nullable=False)
    tests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.name


class States(db.Model):
    """
    A class that translates to be the State table
    Defines the columns for the State table
    """
    __tablename__ = "states"
    name = db.Column(db.Integer,index=True, primary_key=True)
    country_id = db.Column(db.Integer, nullable=False)
    total_infected = db.Column(db.Integer, nullable=False)
    infected_today = db.Column(db.Integer, nullable=False)
    total_deaths = db.Column(db.Integer, nullable=False)
    deaths_today = db.Column(db.Integer, nullable=False)
    total_recovered = db.Column(db.Integer, nullable=False)
    recovered_today = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)
    critical = db.Column(db.Integer, nullable=False)
    tests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.name