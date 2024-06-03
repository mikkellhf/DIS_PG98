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
This has only been run using Windows, and done using python to run the application. 

## Running
1. set the database in __init__.py file.
2. Run the following command to run the web application

    python3 run.py

### Debug
Run the following command, to get the webapp in debug mode. 

    python3 run_debug.py


# Potential problems
If the following error is shown:

"C:\path\DIS_PG98>python3 run.py


Error executing SQL file C:\path\DIS_PG98\DIS_Project\schema_ins.sql: could not open file "C:\path\DIS_PG98\DIS_Project\Data_Sets\health.csv" for reading: Permission denied


HINT:  COPY FROM instructs the PostgreSQL server process to read a file. You may want a client-side facility such as psql's \copy." 
## Guide
Please confer to the following guide:
1. Right-click the file or folder you want to set permissions for and select "Properties". This should be the folder Data_Sets or the individual files within the folder. 
2. Navigate to the "Security" tab.
3. Click on the "Edit" button to change permissions.
4. In the permissions window, click the "Add" button. In lowest text box, write "Everyone" or "Alle" and press enter. This should pop-up another window, where you select the "Everyone"/"Alle". Then, check the boxes in the "Permissions for [username]" section to grant or deny specific permissions (like "Read", "Write", etc.).
5. Click "OK" to apply the changes.

   
The issue should now have been fixed, and the command should run the webapp flawlessly. 
Futher reading: https://kb.uwec.edu/articles/drives-establishing-windows-file-and-folder-level-permissions
