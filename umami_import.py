import csv

# User enter filename and new website id
original_csv_file = input("Please enter the filename of the original CSV file path: ")
new_website_id = input("Please enter the new website ID: ")

# Open the original CSV file
with open(original_csv_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Update the website_id column with the user-provided website ID
for row in data:
    row['website_id'] = new_website_id

# Define the columns required for the website_event table
website_event_columns = [
    'event_id', 'website_id', 'session_id', 'created_at', 'url_path',
    'url_query', 'referrer_path', 'referrer_query', 'referrer_domain',
    'page_title', 'event_type', 'event_name', 'visit_id'
]

# Write the website_event data to a new CSV file
with open('website_event.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=website_event_columns)
    writer.writeheader()
    for row in data:
        writer.writerow({key: row[key] for key in website_event_columns if key in row})

# Define the columns required for the session table
session_columns = [
    'session_id', 'website_id', 'hostname', 'browser', 'os', 'device',
    'screen', 'language', 'country', 'subdivision1', 'subdivision2',
    'city', 'created_at'
]

# Write the session data to a new CSV file
with open('session.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=session_columns)
    writer.writeheader()
    for row in data:
        writer.writerow({key: row[key] for key in session_columns if key in row})

print("Successfully generated website_event.csv and session.csv")
