from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
db = "dbname='postgres' user='postgres' host='127.0.0.1' password = 'Stg22dqa'"
conn = psycopg2.connect(db)
bcrypt = Bcrypt(app)

# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'
from DIS_Project.Search.routes import Search
app.register_blueprint(Search)


def execute_sql_file(filename, Data_Sets = None):
    """Execute a .sql file containing multiple SQL statements."""
    #Get the absolute path of the current file and then append the filename to it
    path = os.getcwd()
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
    with open(filename, 'r') as file:
        sql_commands = file.read()
    #Get the absolute path of the current file and then append the the names of the data sets to it
    #This was an issue, and has been fixed by slighty hardcoding a solution. 
    for i in range(len(Data_Sets)):
        Data_sets[i] =  path+'\\DIS_Project\\Data_Sets\\'+Data_sets[i]
    cur = conn.cursor()
    try:
        cur.execute(sql_commands,tuple(Data_sets))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error executing SQL file {filename}: {e}")
    finally:
        cur.close()
Data_sets = ['health.csv', 'gdp.csv', 'continents.csv', 'language.csv']
execute_sql_file('schema_ins.sql', Data_sets)
