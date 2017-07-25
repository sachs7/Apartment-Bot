from scrape_craigslist import post_to_slack
import settings
import time

import sys
import traceback

if __name__ == "__main__":
    while True:
        print(f'{time.ctime()}: Starting scrape...')
        try:
            post_to_slack()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print(f'{time.ctime()}: Successfully finished scraping')
        time.sleep(settings.SLEEP_INTERVAL)
