import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 750

# The maximum rent you want to pay per month.
MAX_PRICE = 1200

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'chicago'

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "wicker-park": [
        [-87.68815,41.902788],
        [-87.666864,41.925398]
    ],
    "noble": [
        [-87.677293,41.894898],
        [-87.656093,41.911124]
    ],
    "chicago-ave": [
        [-87.687979,41.89295],
        [-87.650642,41.899594]
    ],
    "logan": [
        [-87.711539,41.917256],
        [-87.68652,41.931497]
    ],
    "bucktown": [
        [-87.697978,41.910038],
        [-87.669654,41.925334]
    ],
    "brown-line": [
        [-87.672873,41.932103],
        [-87.64854,41.945032]
    ],
    "chicago": [
        [-87.95517,41.640078],
        [-87.511597,42.026854]
    ]
}


## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 30 * 60 # 30 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
