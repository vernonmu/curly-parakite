# Calendar Event Converter

This Python script converts calendar events from an ICS file to a CSV file, including only past and current day events. It calculates the duration of each event and provides a summary of the total hours spent on past events.

## Prerequisites

Before you can run this script, you need to have Python installed on your machine. Python 3.6 or later is recommended. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, this script requires the `icalendar` Python package. You can install this package via pip:

```
pip install icalendar
```

## Installation

1. **Download the script**: Clone or download the Python script to your local machine.
2. **Prepare your ICS file**: Ensure you have an ICS file ready with your calendar events. This file should be accessible by the script.

## Usage

To use the script, follow these steps:

1. **Locate your ICS file**: Place your `.ics` calendar file into the same directory as main.py

```
ics_file_path = './calendar.ics'
csv_file_path = './calendar-output.csv'
```

2. **Run the script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Execute the script by running:

```
python main.py
```

## Output

The script will output a CSV file at the specified location. The CSV file will contain the following columns:

- **Start Date**: The start date and time of the event.
- **End Date**: The end date and time of the event.
- **Summary**: A summary or title of the event.
- **Description**: Description of the event.
- **Location**: Location of the event.
- **Duration (Hours)**: Duration of the event in hours.

A final row will also be included in the CSV that summarizes the total hours of all events listed.

## Troubleshooting

If you encounter issues with running the script:

- Ensure all prerequisites are installed.
- Check the paths provided for the ICS and CSV files.
- Make sure the ICS file is properly formatted and accessible.

For more help, refer to the Python and icalendar documentation, or raise an issue in the repository where this script is hosted.

## License

Specify the license under which the script is released, which determines how it can be used by others.
