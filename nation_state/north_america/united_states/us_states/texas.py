import random

population = {
    "1910": 3910052,
    "1914": 4220548,
    "1918": 4531111,
    "1932": 5959894,
    "1936": 6194104,
    "1939": 6370558
}

gdp = {
    "1910": 890000000,
    "1914": 891224232,
    "1918": 912013823,
    "1932": 902324722,
    "1936": 909394732,
    "1939": 912373422
}
def population_growth(texas):
    births = random.randrange(1, 20)
    deaths = random.randrange(1, 17)
    texas.population += (births - deaths)
    texas.nation.current_pop += (births - deaths)
    texas.nation.births += births
    texas.nation.deaths += deaths

"""economic_functions"""
def recovery(alabama):
    if alabama.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 75), 2)
        alabama.investment = round(random.uniform(25, 250), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 750), 2)
        alabama.imports = round(random.uniform(320, 560), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 250), 2)
        alabama.investment = round(random.uniform(25, 350), 2)

        alabama.government_spending = round(random.uniform(100, 800), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 750), 2)
        alabama.imports = round(random.uniform(320, 560), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))
def expansion(alabama):
    if alabama.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 550), 2)
        alabama.investment = round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1000), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 1150), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 550), 2)
        alabama.investment = round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1200), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 1150), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

def recession(alabama):
    if alabama.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 250), 2)
        alabama.investment = -round(random.uniform(25, 350), 2)

        alabama.government_spending = round(random.uniform(100, 300), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 450), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 350), 2)
        alabama.investment = -round(random.uniform(25, 550), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 350), 2)
        alabama.imports = round(random.uniform(320, 860), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

def depression(alabama):
    if alabama.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 550), 2)
        alabama.investment = -round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1400), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 750), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 350), 2)
        alabama.investment = -round(random.uniform(25, 550), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 350), 2)
        alabama.imports = round(random.uniform(320, 1200), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                (alabama.exports - alabama.imports))

def economic_growth(alabama):
    """Economic growth of iowa as individual state"""
    if alabama.economic_state == "recovery":
        recovery(alabama)

    elif alabama.economic_state == "depression":
        depression(alabama)

    elif alabama.economic_state == "recession":
        recession(alabama)

    elif alabama.economic_state == "expansion":
        expansion(alabama)

class Texas:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Texas"
        # establishment of connection to United States
        self.nation = us
        """Population variables"""
        self.population = population[str(year)]
        """economic variables"""
        self.current_gdp = gdp[str(year)]
        self.consumer_spending = None
        self.government_spending = None
        self.investment = None
        self.exports = None
        self.imports = None
        self.economic_state = "recovery"
        self.debt = 0