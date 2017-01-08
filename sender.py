from slackclient import SlackClient
import private

SLACK_TOKEN = private.SLACK_TOKEN
SLACK_CHANNEL = "#tonys_apartment"

sc = SlackClient(SLACK_TOKEN)

def post_to_slack(listing):
    desc = "{0} | <{1}> ".format(listing["name"], listing["url"])
    sc.api_call(
        "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
        username='Craigslist Apartment Bot', icon_emoji=':house:'
    )
