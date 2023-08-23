import json


def loadAppSettings():
    f = open("app_config.json")
    app_config = json.load(f)
    f.close()
    return app_config

def saveAppSettings(app_config):
    with open('app_config.json', 'w') as f:
        json.dump(app_config, f)