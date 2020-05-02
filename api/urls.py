from celery.beat import logger

from api import app, jsonify,Response, db
from api.models import Country, State
from api.tasks import Scrapper
from api import celery






# @app.route('/', methods=['GET'])
# def index():
#     db.drop_all()
#     db.create_all()
#     return 'home'

@app.route('/covid19/api/v1/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    print(len(countries))
    if len(countries) <= 0 :
        return jsonify({"message": "No data available"})
    else:
        # Returns all countries with covid-19 cases
        return jsonify(countries=[c.serialize_country() for c in countries])


@app.route('/covid19/api/v1/countries/<int:country_id>', methods=['GET'])
def get_country(country_id):
    country = Country.query.get(country_id)
    if country is None:
        return jsonify({"message": "data does not exist"})
    else:
        # Returns a country with covid-19 cases given country_id
        return jsonify({"country":country.serialize_country()})


@app.route('/covid19/api/v1/states', methods=['GET'])
def get_states():
    states = State.query.all()
    if len(states) <= 0 :
        return jsonify({"message": "data does not exist"})
    else:
        # Returns all states with covid-19 cases given
        return jsonify(states=[state.serialize(state) for state in states])


@app.route('/covid19/api/v1/states/<int:state_id>', methods=['GET'])
def get_state(state_id):
    # Returns a state with covid-19 cases given state_id
    try:
        return jsonify({
            "state": State.query.get(state_id).serialize(State.query.get(state_id)),
        })
    except:
        return jsonify({"message": "data does not exist"})

# Total data
@app.route('/covid19/api/v1/sum', methods=['GET'])
def get_sum():
    countries = Country.query.all()
    total_infected = 0
    infected_today = 0
    total_deaths = 0
    deaths_today = 0
    total_recovered = 0
    recovered_today = 0
    active = critical = 0
    tests = 0
    if len(countries) > 0:
        for country in countries:
            total_infected += country.total_infected
            infected_today += country.infected_today
            total_deaths += country.total_deaths
            deaths_today += country.deaths_today
            total_recovered += country.total_recovered
            recovered_today += country.recovered_today
            active += country.active
            critical += country.critical
            tests += country.tests

        return jsonify({
                "data":{
                    "total_infected":total_infected,
                    "infected_today":infected_today,
                    "total_deaths": total_deaths,
                    "deaths_today":deaths_today,
                    "total_recovered": total_recovered,
                    "recovered_today": recovered_today,
                    "active": active,
                    "critical":critical,
                    "tests":tests
                }
            })
    else:
        return jsonify({"message": "data does not exist"})


# Authentication routes
@app.route('/covid19/api/v1/login')
def login_user():
    # Login using Social auth
    return "login"


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "resource does not exist"
    })


@app.errorhandler(500)
def internal_error(e):
    return "Internal server error", 500