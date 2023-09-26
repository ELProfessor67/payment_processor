from datetime import datetime, timedelta

def get_last_7_months():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    current_date = datetime.now()
    result = []

    for i in range(7):
        month_index = (current_date.month - i - 1) % 12
        result.append(month_index+1)

    return result
