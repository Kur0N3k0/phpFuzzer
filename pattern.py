import glob
import re
from config import *
from result import *

class Pattern:
    pattern = {}

    def __init__(self):
        config = Config()
        pattern = glob.glob(config["pattern"])
        for pt in pattern:
            pt = pt.replace("\\", "/")
            item = json.load(open(pt, "r"))
            self.pattern[item["name"]] = item["regex"]

    def match(self, file):
        content = ""
        with open(file, "r") as f:
            for line in f:
                content += line
        result = {}
        for name in self.pattern:
            result[name] = []
            for pt in self.pattern[name]:
                for item in re.findall(pt, content):
                    idx = content.find(item)
                    line = content[:idx].count("\n") + 1
                    code = item
                    p = Result(line, code)
                    result[name] += [p]
        return result