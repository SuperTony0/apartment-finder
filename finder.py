from craigslist import CraigslistHousing
from functions import in_box
from functions import posted_recently
import settings
import sender

print('Starting scrape...')
houses = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area='chc', category='apa', filters={'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE, 'bedrooms': 1})

results = houses.get_results(sort_by='newest', geotagged=True, limit=25)
apartments = []

for result in results:
    geotag = result["geotag"]
    if geotag is not None and posted_recently(result):
        for box in settings.BOXES.items():
            if in_box(geotag, box[1]):
                apartments.append(result)
                break

for apartment in apartments:
    sender.post_to_slack(apartment)
    print('**********************')
    print(apartment)
