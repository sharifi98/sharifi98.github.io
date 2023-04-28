Scholarship Database Web Application

This is a Python web application that provides a user-friendly interface for filtering, querying, and wrangling a scholarships database. The application consists of three files:

    app.py: This file contains the Flask application that serves the web pages and handles user requests. It defines two routes: / (the home page) and /filter (the page that shows the filtered results).
    create_scholarship_database.py: This file creates the SQLite database that contains the scholarship data. It also populates the database with a set of randomly generated data.
    index.html: This file defines the HTML structure of the web pages that the Flask application serves. It contains a form for users to filter the scholarship data, as well as a table that displays the filtered results.

Instructions:
    Read the installation.md file to get and install the required software then follow the steps below.

    Download the code and save it in a folder on your system.

    Open a terminal or command prompt and navigate to the folder where the code is saved.

    Run the following command to execute create_scholarship_database.py:

'python create_scholarship_database.py' or 'python3 create_scholarship_database.py'

This will create a new SQLite database file called scholarships.db in the same folder as the code file.

Run the following command to start the Flask web app:

    'python app.py' or 'python3 app.py'

    Open your browser and navigate to http://localhost:5001/.

    You should now see the homepage of the web app.

    Use the dropdown menus to filter scholarships based on your criteria.

    Click on the "Filter" button to see the results.

    To clear the filters and start over, you can clear all the dropdown menus or refresh the page.

Additional Notes:

    If you want to modify the scholarship data or add more scholarships to the database, you can edit the create_scholarship_database.py file accordingly.
    The scholarship names are randomly generated using a list of predefined names. If you want to use your own names, you can modify the names list in the create_scholarship_database.py file.
    The other_information attribute is generated using the string.ascii_uppercase, string.digits, string.ascii_lowercase, and ' ' (space) characters. If you want to generate different types of data for this attribute, you can modify the k value in the create_scholarship_database.py file.
    The app is currently set to run in debug mode, which provides additional information and error messages. In a production environment, you should set debug=False in the app.run() function.

Missing Functionality:

There are two key missing functionalities in this project:

    Join Query: A join query was not used in this project to retrieve data from multiple tables. Instead, all the scholarship data is stored in a single table, and the filtering is done using a single SQL query. In the future, implementing a join query to retrieve data from multiple tables would allow for more complex scholarship data to be stored and filtered.
    Separate Reset Button: Although the filtering form includes individual dropdown menus to reset. However, users can still reset the filters by pressing the filter button