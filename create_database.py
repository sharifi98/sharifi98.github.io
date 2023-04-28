import sqlite3
import random
import string

# Open a connection to a new (blank) database file scholarships.db
conn = sqlite3.connect('scholarships.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

c.execute('''CREATE TABLE scholarships
             (id INTEGER PRIMARY KEY,
              name TEXT,
              opens TEXT,
              closes TEXT,
              max_age INTEGER,
              all_can_apply INTEGER,
              gender_requirement TEXT,
              exchange_studies TEXT,
              union_selector TEXT,
              school_selector TEXT,
              municipality_selector TEXT,
              thesis_selector TEXT,
              other_information TEXT)''')


# Define some random data for the scholarships
scholarship_data = {
    'all_can_apply': ['Yes', 'No'],
    'gender_requirement': ['Men', 'Women', 'None'],
    'exchange_studies': ['USA', 'UK', 'France', 'Germany', 'Italy', 'Spain', 'All', 'None'],
    'union_selector': ['LO', 'Lärarnas Riksförbund', 'Saco', 'TCO', 'None'],
    'school_selector': [
        'Lunds universitet',
        'Kungliga Tekniska Högskolan',
        'Göteborgs universitet',
        'Uppsala universitet',
        'Linköpings universitet',
        'None'
    ],
    'municipality_selector': [
        'Stockholm kommun',
        'Göteborgs stad',
        'Malmö stad',
        'Uppsala kommun',
        'Västerås stad',
        'None'
    ],
    'thesis_selector': [
        'IdroUsforskning',
        'Pension och sparande',
        'Miljöteknik',
        'Medicinsk forskning',
        'None'
    ],
}

names = ['John Doe Scholarship', 'Jane Smith Scholarship', 'Bob Johnson Scholarship', 'Alice Wong Scholarship', 'Samuel Lee Scholarship', 'Karen Kim Scholarship', 'David Hernandez Scholarship', 'Megan Brown Scholarship', 'Nathan Davis Scholarship', 'Laura Rodriguez Scholarship', 'Steven Nguyen Scholarship', 'Olivia Wilson Scholarship', 'William Thompson Scholarship',
         'Emily Moore Scholarship', 'Daniel Lee Scholarship', 'Avery Martin Scholarship', 'Sophia Anderson Scholarship', 'Josephine Wright Scholarship', 'Jacob Wilson Scholarship', 'Liam Perez Scholarship', 'Evelyn Gonzalez Scholarship', 'Ethan Hernandez Scholarship', 'Mia Lee Scholarship', 'Alexander Davis Scholarship', 'Charlotte White Scholarship']

# This code generates 25 random scholarship entries and inserts them into a SQLite database.
# The for loop iterates 25 times and generates random values for each scholarship attribute using the random and string modules.
# The values are then used to execute an SQL INSERT command that adds the scholarship to the database.
for i in range(25):
    name = random.choice(names)
    opens = f'{random.randint(1, 12)}/{random.randint(1, 28)}/2023'
    closes = f'{random.randint(1, 12)}/{random.randint(1, 28)}/2023'
    max_age = random.randint(18, 65)
    all_can_apply = 1 if random.choice(
        scholarship_data['all_can_apply']) == 'Yes' else 0
    gender_requirement = random.choice(scholarship_data['gender_requirement'])
    exchange_studies = random.choice(scholarship_data['exchange_studies'])
    union_selector = random.choice(scholarship_data['union_selector'])
    school_selector = random.choice(scholarship_data['school_selector'])
    municipality_selector = random.choice(
        scholarship_data['municipality_selector'])
    thesis_selector = random.choice(scholarship_data['thesis_selector'])
    other_information = ''.join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase + ' ', k=100))

    c.execute('''INSERT INTO scholarships
                 (name, opens, closes, max_age, all_can_apply,
                  gender_requirement, exchange_studies, union_selector,
                  school_selector, municipality_selector, thesis_selector,
                  other_information)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (name, opens, closes, max_age, all_can_apply,
               gender_requirement, exchange_studies, union_selector,
               school_selector, municipality_selector, thesis_selector,
               other_information))


# Commit the changes to the database
conn.commit()
