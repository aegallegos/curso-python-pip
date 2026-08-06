import charts
import read_csv
import utils
import pandas as pd

""" data = [
    {"country": "Colombia", "population": 300},
    {"country": "Bolivia", "population": 400},
    {"country": "Chile", "population": 500},
    {"country": "Venezuela", "population": 600},
] """


def run():
    """keys, values = utils.get_population()
    print(keys, values)
    """
    df = pd.read_csv("world_population.csv")
    df = df[df['Continent'] == 'North America']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

    data = read_csv.read_csv("world_population.csv")
    country = input("Ingrese el nombre del país: ")
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
        charts.generate_pie_chart(labels, values)
    """    print(
            f"Population by country: {result}"
        )  # Output: [{'country': 'Bolivia', 'population': 400}]
    """


if __name__ == "__main__":
    run()
