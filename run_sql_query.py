import os
import sys
import django
from django.db import connection

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ec.settings")  # Replace with your project's settings module
django.setup()

# Check if a SQL query is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python run_sql_script.py 'your_sql_query';")
    sys.exit(1)

# Get the SQL query from the command line arguments
sql_query = sys.argv[1]

with connection.cursor() as cursor:
    cursor.execute(sql_query)
    results = cursor.fetchall()

# Process and print the results
for row in results:
    print(row)
