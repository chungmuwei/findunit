import requests
from bs4 import BeautifulSoup
from datetime import date

### Web Crawling ###
def get_unit_outline_url(unit_code: str, year: int, is_remote: bool) -> list:
	"""
	Reuturn the unit outline url matching the given year and mode if exists, otherwise, return None
	"""

	# 1. set div id to current or archived
	div_id = "currentOutlines" # id of the div label containing the list of outline urls
	if year != date.today().year:
		div_id = "archivedOutlines"
	
	# 2. request the unit url
	unit_url = f"https://www.sydney.edu.au/units/{unit_code}"
	unit_html = requests.get(unit_url).text
	unit_soup = BeautifulSoup(unit_html, 'lxml')
	
	# 3. find the outlines
	# 3.1 unit code not found
	try:
		outlines = unit_soup.find("div", id = div_id).ul.findAll("li")
	except AttributeError:
		print(f"Unit code: {unit_code} not found")
		exit(2)
	
	# 4. find the unit outline url matching the given year and mode
	for outline in outlines:
		if outline.a == None:						# no a tag
			continue
		outline_url = outline.a["href"]
		if str(year) not in outline_url:			# year not match
			continue
		if (is_remote and "RE" in outline_url) or\
		(not is_remote and "RE" not in outline_url):	# correct mode
			return "https://www.sydney.edu.au" + outline_url
	# 4.1 year not found
	print(f"{unit_code}: {year} outline not found")
	return None