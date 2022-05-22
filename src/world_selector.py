import json
import requests
import random

worlds_url = 'https://api.tibiadata.com/v3/worlds'


def get_worlds(url):

    worlds_array = []

    re = requests.get(url)
    status_code = re.status_code
    if(status_code != 200):
        return "Error with status code {}".format(status_code)

    re_content = re.content
    output = json.loads(re_content)

    for i in output['worlds']['regular_worlds']:
        list.append(worlds_array, i['name'])

    return worlds_array


worlds = get_worlds(worlds_url)

def draw_world(worlds):

    index = random.randrange(0, len(worlds)-1)

    return worlds[index]


print(draw_world(worlds))