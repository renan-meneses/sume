import json

config_db = {
    "db": {
            "url" : "mongodb://sume:sume@localhost:27017/?authMechanism=DEFAULT",
            "name" :"sume",
            "user" :"sume",
            "password" :"sume"
    }
}

config =json.loads(json.dumps(config_db))  #load db in json format
