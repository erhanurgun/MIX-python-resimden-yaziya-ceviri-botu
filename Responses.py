import json

def sample_response(input_text):
    user_message = str(input_text).lower()
    with open('db.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for p in data:
            if user_message in p['keys']:
                return p['value']

    return "Ne demek istediğini anlayamadım!"
