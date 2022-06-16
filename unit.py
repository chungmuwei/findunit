'''
Include the definition of class unit and function relating to unit objects
'''

import requests
from bs4 import BeautifulSoup


class unit:
    '''
    This class represents a unit of study
    '''

    __url: str
    __name: str
    __code: str
    __credit_point: int

    __prohibitions: str
    __prerequisites: str
    __corequisites: str
    # __assumed_knowledge: str

    __coordinator: str
    __email: str

    __overview: str

    def __init__(self, url, code, name, credit_point, overview) -> None:
        self.__url = url
        self.__code = code
        self.__name = name
        self.__credit_point = credit_point
        self.__overview = overview
    
    def code(self) -> str:
        return self.__code
    
    def name(self) -> str:
        return self.__name
    
    def overview(self) -> str:
        return self.__overview
    
    def credit_point(self) -> int:
        return self.__credit_point
    
    def set_prohibitions(self, prohibitions: str) -> None:
        self.__prohibitions = prohibitions
    
    def set_prerequisites(self, prerequisites: str) -> None:
        self.__prerequisites = prerequisites
    
    def set_corequisites(self, corequisites: str) -> None:
        self.__corequisites = corequisites
    
    # def set_assumed_knowledge(self, assumed_knowledge: str) -> None:
    #     self.__assumed_knowledge = assumed_knowledge

    def set_coordinator(self, coordinator: str) -> None:
        self.__coordinator = coordinator
    
    def set_email(self, email: str) -> None:
        self.__email = email

    def __str__(self) -> str:
        return f"""{self.code()}: {self.name()}
Credit point:       |   {self.credit_point()}
Prohibition:        |   {self.__prohibitions}
Prerequisite:       |   {self.__prerequisites}
Corequisite:        |   {self.__corequisites}
Coordinator:        |   {self.__coordinator}, {self.__email}

Overview:
{self.overview()}

Source: {self.__url}

"""
    def markdown(self) -> str:
        return f"""# [{self.code()}: {self.name()}]({self.__url})

- Credit point: {self.credit_point()}
- Prohibition: {self.__prohibitions}
- Prerequisite: {self.__prerequisites}
- Corequisite: {self.__corequisites}
- Coordinator: {self.__coordinator} [{self.__email}]({self.__email})

## Overview:

{self.overview()}

---

"""


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

    overview = unit_outline_soup.find("div", {"id": "uniqueId_uos_overview_panel"}).div.div.div.p.text
    name = unit_outline_soup.find("h1", {"class": "pageTitle b-student-site__section-title"}).text.split(": ")[1]
    credit_point = int(unit_outline_soup.find("div", {"id": "academicDetails"}).table.tbody.findAll("tr")[-1].td.text)

    my_unit = unit(unit_outline_url, unit_code, name, credit_point, overview)

    # add enrolment rules
    enrolment_rules = unit_outline_soup.find("div", {"id": "enrolmentRules"}).table.tbody.findAll("tr")
    my_unit.set_prohibitions(enrolment_rules[0].td.text)
    my_unit.set_prerequisites(enrolment_rules[1].td.text)
    my_unit.set_corequisites(enrolment_rules[2].td.text)

    # add teaching staffs
    t = unit_outline_soup.find("div", {"id": "teachingContacts"}).table.tbody.tr.td.findAll("span")
    my_unit.set_coordinator(t[0].text.strip()) 
    my_unit.set_email(t[1].text) 

    return my_unit