# This lib does the http fetching
import urllib.request
# So we can understand json
import json

# Define the API endpoint
elife = "https://api.elifesciences.org/"


#load the json
## This will do a 500 error. I've tried encoding the URL params and tried without
## The brackets around the subject, but I can't find any way that works.
contents = urllib.request.urlopen(elife + "search?for=install&subject[]=computational-systems-biology&per-page=100").read()

# convert the response from a byte array to a string
contents = contents.decode("utf-8")
#string into json
contents = json.loads(contents)

for k,v in enumerate(contents["items"]):
    print(v[title])
    print("===" + v["impactStatement"])
