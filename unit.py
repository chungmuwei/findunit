'''
Include the definition of class unit and function relating to unit objects
'''

from operator import contains
import requests
from bs4 import BeautifulSoup


class unit:
    '''
    This class represents a unit of study
    '''

    __url: str

    __academic_details: dict
    __enrolment_rules: dict
    __teaching_contacts: dict

    __overview: str

    def __init__(self, url) -> None:
        self.__url = url

    def set_overview(self, overview) -> None:
        self.__overview = overview
    
    def set_academic_details(self, academic_details: dict) -> None:
        self.__academic_details = academic_details

    def set_enrolment_rules(self, enrolment_rules: dict) -> None:
        self.__enrolment_rules = enrolment_rules

    def set_teaching_contacts(self, teaching_contacts: dict) -> None:
        self.__teaching_contacts = teaching_contacts

    def __str__(self):
        """
        Return the unit outline in plain text
        """

        ret = ""

        ad = self.__academic_details
        ret += f"{ad['Unit code']}: {ad['Unit name']}\n\n"

        ret += f"Overview:\n{self.__overview}\n\n"

        ret += "Academic details:\n"
        for k, v in self.__academic_details.items():
            ret += "{:<20s}  |   {:s}\n".format(k, v)
        ret += "\n"

        ret += "Enrolment rules:\n"
        for k, v in self.__enrolment_rules.items():
            ret += "{:<20s}  |   {:s}\n".format(k, v)
        ret += "\n"

        ret += "Teaching staff and contact details:\n"
        for k, v in self.__teaching_contacts.items():
            ret += "{:<20s}  |   {:s}\n".format(k, v)
        ret += "\n"

        ret += f"Source: {self.__url}\n"

        ret += "="*80
        ret += "\n"

        return ret

    def markdown(self) -> str:
        """
        Return the unit outline in markdown format
        """

        ret = ""

        ad = self.__academic_details
        ret += f"# [{ad['Unit code']}: {ad['Unit name']}]({self.__url})\n\n"

        ret += f"## Overview\n{self.__overview}\n\n"

        ret += "## Academic details\n"
        for k, v in self.__academic_details.items():
            ret += f"- {k}: {v}\n"
        ret += "\n"

        ret += "## Enrolment rules\n"
        for k, v in self.__enrolment_rules.items():
            ret += f"- {k}: {v}\n"
        ret += "\n"

        ret += "## Teaching staff and contact details\n"
        for k, v in self.__teaching_contacts.items():
            if (k != "Administrative staff"):
                tmp = v.split(',')
                tmp[0] = tmp[0].strip()
                tmp[1] = tmp[1].strip()
                tmp[1] = f"[{tmp[1]}](mailto:{tmp[1]})"
                v = ', '.join(tmp)
            ret += f"- {k}: {v}\n"
        ret += "\n"
        ret += "---"
        ret += "\n\n"

        return ret


def create_unit_object(unit_outline_url: str, unit_code: str) -> unit:
    """
    Create unit object to store information about the unit

	Parameters:
		unit_outline_url: unit outline url string 
		unit_code: unit code string
	Returns:
		unit object corresponds to the unit outline
	"""

    unit_outline_html = requests.get(unit_outline_url).text
    unit_outline_soup = BeautifulSoup(unit_outline_html, 'lxml')

    my_unit = unit(unit_outline_url)
    

    # scraping academic details and store in a dictionary
    academic_details = unit_outline_soup.find("div", {"id": "academicDetails"}).table.tbody.findAll("tr")
    details = dict()
    for i in range(len(academic_details)):
        key = ' '.join(academic_details[i].th.text.split()).replace(' ?', '')
        value = academic_details[i].td.text
        details[key] = value
    my_unit.set_academic_details(details)
    
    # scraping enrolment rules and store in a dictionary
    enrolment_rules = unit_outline_soup.find("div", {"id": "enrolmentRules"}).table.tbody.findAll("tr")
    rules = dict()
    for i in range(len(enrolment_rules)):
        key = ' '.join(enrolment_rules[i].th.text.split()).replace('?', '')
        value = enrolment_rules[i].td.text
        rules[key] = value
    my_unit.set_enrolment_rules(rules)

    # scraping teaching staff and contact details
    teaching_contacts = unit_outline_soup.find("div", {"id": "teachingContacts"}).table.tbody.findAll("tr")
    contacts = dict()
    for i in range(len(teaching_contacts)):
        key = teaching_contacts[i].th.text
        value = ' '.join(teaching_contacts[i].td.text.split())   # remove all whitespace characters
        contacts[key] = value
    my_unit.set_teaching_contacts(contacts)

    # scraping overview
    overview = unit_outline_soup.find("div", {"id": "uniqueId_uos_overview_panel"}).div.div.div.p.text
    my_unit.set_overview(overview)

    return my_unit

if __name__ == "__main__":
    math1002 = create_unit_object("https://www.sydney.edu.au/units/MATH1002/2022-S1C-ND-CC", "")
    math1002.print()
