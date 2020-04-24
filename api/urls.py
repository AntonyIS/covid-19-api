from api import app


@app.route('/')
def index():
    # Landing page for the API Site
    return "Landing page"


@app.route('/api/v1/countries')
def get_countries():
    # Returns all countries with covid-19 cases
    return "Countries"


@app.route('/api/v1/countries/<int:country_id>')
def get_country(country_id):
    # Returns a country with covid-19 cases given country_id
    return "Country"


@app.route('/api/v1/states')
def get_states():
    # Returns all states with covid-19 cases given
    return "States"


@app.route('/api/v1/states/<int:states_id>')
def get_state(states_id):
    # Returns a state with covid-19 cases given state_id
    return "State"


# Authentication routes
@app.route('/api/v1/login')
def login_user():
    # Login using Social auth
    return "login"


@app.errorhandler(404)
def not_found(e):
    return "page not found", 404


@app.errorhandler(500)
def internal_error(e):
    return "Internal server error", 500