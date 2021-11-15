import pymongo
import csv


def connect():

    # username = input("Username: ")
    # password = input("Password")

    username = "dbUser"
    password = "dbUserPassword"

    connection_url = "mongodb+srv://" + username + ":" + password + "@hrs-cluster.gfzro.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)

    # db = client.test
    return client


def loadToMongo():

    client = connect()

    database = client.hsl_database
    reviews = database.reviews
    new_reviews = []

    filename = "test.csv"
    with open(filename, 'r') as csvfile:

        csv_reader = csv.reader(csvfile)
        fields = next(csv_reader)
        for row in csv_reader:

            record = {}
            for i in range(len(fields)):
                record[fields[i]] = row[i]

            new_reviews.append(record)

    result = reviews.insert_many(new_reviews)
    print(result)


# loadToMongo()
