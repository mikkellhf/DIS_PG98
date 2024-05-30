from flask import render_template,request, Blueprint
from DIS_Project.models import search_country

Search = Blueprint('Search', __name__)

posts = [{}]


@Search.route("/")
def home():
    return render_template('home.html')


@Search.route("/about")
def about():
    return render_template('about.html', title='About')

@Search.route('/search', methods=['GET'])
def search():

    min_population = int(request.args.get('popmin'))
    max_population = int(request.args.get('popmax'))
    min_gdp = int(request.args.get('gdpmin'))
    max_gdp = int(request.args.get('gdpmax'))
    language = request.args.get('languages')

    min_lifeExpectancy = int(request.args.get('lifemin'))
    max_lifeExpectancy = int(request.args.get('lifemax'))
    selected_continent = request.args.get('continent')

    # Call the function with the population range extracted from the query parameters
    (columns, search_result) = search_country(min_population, max_population, min_gdp, max_gdp, min_lifeExpectancy, max_lifeExpectancy, selected_continent, language)
    # Pass the search result to the template or perform other operations
    return render_template('search.html', columns=columns, search_result=search_result)


