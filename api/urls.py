from api import app, jsonify,Response, db
from api.models import Country, State


def normalize(country_name):
    names = [name.capitalize() for name in country_name.replace("-", " ").split()]
    return " ".join(names)

def rev_normalize(country_name):
    name = country_name.lower().split()
    return "-".join(name)



@app.route('/covid19/api/v1/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    if len(countries) <= 0 :
        return jsonify({"message": "No data available"})
    else:
        # Returns all countries with covid-19 cases
        return jsonify(countries=[country.serialize_country() for country in countries])


@app.route('/covid19/api/v1/countries/<string:country_name>', methods=['GET'])
def get_country(country_name):
    country = Country.query.filter_by(name=normalize(country_name)).first()
    if country is None:
        return jsonify({"message": "data does not exist"})
    else:
        dict_country = country.serialize_country()
        dict_country['url'] = "http://127.0.0.1:5000/covid19/api/v1/countries/{}/states".format(rev_normalize(country.name))
        # Returns a country with covid-19 cases given country_id
        return jsonify({"country":dict_country})

@app.route('/covid19/api/v1/countries/<country_name>/states', methods=['GET'])
def get_country_states(country_name):
    country_name = normalize(country_name)
    country = Country.query.filter_by(name=country_name).first()
    if country is None:
        return jsonify({"message": "data does not exist"})
    else:
        # Returns states for country with covid-19 cases given country_id
        get_states = State.query.filter_by(country_name=country.name).all()
        states = [state.serialize_state() for state in get_states]
        return jsonify(
            {
                "country":country.serialize_country(),
                "states":states
            }
        )


@app.route('/covid19/api/v1/countries/<string:country_name>/states/<string:state_name>', methods=['GET'])
def get_country_state(country_name,state_name):
    country_name = normalize(country_name)
    state_name = normalize(state_name)
    country = Country.query.filter_by(name=country_name).first()
    if country is None:
        return jsonify({"message": "data does not exist"})
    else:
        # Returns state for country with covid-19 cases given country_id
        state = State.query.filter_by(name=state_name).first()
        state = state.serialize_state()
        state['url'] = "http://127.0.0.1:5000/covid19/api/v1/countries/{}/states".format(rev_normalize(country.name))
        return jsonify(
            {
                "state":state
            }
        )



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
        "countries" : "https://covid19-datamap-api.herokuapp.com/covid19/api/v1/countries",
        "country" : "https://covid19-datamap-api.herokuapp.com/covid19/api/v1/countries/<country_id>",
        "error": "resource does not exist",
    })


@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "message": "Internal server error",
        "Error" : e
    }), 500
