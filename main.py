import json

# Load the JSON data from file
with open('output.json', 'rb') as file:
    data = json.load(file)

# Process the data
# print(f"Received data with timestamp: {data['timestamp']}")
for item in data:
    print(item['Name'])

    

# Do something with the data
# ...