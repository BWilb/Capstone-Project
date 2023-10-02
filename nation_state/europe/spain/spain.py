import random
import time
from datetime import datetime, timedelta

from globe_relations import globe
from datetime import datetime, timedelta
from game.ai import playable_nation

leaders = {
    "1910" : "Segismundo Moret",
    "1914" : "Eduardo Dato",
    "1918" : "Manuel García Prieto",
    "1932" : "Niceto Alcalá-Zamora",
    "1936" : "Manuel Azaña",
    "1939" : "Manuel Azaña"
}
monarchs = {
    "1910" : "Alfonso XIII",
    "1914" : "Alfonso XIII",
    "1918" : "Alfonso XIII",
    "1932" : "Henri VII/Jacques II",
    "1936" : "Henri VII/Jacques II",
    "1939" : "Henri VII/Jacques II"
}

population = {
    "1910": 19681917,
    "1914": 20250331,
    "1918": 20790497,
    "1932": 23812074,
    "1936": 24628744,
    "1939": 24892000
}
gdp = {
    "1910": 2159663720,
    "1914": 2547024746,
    "1918": 5653286406,
    "1932": 2940653248,
    "1936": 3978738880,
    "1939": 4366978929
}

flags = {"1910": "../flags/spain/spain_flag_1910-1930.png",
         "1914": "../flags/spain/spain_flag_1910-1930.png",
         "1918": "../flags/spain/spain_flag_1910-1930.png",
         "1932": "../flags/spain/spanish_flag_1932_1936.jpg",
         "1936": "../flags/spain/spanish_flag_1932_1936.jpg",
         "1939": "../flags/spain/nationalist_spain_1939.jpg"}

leader_images = {
    "1910": "../leaders/spain/alfonso_xiii.jpg",
    "1914": "../leaders/spain/alfonso_xiii.jpg",
    "1918": "../leaders/spain/alfonso_xiii.jpg",
    "1932": "../leaders/spain/330px-Niceto_Alcalá-Zamora_(cropped)1932-1936.jpg",
    "1936": "../leaders/spain/330px-Niceto_Alcalá-Zamora_(cropped)1932-1936.jpg",
    "1939": "../leaders/spain/franco.jpg"
}

class Spain(playable_nation.PlayableNation):
    def __init__(self, year):
        self.name = "Kingdom of Spain"
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[year]
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[year]
        self.leader_image = leader_images[year]
        self.flag = flags[year]
        """Stability"""
        self.stability = 95.56
        # economic
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        # other
        self.chosen = False