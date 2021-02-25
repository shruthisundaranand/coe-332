import json
import random


with open('animals.json', 'r') as f:
    animals = json.load(f)

random_animal = random.randrange(0,21)

def breeding():
    parent_1 = random.choice(animals['animals'])
    parent_2 = random.choice(animals['animals'])

    child_head = parent_1['head:']
    child_body = parent_2['body:']
    child_arms = parent_1['arms:'] + parent_2['arms:']
    child_legs = parent_1['legs:'] + parent_2['legs:']
    child_tails = parent_1['tails:'] + parent_2['tails:']

    rand_child = {'head' : child_head,
                  'body' : child_body,
                  'arms' : child_arms,
                  'legs' : child_legs,
                  'tail' : child_tails
                  }

    print('Parent 1: ')
    print(parent_1)
    print('Parent 2: ')
    print(parent_2)
    print('Child: ')
    print(rand_child)

breeding()








