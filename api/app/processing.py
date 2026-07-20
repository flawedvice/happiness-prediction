from custom_types import Data
import pandas as pd
import numpy as np

ORDERED_FEATURES = [
    "electricity",
    "agricultural_land",
    "alternative_energy",
    "food_production",
    "forest_area",
    "gdp_growth",
    "gdp_per_capita_growth",
    "government_expenditure",
    "inflation_prices",
    "life_expectancy",
    "net_migration",
    "population_growth",
    "urban_agglomeration",
    "hiv_prevalence",
    "rural_population",
    "protected_areas",
    "unemployment",
    "urban_population",
]


def engineer_features(df: pd.DataFrame):

    enhanced_df = df.copy()

    # Let's add a urban/rural ratio
    enhanced_df["urban_to_rural_ratio"] = enhanced_df["urban_population"] / (
        enhanced_df["rural_population"] + 1e-6
    )

    # Urban efficiency and overpopulation feature
    enhanced_df["urban_efficiency"] = enhanced_df["urban_agglomeration"] / (
        enhanced_df["urban_population"] + 1e-6
    )

    # Sex education efficiency feature using np.log1p to handle different scales and zero-division
    enhanced_df["sex_ed_efficiency"] = np.log1p(
        enhanced_df["government_expenditure"]
    ) - np.log1p(enhanced_df["hiv_prevalence"])

    # Economic stability based on inflation and GDP
    enhanced_df["economic_stability"] = (
        enhanced_df["gdp_per_capita_growth"] - enhanced_df["inflation_prices"]
    )

    # Drop redundant columns
    enhanced_df.drop(columns=["urban_population"], inplace=True)

    return enhanced_df


def preprocess(data: Data) -> np.ndarray | None:
    # Parse dict to dataframe
    df = pd.DataFrame(data, columns=["variable", "value"]).pivot_table(
        columns="variable", values="value"
    )

    # Set columns to correct order
    ordered = df[ORDERED_FEATURES]

    # Compute new features
    enhanced = engineer_features(ordered)

    # Return processed dataframe as a Numpy array
    input_array = enhanced.to_numpy(dtype=np.float32)

    if not input_array.shape == (1, len(ORDERED_FEATURES) + 3):
        return None

    return input_array
