from craigslist import CraigslistHousing
import settings
import sender


houses = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area='chc', category='apa', filters={'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE, 'bedrooms': 1})

results = houses.get_results(sort_by='newest', geotagged=True, limit=25)
apartments = []

def in_box(coords, box):
    if coords == None:
        return False
    if box[0][0] < coords[1] < box[1][0] and box[1][1] > coords[0] > box[0][1]:
        return True
    else:
        return False

for result in results:
    geotag = result["geotag"]
    if geotag is not None:
        for box in settings.BOXES.items():
            if in_box(geotag, box[1]):
                apartments.append(result)
                break

for apartment in apartments:
    sender.post_to_slack(apartment)
    print('**********************')
    print(apartment)
