import json

class Config:
    config = None

    def __init__(self):
        self.config = json.load(open("./config.json", "r"))

    def __getitem__(self, item):
        return self.config[item]