#---Libraries---
import requests
import re
from bs4 import BeautifulSoup
from stock_screener_options import *

#---Scraper---
_SCREENER_URL_BASE = "https://finviz.com/screener.ashx?v=111&f=" # you can change the 111 to 121 or other values on the site, code is modular enough that you can feed it any one and it will adjust the data_header and data cols 

'''
build_url
@param options create a list of params (fs_exch.AMEX,...)
@param page_num offset the number of records found by some k

Builds URL by providing a list of options from the enums
'''
def build_url(options, page_num=0):
	#building the query params
	extension = ""
	for option in options:
		extension += str(option.__class__).split("'")[1] + option.name + "," # bit of a string hack
	extension = extension[:-1] #cleans up the string by trimming the final ','
	if page_num != 0 and page_num > 0:
		extension += "&r=" + str(page_num)
	return _SCREENER_URL_BASE + extension

'''
scrape_data_row
@param data_row the row BeautifulSoup object to do parsing on
'''
def scrape_data_row(data_row):
	data = []
	for col in data_row.find_all("td"):
		data.append(col.text)
	return data

'''
scrape
@param options the list of options built from enum values
@param page_num offset by 20
'''
def scrape(options, page_num=0):
	url = build_url(options, page_num)
	req = requests.get(url)
	#theoretically check for status code 200
	soup = BeautifulSoup(req.content) # theoretically include the best parser for a system
	total_found = soup.find("td",{"class":"count-text"}).text
	total_found = re.findall(r'\b\d+\b', total_found)[0] # regex to find only digits surrounded by spaces
	table = soup.find("table", {"width":"100%","border":"0","bgcolor":"#d3d3d3"})
	data_header = [td.text for td in table.find_all("tr", {"align":"center"})[0].find_all("td", {"class":"table-top"})]
	data_rows = table.find_all("tr")[1:]
	data = []
	for data_row in data_rows:
		data.append(scrape_data_row(data_row))

	return (total_found, data_header, data) #3-tuple contains our data



#---Main---
def main():
	print("Stock Screener Tests")

	#example use
	def example(opt  ions,page_num=0):
		x = scrape(options,page_num)
		print("Total Found: " + x[0])
		print(x[1])
		for line in x[2]:
			print(line)
	
	example([exch._nasd, earningsdate._nextdays5])
	example([exch._nasd, earningsdate._nextdays5], 21)


if __name__ == "__main__":
	main()