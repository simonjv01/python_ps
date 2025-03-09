# Get some data
$data = Get-Service | Select-Object -First 10 -Property Name, Status, DisplayName

# Convert to JSON and save to file
# $data | ConvertTo-Json | Out-File -FilePath "output.json"

# Convert to JSON and output to stdout
$data | ConvertTo-Json 