import configparser
import json
config_object = configparser.ConfigParser()
file = open("services.ini","r")
config_object.read_file(file)
output_dict=dict()
sections=config_object.sections()
for section in sections:
    items=config_object.items(section)
    output_dict[section]=dict(items)

json_string=json.dumps(output_dict)
print("The output JSON string is:")
with open('services.json', 'w') as f:
    json.dump(json.loads(json_string), f)
print(json_string)
file.close()