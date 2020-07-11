import json

with open("data/forecast_5days_a.json") as json_file:
    json_data = json.load(json_file)
#this accesses the jsn file and dumps the data into a list.
# print(json_data)

print()
print()
print(type(json_data["Headline"]))
#tell me what type this is (dict, list ext)

# for p_id,p_info in json_data.items():

        # print(key + ':', p_info[key])