import shutil 
from pprint import pprint
import requests

graph_render_url = 'https://pp.userapi.com/c830208/v830208212/af3e9/ZC4SFENrZYo.jpg'

r = requests.get(graph_render_url,  stream=True)
with open("picture.png", 'wb') as out_file:
    
    r.raw.decode_content = True
    shutil.copyfileobj(r.raw, out_file)
    del r