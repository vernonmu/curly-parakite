import csv
from icalendar import Calendar, Event
from datetime import datetime, date

def ics_to_csv(ics_file_path, csv_file_path):
    total_hours = 0 # Initialize total hours
    today = date.today()

    # Open the ICS file
    with open(ics_file_path, 'rb') as file:
        calendar = Calendar.from_ical(file.read())
    
    # Create CSV file and write headers
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Start Date', 'End Date', 'Summary', 'Description', 'Location', 'Duration (Hours)'])
        
        # Iterate over events in the calendar
        for component in calendar.walk():
            if component.name == "VEVENT":
                start_dt = component.get('dtstart').dt
                end_dt = component.get('dtend').dt
                summary = component.get('summary')
                description = component.get('description', '')
                location = component.get('location', '')

                 # Check if the event is past or on the current day
                if isinstance(start_dt, datetime):
                    event_date = start_dt.date()
                elif isinstance(start_dt, date):
                    event_date = start_dt
                else:
                    continue  # Skip this event if date is not properly defined


                # Convert dates to string if they are datetime objects
                if event_date <= today:
                  if isinstance(start_dt, datetime) and isinstance(end_dt, datetime):
                      duration = (end_dt - start_dt).total_seconds() / 3600  # Calculate duration in hours
                      total_hours += duration  # Accumulate total hours
                      start_dt = start_dt.strftime('%Y-%m-%d %H:%M:%S')
                      end_dt = end_dt.strftime('%Y-%m-%d %H:%M:%S')
                  else:
                      duration = 0  # In case of all-day events or invalid data

                # Write event data to CSV
                writer.writerow([start_dt, end_dt, summary, description, location, f"{duration:.2f}"])
        
        # Write total hours at the end of the CSV
        writer.writerow(['', '', '', 'Total Hours:', '', f"{total_hours:.2f}"])


# Usage
ics_file_path = './calendar.ics'
csv_file_path = './calendar-output.csv'
ics_to_csv(ics_file_path, csv_file_path)
