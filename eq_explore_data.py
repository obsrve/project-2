import json

filename = 'project-2\data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readeble_file = 'project-2\data\\readable_eq_data.json'
with open(readeble_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
