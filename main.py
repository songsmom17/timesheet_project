import csv
from datetime import datetime

class WorkLogEntry:
    def __init__(self, date, start_time, end_time, miles_driven):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.miles_driven = miles_driven

    def total_work_hours(self):
        start = datetime.strptime(self.start_time, '%H:%M')
        end = datetime.strptime(self.end_time, '%H:%M')
        return (end - start).seconds / 3600  # Convert seconds to hours

def log_arrival():
    date = datetime.now().strftime('%Y-%m-%d')
    start_time = datetime.now().strftime('%H:%M')
    return date, start_time

def log_departure_and_miles():
    end_time = datetime.now().strftime('%H:%M')
    miles_driven = float(input("Enter miles driven: "))
    return end_time, miles_driven

def save_log(entry, filename='timesheet.csv'):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Start Time', 'End Time', 'Total Hours', 'Miles Driven']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({
            'Date': entry.date,
            'Start Time': entry.start_time,
            'End Time': entry.end_time,
            'Total Hours': entry.total_work_hours(),
            'Miles Driven': entry.miles_driven
        })

# Main process
print("Logging arrival time...")
date, start_time = log_arrival()
print(f"Arrived at {start_time} on {date}.")

input("Press Enter when you leave to log departure and miles driven...")

print("Logging departure time and miles driven...")
end_time, miles_driven = log_departure_and_miles()
entry = WorkLogEntry(date, start_time, end_time, miles_driven)
save_log(entry)

print(f"Log saved for {date}. Total Hours: {entry.total_work_hours()} hours, Miles Driven: {entry.miles_driven} miles.")