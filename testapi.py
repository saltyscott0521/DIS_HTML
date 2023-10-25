import requests


r = requests.get("https://data.wa.gov/api/views/f6w7-q2d2/rows.json?accessType=DOWNLOAD")
data = r.text
