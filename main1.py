import json


class Countries:

    def __init__(self, file):
        self.file = file
        self.country_index = 0
        self.new_file = open("wiki_countries.txt", "a")

    def __iter__(self):
        return self

    def __next__(self):
        if self.country_index == len(self.file):
            raise StopIteration
        current_country = self.file[self.country_index]
        self.country_index += 1
        name = current_country['name']['common']
        pair = {name: "https://en.wikipedia.org/wiki/" + name}
        self.new_file.write(str(pair) + "\n")
        return current_country


if __name__ == '__main__':
    with open('countries.json') as json_file:
        data = json.load(json_file)
        for country in Countries(data):
            pass
