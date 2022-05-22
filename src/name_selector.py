import json
import requests
import random

names_url = 'http://names.drycodes.com/100?separator=space&format=json'


def get_names(url):
    
    re = requests.get(names_url)
    status_code = re.status_code
    
    if(status_code != 200):
        return "Error with status code {}".format(status_code)

    re_content = re.content
    output = json.loads(re_content)

    return output


def draw_name():
    
    random_index = random.randrange(0, len(names)-1)
    
    return(names[random_index].title())


names = get_names(names_url)

print(draw_name())
