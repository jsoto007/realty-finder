import requests
import pprint
import csv
import datetime
import atexit
import re
import time
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller

from selenium import webdriver

driver = webdriver.Firefox()



print("####****Please Enter the Zip-Code****####")
print("############********############")
print("############********############")
print("####****only numbers no spaces****####")
print("############********############")
print("############********############")

zip = input("")
print("Zip-code entered:", zip)


current_time = datetime.datetime.now()


day = current_time.day
month = current_time.month
year = current_time.year

url = f"https://phl.carto.com/api/v2/sql?q=SELECT * FROM opa_properties_public WHERE zip_code = '{zip}' LIMIT 5"


response = requests.get(url)


if response.status_code == 200:
  data = response.json()


    

  pp = pprint.PrettyPrinter(indent=4)

  pprint.pp(data)

# Get the tax balance from the website.
def gets_tax_balance():
  
  
  keyboard = Controller()
  time.sleep(5)
  for row in data['rows']:
      stree_name = (row['mailing_street'])
      driver.get("https://www.phila.gov/revenue/realestatetax/")

      time.sleep(5)

      search_bar = driver.find_element("xpath", 
                                "//input[contains(@id, 'Dc-c')]")
      search_bar.click()
      keyboard.type(f"{stree_name}")
      keyboard.press(Key.enter)
      keyboard.release(Key.enter)
      time.sleep(2)
      opa_number = driver.find_element("xpath",
                                       "//a[contains(@id, 'l_Dc-l-1')]")
      
      opa_number.click()

      time.sleep(2)

      balance = driver.find_element("xpath",
                                    "//span[contains(@id, 'fgvt_Dc-d')]")
      t_balance = balance.get_attribute('text')

      time.sleep(1)
      row["Taxed_Balance"] = f"{t_balance}"



gets_tax_balance()

fields = ["objectid",	"assessment_date",	"basements",	"beginning_point",	"book_and_page",	"building_code",	"building_code_description",	"category_code",	"category_code_description",	"census_tract",	"central_air",	"cross_reference",	"date_exterior_condition", "depth",	"exempt_building",	"exempt_land",	"exterior_condition",	"fireplaces",	"frontage",	"fuel",	"garage_spaces",	"garage_type",	"general_construction",	"geographic_ward",	"homestead_exemption",	"house_extension",	"house_number",	"interior_condition",	"location",	"mailing_address_1",	"mailing_address_2",	"mailing_care_of",	"mailing_city_state",	"mailing_street",	"mailing_zip"	"market_value",	"market_value_date",	"number_of_bathrooms",	"number_of_bedrooms",	"number_of_rooms",	"number_stories",	"off_street_open",	"other_building",	"owner_1",	"owner_2",	"parcel_number",	"parcel_shape",	"quality_grade",	"recording_date",	"registry_number",	"sale_date",	"sale_price",	"separate_utilities",	"sewer",	"site_type",	"state_code",	"street_code",	"street_designation",	"street_direction",	"street_name",	"suffix",	"taxable_building",	"taxable_land",	"topography",	"total_area",	"total_livable_area",	"type_heater",	"unfinished",	"unit",	"utility",	"view_type",	"year_built"	"year_built_estimate",	"zip_code",	"zoning",	"pin",	"building_code_new"	"building_code_description_new",	"shape", "time", "rows", "fields", "total_rows", 'building_code_new', 'the_geom', 'mailing_zip', 'market_value', 'the_geom_webmercator', 'year_built', 'cartodb_id', 'year_built_estimate', 'building_code_description_new', 'Taxed_Balance']


rows = data['rows']

# Specify the CSV file name
csv_file = f"Housing Zip-Code {zip} {month},{day},{year}.csv"

# Writing to csv file
with open(csv_file, 'w', newline='') as csvfile:
    # Create a writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # Write the header
    writer.writeheader()

    # Write the data
    for row in rows:
        writer.writerow(row)

print(f"Data successfully written to {csv_file}")


print("888888888888888888888888888888888888888")

# for row in data['rows']:
#     print(row['mailing_street'])




