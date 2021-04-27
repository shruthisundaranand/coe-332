import json
import petname
import random
import uuid
import datetime

heads = ['snake', 'bull', 'lion', 'raven', 'bunny']

def random_head():
    return(random.choice(heads))

def random_body():
    return((random.choice(petname.names)) + '-' + (random.choice(petname.names)))

def random_arms():
    num_of_arms = random.randrange(2,11,2)
    random_arms.arms = num_of_arms
    return(num_of_arms)

def random_legs():
    num_of_legs = random.randrange(3,13,3)
    random_legs.legs = num_of_legs
    return(num_of_legs)

def num_tails(input_arms, input_legs):
    tails = input_arms + input_legs
    return(tails)

def uid():
    uid1 = str(uuid.uuid4())
    return(uid1)

def cdate():
    date = str(datetime.datetime.now())
    return(date)

data = {}

data['animals'] = []

for i in range (20):
    data['animals'].append({
        'uid': uid(),
        'head': random_head(),
        'body': random_body(),
        'arms': random_arms(),
        'legs': random_legs(),
        'tails': num_tails(random_arms.arms, random_legs.legs),
        'created_on': cdate()
        })

with open ('animals.json', 'w') as out:
    json.dump(data, out, indent=2)
