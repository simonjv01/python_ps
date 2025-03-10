import json
import subprocess

# Run the script that generates the JSON data
script_path = 'c:\\Users\\sjvar\\dev\\pythondev\\python_ps\\export_data.ps1'
subprocess.run(["powershell.exe", "-File", script_path], check=True)

# Load the JSON data from file
with open('output.json', 'rb') as file:
    data = json.load(file)

# Process the data
# print(f"Received data with timestamp: {data['timestamp']}")
for item in data:
    print(item['Name'])

    

# Do something with the data
# ...