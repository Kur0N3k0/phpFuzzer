from Queue import *

from pattern import *
from config import *

from selenium import webdriver
from bs4 import BeautifulSoup

class Fuzzer:
    pattern = None

    def __init__(self, url):
        self.pattern = Pattern()
        self.target = url
        self.config = Config()

    def parse_url(self, url):
        info = url.spilt("?")
        result = { "uri": info[0] }
        if len(info) > 1:
            pinfo = info[1].spilt("&")
            names = []
            for item in pinfo:
                name = item.spilt("=")[0]
                names += [name]
            result["param"] = ",".join(names)
        return result

    def cmp_param(self, a1, a2):
        return len(a1) == len(a2) and len(set(a1) & set(a2)) == len(a1)

    def request(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")

        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
        driver = webdriver.Chrome("./thirdparty/chromedriver.exe", chrome_options=options)
        driver.get(url)
        driver.implicitly_wait(2)

        html = driver.page_source
        return html

    def get_urls(self, html):
        soup = BeautifulSoup(html, "html.parser")

    def run(self):

        queue = Queue()
        queue.put(self.target)

        while not queue.empty():
            url = queue.get()
            # parse url
            self.parse_url(url)
            # get available urls
            source = self.request(url)
            self.get_urls(source)
            # exploit stub
            #



fuzz = Fuzzer()
fuzz.run()