import shutil 
from pprint import pprint
import requests
from PyQt5 import QtWidgets


r = requests.options('http://httpbin.org/get')

pprint(r.headers)
pprint(r.content)
pprint(28956.67/4*1.1)
pprint(27140/20*1.1)
pprint(11*(1+20/30))

