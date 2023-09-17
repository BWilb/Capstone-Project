import random
import time
from enum import Enum
from datetime import datetime, timedelta


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4
class NationAI:
    def __init__(self, globe):
        # general information
        self.population_reward = 0
        self.economic_reward = 0
        self.region = ""
        self.name = ""
        self.date = datetime(globe.date.year, 1, 1)
        self.year_placeholder = self.date.year
        self.economic_change_date = self.date + timedelta(days=120)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        # social factors
        """population factors"""
        self.population = 0
        self.birth_control = False
        self.birth_enhancer = False
        self.births = 0
        self.deaths = 0
        self.happiness = 98.56
        # political
        self.leader = "Gregory Prescov"
        self.political_power = 100
        self.political_exponent = 1.00
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = EconomicState.RECOVERY
        self.national_debt = 0
        self.current_gdp = 0
        self.past_gdp = self.current_gdp
        self.corporate_taxes = 5.00
        self.income_taxes = 5.00
        """Components of GDP"""
        self.consumer_spending = 100
        self.investment = 100
        self.government_spending = 150
        self.exports = 500
        self.imports = 500

    def check_population_growth(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""

        if self.year_placeholder < self.date.year:
            pop_change = ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100

            if pop_change < 1.25:
                self.population_stability = 0
                self.population_reward -= 1.25
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 1:
                    print(f"{self.leader}'s government has decided to implement policies to increase growth in births.\n")
                    time.sleep(1.25)

                    self.birth_enhancer = True

                    if self.birth_control:
                        self.birth_control = False

            elif pop_change >= 1.25 and pop_change <= 8.56:
                """If statement increments variable holding into account whether population is becoming stable or not"""
                self.population_stability += 1
                self.population_reward += 5

                if self.population_stability >= 2:
                    """checking to see if population growth has been stable for 2 years or longer"""
                    if self.population_reward < 10:
                        chance = random.randrange(0, 10)
                        if chance % 4 == 2:
                            """25% chance that government will choose to remove protocols"""
                            self.birth_control = False
                            self.birth_enhancer = False

                    if self.population_reward > 10 and self.population_reward < 20:
                        chance = random.randrange(0, 10)
                        if chance % 3 == 2:
                            """33% chance that government will choose to remove protocols"""
                            self.birth_control = False
                            self.birth_enhancer = False

                    if self.population_reward >= 30:
                        chance = random.randrange(0, 10)
                        if chance % 2 == 0:
                            """50% chance that government will choose to remove protocols"""
                            self.birth_control = False
                            self.birth_enhancer = False

            elif pop_change > 8.56:
                self.population_stability = 0
                self.population_reward -= 1.25
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 1:
                    print(f"{self.leader}'s government has decided to implement policies to control births.\n")
                    time.sleep(1.25)

                    self.birth_control = True

                    if self.birth_enhancer:
                        self.birth_enhancer = False
        else:
            self.regular_pop_growth()


    def regular_pop_growth(self):
        if self.population < 1000000:
            if self.birth_enhancer:
                births = random.randrange(self.population * 0.00003, self.population * 0.00005)
                deaths = random.randrange(self.population * 0.00002, self.population * 0.000045)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = int(random.randrange(self.population * 0.000015, self.population * 0.000030))
                deaths = int(random.randrange(self.population * 0.000018, self.population * 0.000025))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = (random.randrange(int(self.population * 0.000025), int(self.population * 0.000040)))
                deaths = (random.randrange(int(self.population * 0.000020), int(self.population * 0.000035)))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

        elif self.population > 1000000 and self.population < 250000000:
            if self.birth_enhancer:
                births = int(random.randrange(self.population * 0.0000007, self.population * 0.0000009))
                deaths = int(random.randrange(self.population * 0.0000005, self.population * 0.0000008))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = int(random.randrange(self.population * 0.0000004, self.population * 0.0000007))
                deaths = int(random.randrange(self.population * 0.0000005, self.population * 0.0000008))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = random.randrange(int(self.population * 0.0000006), int(self.population * 0.0000008))
                deaths = random.randrange(int(self.population * 0.0000005), int(self.population * 0.0000007))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths
        else:
            if self.birth_enhancer:
                births = int(random.randrange(self.population * 0.00000007, self.population * 0.00000009))
                deaths = int(random.randrange(self.population * 0.00000005, self.population * 0.00000008))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = int(random.randrange(self.population * 0.00000004, self.population * 0.00000007))
                deaths = int(random.randrange(self.population * 0.00000005, self.population * 0.00000008))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = (random.randrange(int(self.population * 0.00000006), int(self.population * 0.00000008)))
                deaths = (random.randrange(int(self.population * 0.00000005), int(self.population * 0.00000007)))
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

    def political_power_growth(self):
        self.political_power += self.political_exponent

    # economic functions
    def check_economic_state(self):
        """function dealing with primary economic decisions of canadian parliament"""
        if self.date > self.economic_change_date:
            """instead of comparing an entire year, break the year up into sections/potential business cycles"""
            gdp_growth = ((self.current_gdp - self.past_gdp) / ((self.current_gdp + self.past_gdp) / 2)) * 100
            if gdp_growth >= 6.65:
                self.economic_stability = 0
                self.economic_reward -= 1.25
                # economy rises into expansion
                if self.e_s == EconomicState.RECOVERY:
                    self.e_s = "expansion"
                    print("Your economy is now in an expansionary period.\n")
                    self.consumer_spending = 300
                    self.government_spending = 500
                    self.investment = 350
                    self.imports = 1000
                    self.exports = 1200
                    time.sleep(3)
                    self.economic_change_date = self.date + timedelta(days=120)
                # economy rises into recovery
                elif self.e_s == EconomicState.RECESSION or self.e_s.lower() == EconomicState.DEPRESSION:
                    self.e_s = "recovery"
                    print("Your economy is now in recovery period.\n")
                    self.consumer_spending = 200
                    self.government_spending = 300
                    self.investment = 250
                    self.imports = 1000
                    self.exports = 900
                    time.sleep(3)
                    self.economic_change_date = self.date + timedelta(days=120)

            elif gdp_growth <= -0.25:
                self.economic_stability = 0
                self.economic_reward -= 1.25
                # economy falls into depression
                if self.e_s == EconomicState.RECESSION:
                    self.e_s = "depression"
                    self.consumer_spending = -200
                    self.government_spending = 00
                    self.investment = -250
                    self.imports = 1700
                    self.exports = 500
                    print("Your economy is now in a recessionary period.\n")
                    time.sleep(3)
                    self.economic_change_date = self.date + timedelta(days=120)

                # economy falls into recession
                elif self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
                    self.e_s = "recession"
                    self.consumer_spending = -100
                    self.government_spending = 300
                    self.investment = -150
                    self.imports = 1500
                    self.exports = 800
                    print("Your economy is now in a depression period.\n")
                    time.sleep(3)
                    self.economic_change_date = self.date + timedelta(days=120)

            elif gdp_growth < 6.65 or gdp_growth >= 1.25:
                self.economic_stability += 1
                self.economic_reward += 5

        else:
            # gets called regardless of the current economic state
            self.provide_economic_aid()

            if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
                self.neg_ec_growth()

            elif self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
                self.pos_ec_growth()

    def provide_economic_aid(self):
        if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
            if self.economic_reward < 10:
                """lower reward means government will most likely not choose to do anything
                higher reward means the opposite
                """
                chance = random.randrange(0, 10)
                if chance % 4 == 0:
                    """25% chance that government will do something
                    - raise corporate and income taxes by 5-10%(causes consumer spending and investment to decrease)
                    - increase government spending
                    """
                    self.corporate_taxes = self.corporate_taxes * 0.05
                    self.income_taxes = self.income_taxes * 0.05
                    self.government_spending += 200
                    self.consumer_spending -= 150
                    self.investment -= 150

                if chance % 3 == 0:
                    """33% chance that government will do something
                    - raise corporate and income taxes by 5-10%(causes consumer spending and investment to decrease)
                    - increase government spending
                    """
                    self.corporate_taxes = self.corporate_taxes * 0.10
                    self.income_taxes = self.income_taxes * 0.10
                    self.government_spending += 400
                    self.consumer_spending -= 200
                    self.investment -= 200

                if chance % 2 == 0:
                    """50% chance that government will do something
                    - raise corporate and income taxes by 5-10%(causes consumer spending and investment to decrease)
                    - increase government spending
                    """
                    self.corporate_taxes = self.corporate_taxes * 0.15
                    self.income_taxes = self.income_taxes * 0.15
                    self.government_spending += 600
                    self.consumer_spending -= 250
                    self.investment -= 250

                else:
                    self.stability -= 5
                    self.happiness -= 10

    def pos_ec_growth(self):
        self.national_debt += round(
            (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

        self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                             (self.exports - self.imports))

    def neg_ec_growth(self):
        self.national_debt += round(self.government_spending * round(random.uniform(0.15, 0.35), 4), 2)

        self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                             (self.exports - self.imports))
    # stability functions
    def stability_happiness_change(self, globe):
        print('hhi')
        if globe.tension > 25 and globe.tension < 50:
            """if global tension is between 25 and 50"""
            if self.e_s.RECESSION or self.e_s.DEPRESSION:
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.25, 1.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.25, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    happiness_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.50, 1.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.45, 1.65), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.75, 2.76), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        elif globe.tension > 50 and globe.tension < 75:
            """if global tension is between 50 and 75"""
            if self.e_s.RECESSION or self.e_s.DEPRESSION:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.10, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.05, 1.05), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.13, 0.96), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.10, 0.76), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.05, 1.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(0.96, 1.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        elif globe.tension > 75:
            """if global tension is above 75"""
            if self.e_s.RECESSION or self.e_s.DEPRESSION:
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.05, 0.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_decrease = round(random.uniform(1.56, 3.75), 2)
                    if (self.stability - stability_decrease) > 5:
                        self.stability -= stability_decrease

                if self.improve_happiness > self.date:
                    stability_increase = round(random.uniform(0.05, 0.99), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_decrease = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability - stability_decrease) > 5:
                        self.stability -= stability_decrease

            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_increase = round(random.uniform(1.45, 2.34), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """If policies toward improving happiness have been imposed"""
                    happiness_increase = round(random.uniform(1.05, 2.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(0.96, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        else:
            if self.improve_stability > self.date:
                stability_increase = round(random.uniform(1.56, 2.56), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            else:
                stability_increase = round(random.uniform(1.45, 2.34), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            if self.improve_happiness > self.date:
                """If policies toward improving happiness have been imposed"""
                happiness_increase = round(random.uniform(1.05, 2.96), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase
            else:
                happiness_increase = round(random.uniform(0.96, 2.56), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase