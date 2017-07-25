from craigslist import CraigslistHousing
from slackclient import SlackClient
from utilities import slack_util

import time

import settings


def scrape():
    ch = CraigslistHousing(site=settings.CRAIGSLIST_SITE, category=settings.CRAIGSLIST_HOUSING_SECTION,
                           filters={'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE,
                                    'min_bedrooms': settings.MIN_BEDROOM, 'max_bedrooms': settings.MAX_BEDROOM,
                                    'min_bathrooms': settings.MIN_BATHROOM, 'max_bathrooms': settings.MAX_BATHROOM
                                    })

    gen = ch.get_results(sort_by='newest', geotagged=True, limit=30)

    return [item for item in gen if item['where'] in settings.NEIGHBORHOODS]


def post_to_slack():

    # Create a slack client.
    sc = SlackClient(settings.SLACK_TOKEN)

    # Get all the results from craigslist.
    all_results = scrape()
    print(all_results)
    result_count = len(all_results)
    print(f'{time.ctime()}: Got {result_count} results')

    # Post each result to slack.
    for result in all_results:
        slack_util(sc, result)

