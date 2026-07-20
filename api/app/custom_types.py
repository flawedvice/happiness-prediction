from pydantic import BaseModel, PositiveFloat


class Data(BaseModel):
    electricity: PositiveFloat = 99.400000  # Access to electricity (% of population)
    agricultural_land: PositiveFloat = 44.270761  # Agricultural land (% of land area)
    alternative_energy: PositiveFloat = (
        6.005000  # Alternative and nuclear energy (% of total energy use)
    )
    food_production: PositiveFloat = (
        101.965455  # Food production index (2014-2016 = 100)
    )
    forest_area: PositiveFloat = 31.738011  # Forest area (% of land area)
    gdp_growth: float = 3.402213  # GDP growth (annual %)
    gdp_per_capita_growth: float = 1.943356  # GDP per capita growth (annual %)
    government_expenditure: PositiveFloat = (
        4.175410  # "Government expenditure on education total (% of GDP)")
    )
    inflation_prices: float = 3.344380  # "Inflation consumer prices (annual %)"
    life_expectancy: PositiveFloat = (
        74.005500  # "Life expectancy at birth total (years)"
    )
    net_migration: float = -3851.500000  # Net migration
    population_growth: float = 1.211590  # Population growth (annual %)
    urban_agglomeration: PositiveFloat = (
        19.846357  # Population in urban agglomerations of more than 1 million (% of total population)
    )
    hiv_prevalence: PositiveFloat = (
        0.300000  # "Prevalence of HIV total (% of population ages 15-49)"
    )
    urban_population: PositiveFloat = (
        36.204590  # Urban population (% of total population)
    )
    rural_population: PositiveFloat = (
        14.500000  # Rural population (% of total population)
    )
    protected_areas: PositiveFloat = (
        5.150000  # Terrestrial and marine protected areas (% of total territorial area)
    )
    unemployment: PositiveFloat = (
        63.795410  # "Unemployment total (% of total labor force) (modeled ILO estimate)"
    )
