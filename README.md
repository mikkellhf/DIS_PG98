# Country Query Project: DIS_Project
## Usage
The DIS_Project is a website running Python and Flask library.
The schema of the database is countries and certain fact about countries.

    git repository:  https://github.com/mikkellhf/DIS_PG98

There are five different parameters that can be used to filter the search results. 
The language parameter works as regex. Any official language that matches the start of an language input (regardless of capalization), will be shown. ie Denmark shows up having dA/DA/da/Da as the language input. The rest of the parameters are self explanatory. 

The results that are shown are handpicked catagories from the different data sets, meant to display the most interesting information regarding countries. 

## Requirements:
Run the code below to install the necessary modules.

    pip install -r requirements.txt

#### notes
This has only been run using Windows, and using the python method to run the application. 

## Running
1. set the database in __init__.py file.
2. 

    python3 run.py

### Debug
Run the following command, to get the webapp in debug mode. 

    python3 run_debug.py
