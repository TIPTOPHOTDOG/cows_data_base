import pymongo
import json


class MongoDBDatabase:

    def __init__(self, host, port, database, collection):
        self.client = pymongo.MongoClient(host, port)
        self.database = self.client[database]
        self.collection = self.database[collection]

    def read_all(self):
        return self.collection.find()

    def read_one(self, id):
        return self.collection.find_one({"_id": id})

    def add(self, data):
        self.collection.insert_one(data)

    def delete(self, id):
        self.collection.delete_one({"_id": id})

    def delete_all(self):
        for i in self.collection.find():
            self.delete(i["_id"])

    def print_data_base(self):
        print('=-=-' * 30, '=', sep='')
        for i in self.read_all():
            for j in i.keys():
                print(j, i[j])
            print('=-=-' * 30, '=', sep='')

    def update(self, id, data):
        self.collection.update_one({"_id": id}, {"$set": data})

    def save_to_json(self, filename):
        with open(filename, "w") as f:
            data = [json.dumps(cow) for cow in self.read_all()]
            f.write(json.dumps(data))


if __name__ == '__main__':
    database = MongoDBDatabase("localhost", 27017, "database", "cows")

    database.delete_all()
    cows = [
        {
            "_id": "12345",
            "name": "Бычок",
            "age": 4,
            "color": "черный",
            "height": 150,
            "weight": 500,
            "vitamins": {
                "A": 100,
                "B1": 20,
                "B2": 30,
                "B3": 40,
                "B5": 50,
                "B6": 60,
                "B12": 70,
                "C": 80,
                "D": 90,
                "E": 100
            },
            "minerals": {
                "Ca": 1000,
                "Fe": 200,
                "Mg": 300,
                "K": 400,
                "Na": 500,
                "P": 600,
                "Zn": 700,
                "Cu": 800,
                "Se": 900,
                "I": 1000
            }
        },
        {
            "_id": "67890",
            "name": "Коровка",
            "age": 6,
            "color": "белая",
            "height": 130,
            "weight": 400,
            "vitamins": {
                "A": 150,
                "B1": 30,
                "B2": 40,
                "B3": 50,
                "B5": 60,
                "B6": 70,
                "B12": 80,
                "C": 90,
                "D": 100,
                "E": 110
            },
            "minerals": {
                "Ca": 1100,
                "Fe": 220,
                "Mg": 330,
                "K": 440,
                "Na": 550,
                "P": 660,
                "Zn": 770,
                "Cu": 880,
                "Se": 990,
                "I": 1100
            }
        },
        {
            "_id": "23456",
            "name": "Телёнок",
            "age": 2,
            "color": "рыжая",
            "height": 120,
            "weight": 300,
            "vitamins": {
                "A": 200,
                "B1": 40,
                "B2": 50,
                "B3": 60,
                "B5": 70,
                "B6": 80,
                "B12": 90,
                "C": 100,
                "D": 110,
                "E": 120
            },
            "minerals": {
                "Ca": 1200,
                "Fe": 240,
                "Mg": 360,
                "K": 480,
                "Na": 600,
                "P": 720,
                "Zn": 840,
                "Cu": 960,
                "Se": 1080,
                "I": 1200
            }
        },
        {
            "_id": "98765",
            "name": "Манька",
            "age": 8,
            "color": "пестрая",
            "height": 140,
            "weight": 550,
            "vitamins": {
                "A": 125,
                "B1": 35,
                "B2": 45,
                "B3": 55,
                "B5": 65,
                "B6": 75,
                "B12": 85,
                "C": 95,
                "D": 105,
                "E": 115
            },
            "minerals": {
                "Ca": 1300,
                "Fe": 260,
                "Mg": 390,
                "K": 520,
                "Na": 650,
                "P": 780,
                "Zn": 910,
                "Cu": 1040,
                "Se": 1170,
                "I": 1300
            }
        }
    ]
    for cow in cows:
        database.add(cow)

    database.print_data_base()

    database.save_to_json("cows.json")
