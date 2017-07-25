import settings

POST_ONLY_UNIQUE_ID = set()


def slack_util(sc, result):
    """ Slack Client: sc """

    message = f'*Name:* {result["name"]} | *Posted at:* {result["datetime"]} | *Price:* {result["price"]} |' \
              f' *Near:* {result["where"]} | *Bedrooms:* {result["bedrooms"]} | *URL:* {result["url"]}'

    # print(POST_ONLY_UNIQUE_ID)

    if result['id'] not in POST_ONLY_UNIQUE_ID:

        sc.api_call(
            "chat.postMessage", channel=settings.SLACK_CHANNEL, text=message,
            username='pybot', icon_emoji=':robot_face:'
        )
        POST_ONLY_UNIQUE_ID.add(result['id'])
    # print(POST_ONLY_UNIQUE_ID)
