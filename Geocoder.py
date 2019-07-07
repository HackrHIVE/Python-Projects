'''
Before running this script please install googlemaps library
--> pip install googlemaps
'''

import googlemaps as gm

gmaps_key = gm.Client(key='AIzaSyBh7KtLf7ZRYQfY7curj8BAbZpVHgKXLi8')

address = input('Enter address please : ')

geocoder_res = gmaps_key.geocode(address)
try:
    lat = geocoder_res[0]['geometry']['location']['lat']
    lon = geocoder_res[0]['geometry']['location']['lng']
except:
    lat = None
    lon = None

print('Geocoded result for address : {} is --> {},{}'.format(address,lat,lon))

'''
Reference --> Google Developers (https://developers.google.com/)
'''
