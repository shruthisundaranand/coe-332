import json
import random


with open('animals.json', 'r') as f:
    animals = json.load(f)

rand_animal = random.randrange(0,21)

print(animals['animals'][rand_animal])
