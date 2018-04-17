#!/usr/env/bin python
import re
import sys
import optparse
import urllib2
from bs4 import BeautifulSoup

#https://www.ikea.com/gb/en/products/

def get_data(url):
	page = BeautifulSoup(urllib2.urlopen(url), 'html.parser')
	return page

def get_all_products():
	page = get_data("https://www.ikea.com/gb/en/products/")
	#print(page)
	product_sections = page.findAll("li", {"class":"LandingPage-List--item LandingPage-List--item__divider"})
	#print(type(product_sections[0]))
	for product_type in product_sections:
		#<h5><a href="/gb/en/products/lighting/">Lighting</a></h5>
		line = product_type.findAll("h5")[0]
		link = re.findall(r'(?<=<h5><a href=\").*(?=\">)', str(line))[0]
		print(link)

get_all_products()