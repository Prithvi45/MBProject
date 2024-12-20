from datetime import datetime, timedelta
from django.conf import settings


#Task 3.3
def get_expiry_details(request, data_expiry_hours=24):

    session_expiry = request.session.get_expiry_age()

    data_expiry = (datetime.now() + timedelta(hours=data_expiry_hours)).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "session_expiry": session_expiry,
        "data_expiry": data_expiry
    }

