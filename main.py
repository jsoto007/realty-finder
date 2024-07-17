import requests
import pprint
import csv

url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM opa_properties_public"

response = requests.get(url)

if response.status_code == 200:
  data = response.json()


  pp = pprint.PrettyPrinter(indent=4)
    
  pprint.pp(data)

file = open("scraped_quotess.csv", "w")

writer.csv.writer(file)

writer.writerow(["Hello", "Hello2"])


