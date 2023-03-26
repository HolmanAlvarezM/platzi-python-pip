import re

def get_population(country_dict):
  population_dict = {}

  for key, value in country_dict.items():
    match = re.search(r'\d{4}', key)
    if match:
      population_dict[match.group(0)] = int(value)
  return population_dict.keys(), population_dict.values()

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'].lower() == country.lower(), data))
  return result