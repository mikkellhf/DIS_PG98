from DIS_Project import conn

def search_country(min_population, max_population, min_gdp, max_gdp, min_lifeExpectancy, max_lifeExpectancy, selected_continent, language):
    columns_health = "Country, LifeExpectancy, FertilityRate, Population"
    columns_gdp = "Country, gdp"
    columns_continent = "Country, Continent"
    columns_langauge = "Country, Official_language"

    columns = columns_health + ", " + columns_gdp.split(",")[1]
    columns += ", " + columns_langauge.split(",")[1]

    print(language)
    cur = conn.cursor()

    # SQL query for filtering based on population and life expectancy
    sql_query_population_life = f"""
    SELECT {columns_health} 
    FROM countries_health 
    WHERE Population >= %s AND Population <= %s 
    AND LifeExpectancy >= %s AND LifeExpectancy <= %s
    """ % (min_population, max_population, min_lifeExpectancy, max_lifeExpectancy)

    # SQL query for filtering based on GDP
    sql_query_gdp = f"""
    SELECT {columns_gdp} 
    FROM countries_gdp 
    WHERE gdp >= %s AND gdp <= %s
    """ % (min_gdp, max_gdp)

    
    if language == None: 
        language = '' 
    language = language.split(",")
    
    #Loop through the langauges to make the first letter big and the rest small
    for i in range(len(language)):
        language[i] = language[i].capitalize()
    
    sql_query_language = f"""
        (SELECT {columns_langauge} 
        FROM countries_language 
        WHERE Official_language LIKE '{language[0]}%' 
        """
    for i in range(1, len(language)):
        sql_query_language += f" OR Official_language LIKE '{language[i]}%'"
    sql_query_language += ")"
    # Construct the final SQL query based on selected continent

    sql_final_query = f"""
    SELECT DISTINCT {columns} 
    FROM ({sql_query_gdp}) 
    NATURAL JOIN ({sql_query_population_life})
    NATURAL JOIN {sql_query_language}
    """

    # We need to check if a continent is selected
    # If so we need to join with the countries table to get the continent
    if selected_continent != "All Continents":
        
        sql_query_continents = f"""
        (SELECT {columns_continent} 
        FROM countries_continent 
        WHERE Continent = '{selected_continent}')
        """
        sql_final_query += f"NATURAL JOIN {sql_query_continents}"



    # Sort the results by country name
    sql_final_query += " ORDER BY Country ASC"

    # Execute the final query with continent parameter
    cur.execute(sql_final_query)
    result = cur.fetchall()
    cur.close()
    
    return (columns, result)
