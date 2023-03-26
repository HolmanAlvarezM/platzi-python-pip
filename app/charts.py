import matplotlib.pyplot as plt

def generate_bar_chart(country, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{country}.png')
  plt.close()

def generate_pie_chart(continent, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{continent}.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 50, 20]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)