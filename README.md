# JSON to iCalendar Converter

This script converts a JSON file containing event data into an iCalendar (.ics) file that can be imported into calendar applications like Google Calendar, Apple Calendar, Microsoft Outlook, etc.

## Getting Calendar Data from Axis

To get your calendar data:

1. Log in to your Axis Navitas account
2. Open this URL in your browser (change the date range as needed):
   ```
   https://axis.navitas.com/apps/timetable/timetable?start=2025-03-30T00%3A00%3A00&end=2025-05-11T00%3A00%3A00
   ```
3. Just copy the plain text results and put them in start.json

## Usage

```bash
python3 json_to_calendar.py [input_json_file] [output_ics_file]
```

### Arguments:
- `input_json_file` (optional): Path to the JSON file containing the calendar events. Defaults to `start.json` if not specified.
- `output_ics_file` (optional): Path where the output iCalendar file will be saved. Defaults to `calendar_events.ics` if not specified.

### Example:
```bash
python3 json_to_calendar.py start.json my_calendar.ics
```

## JSON Format

The input JSON file should be an array of event objects, each with the following properties:
- `title`: The event title
- `room`: Location of the event
- `start`: Start time in ISO 8601 format (e.g., "2025-02-24T10:45:00Z")
- `end`: End time in ISO 8601 format
- `bookingName`: (Optional) Additional booking information

## Importing the ICS File

After running the script, you can import the generated .ics file into your calendar application:

- **Google Calendar**: Go to Settings > Import & Export > Import
- **Apple Calendar**: File > Import
- **Microsoft Outlook**: File > Open & Export > Import/Export > Import an iCalendar (.ics) file

## Requirements

- Python 3.6 or higher
- Standard library modules: json, uuid, datetime, sys 