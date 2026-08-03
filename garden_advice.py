"""
Garden Advice App

A simple command-line tool that asks the user for the current season
and the type of plant they are growing, then prints tailored care
advice and a plant recommendation based on their answers.
"""

# Dictionary storing watering/care advice for each season
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

# Dictionary storing care advice for each plant type
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

# Dictionary recommending plants suited to each season
SEASON_PLANT_RECOMMENDATIONS = {
    "summer": "Recommended plants for summer: sunflowers, tomatoes, basil.",
    "winter": "Recommended plants for winter: kale, pansies, garlic.",
}


def get_season_advice(season):
    """
    Return care advice for the given season.
    If the season is not recognised, return a default message.
    """
    return SEASON_ADVICE.get(season, "No advice for this season.\n")


def get_plant_advice(plant_type):
    """
    Return care advice for the given plant type.
    If the plant type is not recognised, return a default message.
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def get_plant_recommendation(season):
    """
    Return a plant recommendation for the given season.
    If the season is not recognised, return a default message.
    """
    return SEASON_PLANT_RECOMMENDATIONS.get(
        season, "No plant recommendations available for this season."
    )


def main():
    """
    Ask the user for their season and plant type, then print
    combined care advice and a plant recommendation.
    """
    valid_seasons = SEASON_ADVICE.keys()
    valid_plants = PLANT_ADVICE.keys()

    season = input(
        "Enter the current season (summer/winter): ").strip().lower()
    while season not in valid_seasons:
        print(
            f"Invalid season. Please choose from: {', '.join(valid_seasons)}")
        season = input(
            "Enter the current season (summer/winter): ").strip().lower()

    plant_type = input(
        "Enter the plant type (flower/vegetable): ").strip().lower()
    while plant_type not in valid_plants:
        print(
            f"Invalid plant type. Please choose from: "
            f"{', '.join(valid_plants)}")
        plant_type = input(
            "Enter the plant type (flower/vegetable): ").strip().lower()

    advice = get_season_advice(season) + get_plant_advice(plant_type)
    recommendation = get_plant_recommendation(season)

    print(advice)
    print(recommendation)


if __name__ == "__main__":
    main()
