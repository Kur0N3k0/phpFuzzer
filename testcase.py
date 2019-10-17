import fnmatch
import os
from config import *

class Testcase:
    path = []

    def __init__(self):
        config = Config()
        for root, dirnames, filenames in os.walk(config["testcase"]):
            for filename in fnmatch.filter(filenames, config["extension"]):
                self.path.append(root.replace("\\", "/") + "/" + filename.replace("\\", "/"))
"""
        for report in self.testcase.path:
            report = os.path.dirname(report)
            report = report.replace(self.config["testcase"], self.config["result"])
            if not os.path.exists(report):
                os.makedirs(report)
"""