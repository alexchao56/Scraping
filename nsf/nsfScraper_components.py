from bs4 import BeautifulSoup
from progress.bar import Bar
from soupselect import select
import csv
import os
import re
import sys

# Get all the files from the current directory
allFiles = os.listdir(".")
bar = Bar('Processing', max=len(allFiles))

#Returns whether or not a string contains any numbers
def contain_numbers(s):
	return bool(re.match(".*\\d.*", s))

def get_data(currentSoup, tag, attributes):
	return currentSoup.find_all(tag, attributes)

products = []
colnames = []

trade_designation_attr = {
	'align': 'left',
    'valign': 'top',
    'width': '45%'
}

water_contact_size_restriction_attr = {
	'align': 'left',
	'valign': 'top',
	'width': '35%'
}

water_contact_temp_attr = {
	'align': 'left',
	'valign': 'top',
	'width': '20%'
}

water_contract_material_attr = {
	'align': 'left',
	'valign': 'top',
	'width': '20%'
}

company_attr = {
	'size': '+2'
}


facility_attr = {
	'size': '+1'
}

products = {}
products['Trade Designation'] = []
products['Water Contact Size Restriction'] = []
products['Water Contact Temp'] = []
products['Water Contact Material'] = []
products['Company'] = []
products['Facilities'] = []
products['Certification'] = []
product_count_list = []
facility_count_list = []

for i in range(len(allFiles)):

	with open(allFiles[i], 'r') as f:

		html = f.read()

		soup = BeautifulSoup(html)

		trade_links = get_data(soup, 'td', trade_designation_attr)
		water_contact_size = get_data(soup, 'td', water_contact_size_restriction_attr)
		water_contact_temp = get_data(soup, 'td', water_contact_temp_attr)
		water_contract_material = get_data(soup, 'td', water_contract_material_atr)
		company_links = get_data(soup, 'font', company_attr)
		facility_links = get_data(soup, 'font', facility_attr)
		facility_count_list.append(len(facility_links))

		company_count = 0

		for link in trade_links:
			text = link.get_text()
			if text not in products.keys():
				products['Trade Designation'].append(text)
				company_count += 1

		product_count_list.append(company_count)
		for link in product_function_links:
			text = link.get_text()
			if text not in products.keys():
				products['Water Contact Temp'].append(text)

		for link in max_use_links:
			text = link.get_text()
			if text not in products.keys():
				products['Max Use'].append(text)

		for link in company_links:
			text = link.get_text()
			for _ in range(company_count):
				if text not in products.keys():
					products['Company'].append(text)

		for link in facility_links:
			text = link.get_text()
			products['Facilities'].append(text)

		for link in facility_links:
			text = link.get_text()
			products['Facilities'].append(text)
		for _ in range(company_count):
			products['Certification'].append('NSF/ANSI 61')

  		bar.next()
bar.finish()

print " "

print "Trade Designation: " + str(len(products['Trade Designation']))
print "Product Function: " + str(len(products['Product Function']))
print "Max Use: " + str(len(products['Max Use']))
print "Company: " + str(len(products['Company']))
print "Facility: " + str(len(products['Facilities']))

########## WRITING TO CSV ##############

f = csv.writer(open("../data/chemicals.csv", "w"))
f.writerow(["Trade Designation", "Product Function", "Max Use", "Company", "Facility", "Certification"])    # Write column headers as the first line
for i in range(len(products['Trade Designation'])):
	trade = products['Trade Designation'][i].encode('utf-8')
	funct = products['Product Function'][i].encode('utf-8')
	maxUse = products['Max Use'][i].encode('utf-8')
	company = products['Company'][i].encode('utf-8')
	if i < len(products['Facilities']):
		facilities = products['Facilities'][i].encode('utf-8')
	else:
		facilities = 'N/A'
	certification = products['Certification'][i].encode('utf-8')
	f.writerow([trade,funct,maxUse,company,facilities, certification])
	writingBar.next()
writingBar.finish()