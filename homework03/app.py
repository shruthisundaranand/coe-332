import json

from flask import Flask

app = Flask(__name__)

def getdata():
    with open("animals.json", "r") as json_data:
        userdata = json.load(json_data)
    return userdata

@app.route('/animals', methods=['GET'])
def get_animals():
    data1 = json.dumps(getdata())
    return data1

@app.route('/animals/head/<string:head_id>', methods=['GET'])
def get_animals_getBunny(head_id):
    data2 = getdata()
    animals1 = data['animals']
    list1 = []
    for animal in animals1:
        if (animal['head:'] == head_id):
            list1.append(animal)
    return jsonify(list1)

@app.route('/animals/legs/<int:leg_id>', methods=['GET'])
def get_animals_getLegs(leg_id):
    data3 = getdata()
    animals2 = data['animals']
    list2 = []
    for animal in animals2:
        if (animal['legs:'] == leg_id):
            list2.append(animal)
    return jsonify(list2)

app.run(debug=True, host='0.0.0.0')

