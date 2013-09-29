import requests
import pprint
from geopy import geocoders
import json
g = geocoders.GoogleV3()
pp = pprint.PrettyPrinter(indent=4)
address = raw_input('Enter the address: ')
place, (lat, lng) = g.geocode(address)
print "%s: %.5f, %.5f" % (place, lat, lng)
url = "http://api.nytimes.com/svc/semantic/v2/geocodes/query.json?nearby=%s,%s&api-key=04e6236f0ac7eb2e6e57528dbb5dec8f:14:68190350" %(lat,lng)

response = requests.get(url)
data = json.loads(response.text)
pp.pprint(data)



