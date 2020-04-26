from api import app, jsonify, Response
from api.models import Country, State


@app.route('/covid19', methods=['GET'])
def index():
    # Landing page for the API Site
    return "Landing page"


@app.route('/covid19/api/v1/countries', methods=['GET'])
def get_countries():
    # Returns all countries with covid-19 cases
    return jsonify(countries=[c.serialize_country() for c in Country.query.all()])


@app.route('/covid19/api/v1/countries/<int:country_id>', methods=['GET'])
def get_country(country_id):
    # Returns a country with covid-19 cases given country_id
    return jsonify({
        "country":Country.query.get(country_id).serialize_country(),
    })


@app.route('/covid19/api/v1/states', methods=['GET'])
def get_states():
    # Returns all states with covid-19 cases given
    return jsonify(states=[state.serialize(state) for state in State.query.all()])


@app.route('/covid19/api/v1/states/<int:state_id>', methods=['GET'])
def get_state(state_id):
    # Returns a state with covid-19 cases given state_id
    try:
        return jsonify({
            "state": State.query.get(state_id).serialize(State.query.get(state_id)),
        })
    except:
        return "no states"


# Authentication routes
@app.route('/covid19/api/v1/login')
def login_user():
    # Login using Social auth
    return "login"


@app.errorhandler(404)
def not_found(e):
    return "page not found", 404


@app.errorhandler(500)
def internal_error(e):
    return "Internal server error", 500