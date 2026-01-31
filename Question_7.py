# NAME: HASSAN ADNAN
# UCID: 30217418


def convertTime(secondsSinceMidnight):
    if secondsSinceMidnight < 0 or secondsSinceMidnight >= 86400:
        return "Invalid input"

    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60

    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    if hours == 0:
        displayHour = 12
    elif hours > 12:
        displayHour = hours - 12
    else:
        displayHour = hours

    return f"{displayHour:02d}:{minutes:02d}:{seconds:02d} {period}"
