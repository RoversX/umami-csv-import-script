import pandas as pd

# User enter filename and new website id
original_csv_file = input("Please enter the filename of the original CSV file path: ")
new_website_id = input("Please enter the new website ID: ")

# Load the original CSV file
df = pd.read_csv(original_csv_file)

# Update the website_id column with the user-provided website ID
df['website_id'] = new_website_id

# Define the columns required for the website_event table
website_event_columns = [
    'event_id', 'website_id', 'session_id', 'created_at', 'url_path',
    'url_query', 'referrer_path', 'referrer_query', 'referrer_domain',
    'page_title', 'event_type', 'event_name', 'visit_id'
]

# Create a new DataFrame for the website_event data with the required columns
df_website_event = df[website_event_columns]

# Save the new website_event data to a CSV file
df_website_event.to_csv('website_event.csv', index=False)

# Define the columns required for the session table
session_columns = [
    'session_id', 'website_id', 'hostname', 'browser', 'os', 'device',
    'screen', 'language', 'country', 'subdivision1', 'subdivision2',
    'city', 'created_at'
]

# Create a new DataFrame for the session data with the required columns
df_session = df[session_columns]

# Save the new session data to a CSV file
df_session.to_csv('session.csv', index=False)

print("Successfully generated website_event.csv and session.csv")
