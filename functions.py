import datetime
import settings
from datetime import timedelta

def in_box(coords, box):
    if coords == None:
        return False
    if box[0][0] < coords[1] < box[1][0] and box[1][1] > coords[0] > box[0][1]:
        return True
    else:
        return False

def posted_recently(apartment):
    altered_time = unicode(datetime.datetime.now() - timedelta(seconds=(settings.SLEEP_INTERVAL+300)))
    current_time = unicode(datetime.datetime.now())
    result = (altered_time < apartment['datetime'])
    return result
