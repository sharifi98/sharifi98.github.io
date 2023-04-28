# Import the necessary modules for the Flask web app, SQLite database, and templating.
from flask import Flask, render_template, request
import sqlite3

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage


@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('scholarships.db')
    c = conn.cursor()
    # Execute a SELECT statement to retrieve all the scholarship data from the database
    c.execute('SELECT * FROM scholarships')
    # Fetch all the results from the SELECT statement and store them in a variable
    data = c.fetchall()
    # Close the database connection
    conn.close()

    # Define the scholarship data for the dropdown menus
    scholarship_data = {
        'all_can_apply': ['Yes', 'No'],
        'gender_requirement': ['Men', 'Women', 'None'],
        'exchange_studies': ['USA', 'UK', 'France', 'Germany', 'Italy', 'Spain', 'All', 'None'],
        'union_selector': ['LO', 'Lärarnas Riksförbund', 'Saco', 'TCO', 'None'],
        'school_selector': ['Lunds universitet', 'Kungliga Tekniska Högskolan', 'Göteborgs universitet', 'Uppsala universitet', 'Linköpings universitet', 'None'],
        'municipality_selector': ['Stockholm kommun', 'Göteborgs stad', 'Malmö stad', 'Uppsala kommun', 'Västerås stad', 'None'],
        'thesis_selector': ['IdroUsforskning', 'Pension och sparande', 'Miljöteknik', 'Medicinsk forskning', 'None']
    }

    # Render the index.html template and pass the scholarship data and dropdown menu data to it
    return render_template('index.html', data=data, scholarship_data=scholarship_data)


# Define the route for filtering scholarships
@app.route('/filter', methods=['POST'])
def filter():
    # Connect to the SQLite database
    conn = sqlite3.connect('scholarships.db')
    c = conn.cursor()
    # Start building the SQL query for filtering scholarships
    query = 'SELECT * FROM scholarships WHERE 1=1'
    # Initialize an empty list to store query parameters
    params = []

    # Check if each form field has a value, and if so, add the corresponding condition to the query
    if request.form['all_can_apply']:
        query += ' AND all_can_apply = ?'
        params.append(request.form['all_can_apply'])

    if request.form['gender_requirement']:
        query += ' AND gender_requirement = ?'
        params.append(request.form['gender_requirement'])

    if request.form['exchange_studies']:
        query += ' AND exchange_studies = ?'
        params.append(request.form['exchange_studies'])

    if request.form['union_selector']:
        query += ' AND union_selector = ?'
        params.append(request.form['union_selector'])

    if request.form['school_selector']:
        query += ' AND school_selector = ?'
        params.append(request.form['school_selector'])

    if request.form['municipality_selector']:
        query += ' AND municipality_selector = ?'
        params.append(request.form['municipality_selector'])

    if request.form['thesis_selector']:
        query += ' AND thesis_selector = ?'
        params.append(request.form['thesis_selector'])

    # Execute the query with the provided parameters
    c.execute(query, params)
    # Fetch all the results from the query
    data = c.fetchall()

    scholarship_data = {
        'all_can_apply': ['Yes', 'No'],
        'gender_requirement': ['Men', 'Women', 'None'],
        'exchange_studies': ['USA', 'UK', 'France', 'Germany', 'Italy', 'Spain', 'All', 'None'],
        'union_selector': ['LO', 'Lärarnas Riksförbund', 'Saco', 'TCO', 'None'],
        'school_selector': ['Lunds universitet', 'Kungliga Tekniska Högskolan', 'Göteborgs universitet', 'Uppsala universitet', 'Linköpings universitet', 'None'],
        'municipality_selector': ['Stockholm kommun', 'Göteborgs stad', 'Malmö stad', 'Uppsala kommun', 'Västerås stad', 'None'],
        'thesis_selector': ['IdroUsforskning', 'Pension och sparande', 'Miljöteknik', 'Medicinsk forskning', 'None']
    }

    # Close the database connection
    conn.close()

    return render_template('index.html', data=data, scholarship_data=scholarship_data)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
