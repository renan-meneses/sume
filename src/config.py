import json
import bson.json_util as json_util

config_db = {
    "db": {
            "url" : "mongodb://sume:sume@localhost:27017/?authMechanism=DEFAULT",
            "name" :"sume",
            "user" :"sume",
            "password" :"sume"
    }
}
def parse_json(data):
        return json.loads(json_util.dumps(data))

config =json.loads(json.dumps(config_db))  #load db in json format
