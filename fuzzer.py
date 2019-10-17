import os
from pattern import *
from testcase import *
from config import *

class Fuzzer:
    pattern = None
    testcase = None

    def __init__(self):
        self.pattern = Pattern()
        self.testcase = Testcase()
        self.config = Config()

    def run(self):
        for file in self.testcase.path:
            result = "[{}]\n".format(file)
            match = self.pattern.match(file)
            cnt = 0

            for name in match:
                for item in match[name]:
                    result += "{} #{}".format(name, str(item).replace("\n", "\\n")) + "\n"
                    cnt += 1
            if cnt == 0:
                continue

            print result
            report = file.replace(self.config["testcase"], self.config["result"])
            path = os.path.dirname(report)
            if not os.path.exists(path):
                os.makedirs(path)
            with open(report, "wb") as f:
                f.write(result)

fuzzer = Fuzzer()
fuzzer.run()