from datetime import datetime

DUMMY_DATA = [
    {"id": 1, "name": "John Doe", "datetime": "2024-12-19T12:34:56"},
    {"id": 2, "name": "Jane Smith", "datetime": "2023-10-14T08:15:30"},
]

# Transform `datetime` to `Date` column
for record in DUMMY_DATA:
    dt = datetime.strptime(record["datetime"], "%Y-%m-%dT%H:%M:%S")
    record["date"] = dt.strftime("%d-%B-%Y")  # Format: DD-Month-Year

