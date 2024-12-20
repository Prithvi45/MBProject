from datetime import datetime


'''
DUMMY_DATA = [
    {"id": 1, "name": "John Doe", "datetime": "2024-12-19T12:34:56"},
    {"id": 2, "name": "Jane Smith", "datetime": "2023-10-14T08:15:30"},
]
'''

DUMMY_DATA = [
        {"id":1,"10_min_std_deviation": 8, "time": 2.46, "datetime": "2024-12-19T12:34:56", "10_min_sampled_avg": 24.8},
        {"id":2,"10_min_std_deviation": 6, "time": 3.14, "datetime": "2024-12-19T12:45:32", "10_min_sampled_avg": 20.5},
        {"id":3,"10_min_std_deviation": 10, "time": 1.75, "datetime": "2024-12-19T13:12:01", "10_min_sampled_avg": 28.7},
        {"id":4,"10_min_std_deviation": 7, "time": 2.89, "datetime": "2024-12-19T13:25:15", "10_min_sampled_avg": 22.3},
        {"id":5,"10_min_std_deviation": 9, "time": 3.67, "datetime": "2024-12-19T13:45:20", "10_min_sampled_avg": 25.9},
        {"id":6,"10_min_std_deviation": 5, "time": 2.31, "datetime": "2024-12-19T14:02:48", "10_min_sampled_avg": 18.2},
        {"id":7,"10_min_std_deviation": 12, "time": 3.92, "datetime": "2024-12-19T14:30:50", "10_min_sampled_avg": 31.0},
        {"id":8,"10_min_std_deviation": 11, "time": 2.50, "datetime": "2024-12-19T14:45:12", "10_min_sampled_avg": 27.6},
        {"id":"9","10_min_std_deviation": 8, "time": 1.95, "datetime": "2024-12-19T15:10:43", "10_min_sampled_avg": 24.3},
        {"id":10,"10_min_std_deviation": 13, "time": 4.10, "datetime": "2024-12-19T15:30:28", "10_min_sampled_avg": 33.5}
]



# Transform `datetime` to `Date` column
for record in DUMMY_DATA:
    dt = datetime.strptime(record["datetime"], "%Y-%m-%dT%H:%M:%S")
    record["date"] = dt.strftime("%d-%B-%Y")  # Format: DD-Month-Year

