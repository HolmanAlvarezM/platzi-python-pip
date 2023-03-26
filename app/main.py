import utils
import read_csv
import charts

def run():
  option = select_option()
  data = read_csv.read_csv('data.csv')

  if option == 1:
    show_population(data)
  else:
    show_world_population(data)

def select_option():
  option = 0
  while option not in range(1, 3):
    print('***' * 10)
    print('Select process to show:')
    print('1. Population of a Country.')
    print('2. World population percent')
    option = int(input('Type your option => '))
  return option

def show_population(data):
  print('***' * 10)
  countryName = input('Type the country => ')
  result = utils.population_by_country(data, countryName)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(countryName, labels, values)

def show_world_population(data):
  option = 0

  while option not in range(1, 7):
    print('***' * 10)
    print('Select a continent:')
    print('1. Africa')
    print('2. Asia')
    print('3. Europe')
    print('4. North America')
    print('5. Oceania')
    print('6. South America')
    option = int(input('Type your option => '))

  continent = ''
  if option == 1:
    continent = 'Africa'
  elif option == 2:
    continent = 'Asia'
  elif option == 3:
    continent = 'Europe'
  elif option == 4:
    continent = 'North America'
  elif option == 5:
    continent = 'Oceania'
  else:
    continent = 'South America'

  data = list(filter(lambda item: item['Continent'] == continent, data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percents = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(continent, countries, percents)

if __name__ == '__main__':
  run()