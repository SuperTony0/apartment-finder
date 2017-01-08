import time
import settings

while True:
    execfile('finder.py')
    time.sleep(settings.SLEEP_INTERVAL)
