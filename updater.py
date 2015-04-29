import requests

URL_UPDATE = "http://www.dgp.toronto.edu/~mccrae/projects/firebox/version.html"

check = requests.get(URL_UPDATE)
version_online = check.text

if version_online > "41.8":
    print "New Version out."
