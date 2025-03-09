import json

# Load the JSON data from file
with open('data.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Process the data
print(f"Received data with timestamp: {data['timestamp']}")
for server in data['servers']:
    print(f"Server: {server['name']}, IP: {server['ip']}, Status: {server['status']}")

# Do something with the data
# ...