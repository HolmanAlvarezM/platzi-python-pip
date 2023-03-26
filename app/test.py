import re

dict = {
  '2022 Population':100,
  '2015 Population':90,
  '2010 Population':80,
  '2000 Population':70,
  'other Population':60,
  'more Population':50
}

new_dict = {}

for key, value in dict.items():
  match = re.search(r'\d{4}', key)
  if match:
    new_dict[match.group(0)] = value
print(new_dict)