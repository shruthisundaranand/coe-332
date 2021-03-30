import json
from datetime import datetime
from flask import Flask, jsonify, request
from jsonRead import data

app = Flask(__name__)

def getdata():
    with open("animals.json", "r") as json_data:
        userdata = json.load(json_data)
    return userdata

def getdatafile():
    with open("animals.json", "r") as json_data:
        userdata = json.load(json_data)
    return json_data

@app.route('/animals/query', methods = ['GET'])
def get_animals_query():
    #make sure the dates are valid when inputed                                                    
    data1 = getdata()
    animals1 = data['animal']
    start = request.args.get('start')
    end = request.args.get('end')
    list1 = []

    if ((start is None) or (end is None)):
        return jsonify({'error': 'send proper dates'})

    startDate = datetime.strptime(start, '%Y-%m-%d')
    endDate = datetime.strptime(end, '%Y-%m-%d')


    for animal in animals1:
        dt = datetime.strptime(animal['created_on'], '%Y-%m-%d %H:%M:%S.%f')
        if ((dt >= startDate) and (dt <= endDate)):
            list1.append(animal)

    return jsonify({'animals in date range': list1})

@app.route('/animals/select/<string:uuid_id>', methods=['GET'])
def select_animal(uuid_id):
    data2 = getdata()
    animals2 = data['animal']

    for animal in animal2:
        if (animal['uid'] == uuid_id):
            return jsonify({'animal': animal})

    return jsonify({'animal': 'no such animal exists'})

@app.route('/animals/update/<string:uuid_id>', methods=['PUT'])
def update_animal(uuid_id):
    # changing the number of legs to 20 of the specific uuid animal                                
    data3 = getdata()
    animals3 = data['animal']
    animals3_1 = json.load(json_file)
    list3 = {}
    list3['animals'] = []

    modified = []

    for animal in animals3:
        if (animal['uid'] == uuid_id):
            animal['legs'] = 20
            modified.append(animal)
        list3['animals'].append(animal)

    with open(data3, 'w') as outfile:
        json.dump(list3, outfile)

    if(len(modified) == 0):
        return jsonofy({'animal': 'no such animal with id ' + id})

    return jsonify(modified)

@app.route('/animals/delete', methods=['GET'])
def delete_animal():
    data4 = getdata()
    animals4 = data['animals']
    start2 = request.args.get('start')
    end2 = request.args.get('end')
    if ((start is None) or (end is None)):
        return jsonify({'error': 'send proper dates'})

    startDate2 = datetime.strptime(start, '%Y-%m-%d')
    endDate2 = datetime.strptime(end, '%Y-%m-%d')

    output = {}
    output['animals'] = animals.copy()

    for animal in animals14:
        dt2 = datetime.strptime(animal['created_on'], '%Y-%m-%d %H:%M:%S.%f')
        if ((dt2 >= startDate2) and (dt2 <= endDate2)):
            output['animals'].remove(animal)

    with open(data4, 'w') as outfile:
        json.dump(output, outfile)

    if (len(output['animals'])) ==len(animals):
        return jsonify ({'animal': 'no animal removed'})

    return jsonify({'animals after deleting': output})

@app.route('/animals/avglegs', methods=['GET'])
def average_legs():
    `# finds average number of legs of all animals                                                 
    data5 = getdata()
    animals5 = data['animals']
    num_legs = 0
    count5 = len(animals5)
    for animal in animals:
        num_legs = num_legs + animal['legs']
    leg_count = num_legs/count5
    if (leg_count > 0):
        return jsonify({'average': leg_count})
    else:
        return jsonify({'average': 0})


@app.route('/animals/total', methods=['GET'])
def total_animals():
    # returns the total number of animals in the json file - should be 20                          
    data6 = getdata()
    animals6 = data['animals']
    count = len(animals6)
    return jsonify ({'count': count})


app.run(debug= True, host = '0.0.0.0')
