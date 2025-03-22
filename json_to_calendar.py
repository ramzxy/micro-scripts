#!/usr/bin/env python3
import json
import uuid
from datetime import datetime, timedelta
import sys

def json_to_ics(json_file, output_file):
    # Load the JSON data
    with open(json_file, 'r') as f:
        events = json.load(f)
    
    # Create the iCalendar file content
    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Calendar Events//NONSGML v1.0//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]
    
    for event in events:
        # Get event details
        title = event.get('title', '').replace('\n', ' - ')
        room = event.get('room', '')
        start_time = event.get('start', '')
        end_time = event.get('end', '')
        booking_name = event.get('bookingName', '')
        
        # Create unique ID for the event
        event_id = str(uuid.uuid4())
        
        # Parse start and end times
        try:
            start_dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            end_dt = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
            
            # Shift times back by 1 hour to compensate for calendar app behavior
            start_dt = start_dt - timedelta(hours=1)
            end_dt = end_dt - timedelta(hours=1)
            
            # Format times for iCalendar
            start_str = start_dt.strftime("%Y%m%dT%H%M%SZ")
            end_str = end_dt.strftime("%Y%m%dT%H%M%SZ")
            
            # Create description with additional information
            description = f"Room: {room}"
            if booking_name:
                description += f"\nBooking: {booking_name}"
            
            # Add event to calendar
            ics_content.extend([
                "BEGIN:VEVENT",
                f"UID:{event_id}",
                f"SUMMARY:{title}",
                f"LOCATION:{room}",
                f"DESCRIPTION:{description}",
                f"DTSTART:{start_str}",
                f"DTEND:{end_str}",
                "END:VEVENT"
            ])
        except ValueError as e:
            print(f"Error processing event: {title}. Error: {e}")
    
    # End calendar
    ics_content.append("END:VCALENDAR")
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write('\n'.join(ics_content))
    
    print(f"Calendar file successfully created at {output_file}")
    print("Note: All event times have been shifted back by 1 hour to compensate for calendar import behavior.")

if __name__ == "__main__":
    # Check if file names are provided as arguments
    if len(sys.argv) > 2:
        json_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        # Default file names
        json_file = "start.json"
        output_file = "calendar_events.ics"
    
    json_to_ics(json_file, output_file) 