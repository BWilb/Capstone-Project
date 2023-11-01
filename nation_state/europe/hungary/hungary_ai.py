import random
from datetime import datetime, timedelta
import time
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leader_images = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../leaders/hungary/OIP.jpg",
    "1936": "../leaders/hungary/OIP.jpg",
    "1939": "../leaders/hungary/OIP.jpg"
}
flags = {
    "1910": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1914": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1918": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1932": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1936": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1939": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg"
}

prime_ministers = {
    "1910": None,
    "1914": None,
    "1918": None,
    "1932": "Miklos Horthy",
    "1936": "Miklos Horthy",
    "1939": "Miklos Horthy"
}

"""Economic variables and dictionaries"""
gdp = {
    "1910": 7243560000,
    "1914": 7294052632,
    "1918": 7318292632,
    "1932": 12072684211,
    "1936": 15920315789,
    "1939": 19837894737
}

"""Population variables and dictionaries"""
population = {
    "1910": 7600000,
    "1914": 7740000,
    "1918": 7860000,
    "1932": 8740000,
    "1936": 8900000,
    "1939": 9180000
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class HungaryAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Hungary"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = prime_ministers[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        if globe.date.year < 1932:
            self.political_typology = ""
        self.political_power = 200
        self.political_exponent = 1.56
        """Stability"""
        self.stability = 95.56
        # economic
        self.corporate_taxes = 24.00
        self.income_taxes = 20.00
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        self.us_relations = 34.56
        # other
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(0, len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "Hungary":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

    def main(self, globe, network):
        #super().establishing_beginning_objectives()
        while self.population > 100000:
            """super().check_economic_growth(globe.date)
                        super().check_population_growth()
                        # random_functions.random_functions(self, globe)
                        super().stability_happiness_change(globe)
                        super().political_power_growth()
                        super().determine_diplomatic_approach(globe.nations, globe, network)
                        super().change_relations(globe.nations)
                        chance = random.randrange(1, 50)
                        if chance % 8 == 2 or chance % 5 == 4:
                            super().protests()"""
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break