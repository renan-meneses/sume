from factory.validation import Validator
from factory.database import Database


class Weather(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = 'weathers'  # collection name

        self.fields = {
            "city": "string",
            "temp": "float",
            "temp_min": "float",
            "temp_max": "float",
            "dt":"string",
            "description": "list",
            "created": "datetime",
            "updated": "datetime",
        }

        self.create_required_fields = ["city","temp","temp_min","temp_max","dt","description"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = ["city","temp","temp_min","temp_max","dt","description"]

        # Fields optional for UPDATE
        self.update_optional_fields = []

    
    def create(self, weather):
        # Validator will throw error if invalid
        self.validator.validate(weather, self.fields, self.create_required_fields, self.create_optional_fields)
        return self.db.insert(weather, self.collection_name)
         
    
    def find(self, weather):  # find all
        return self.db.find(weather, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, weather):
        self.validator.validate(weather, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, weather,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
