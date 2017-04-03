import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds141450.mlab.com:41450/kisskiss1709
host = "ds141450.mlab.com"
port = 41450
db_name = "kisskiss1709"
username = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())