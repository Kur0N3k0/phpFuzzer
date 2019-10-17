class Result:
    line = 0
    code = ""

    def __init__(self, line, code):
        self.line = int(line)
        self.code = str(code)

    def __str__(self):
        return "{}: {}".format(self.line, self.code)