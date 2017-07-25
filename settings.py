MIN_PRICE = 3000

MAX_PRICE = 4000

MIN_BEDROOM = 4

MAX_BEDROOM = 4

MIN_BATHROOM = 2

MAX_BATHROOM = 4

# Craigslist site to be searched on.
# Example: https://sfbay.craigslist.org
CRAIGSLIST_SITE = 'sfbay'

# Craigslist section to search for: apa (apartment)
CRAIGSLIST_HOUSING_SECTION = 'apa'

''' Area to search house for: South Bay Area '''
AREAS = 'sby'

NEIGHBORHOODS = ['mountain view', 'santa clara', 'sunnyvale', 'milpitas']

# Send Slack message for every 20 minutes
SLEEP_INTERVAL = 20 * 60

SLACK_CHANNEL = '#housing'

try:
    from private import *
    TOKEN_FOR_SLACK = SLACK_TOKEN
except Exception:
    pass

