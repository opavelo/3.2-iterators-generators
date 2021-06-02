import json
from pprint import pprint
import hashlib

class CountriesIterate:
    def __iter__(self):
        self.countries = []
        with open('countries.json', 'r', encoding = 'utf-8') as f:
            self.json_data = json.load(f)
        for land in self.json_data:
            self.countries.append(land['name']['common'])
        self.countries = iter(set(self.countries))
        #pprint(self.countries)
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        Country = next(self.countries)
        link = Country.replace(' ', '_')
        link = 'https://en.wikipedia.org/wiki/' + str(link)

        return link + ' - ' + Country + '\n'

with open(r'Country-Link.txt', 'w', encoding = 'utf-8') as f:
    for name in CountriesIterate():
        f.write(name)
    f.close()

def my_generator(link):
    with open(link, 'r', encoding='utf-8') as f:
        data = f.readlines()
    for line in data:
        line = line.rstrip()
        line_json = json.dumps(line)
        line_hash = hashlib.md5(line_json.encode()).hexdigest()
        yield line_hash

for number in my_generator('Country-Link.txt'):
    print(number)