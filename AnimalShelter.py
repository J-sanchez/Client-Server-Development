
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

print('Hello, Welcome to Austin Animal Center')

class animalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = "aacuser"
        PASS = "SNHU321"
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30744
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria)
            for document in data:
                print(document)
            else:
                raise Exception("Nothing to read, because criteria parameter is empty")

        return data

    def update(self, criteria, updateData):
        if updateData is not None:
            updated = self.database.animals.update_one(criteria, updateData)
            if updated != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to update, updateData is empty")

    def delete(self, deleteData):
        if deleteData is not None:
            deleted = self.database.animals.delete_many(deleteData)
            if deleted != 0:
                return True
            else: 
                return False
        else:
            raise Exception("Nothing to delete, deleteData is Empty")
            