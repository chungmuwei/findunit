class unit:

    __url: str
    __name: str
    __code: str
    __credit_point: int

    __prohibitions: str
    __prerequisites: str
    __corequisites: str
    # __assumed_knowledge: str

    __coordinator: str

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
    
    def __str__(self) -> str:
        return f"""{self.code()}: {self.name()}
Credit point:       |   {self.credit_point()}
Prohibition:        |   {self.__prohibitions}
Prerequisite:       |   {self.__prerequisites}
Corequisite:        |   {self.__corequisites}

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

## Overview:

{self.overview()}

---

"""
    
if __name__ == "__main__":
    comp2022 = unit("comp2022")
    print(comp2022.code())
