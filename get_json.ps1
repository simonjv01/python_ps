# get_json.ps1
$data = @{
    "servers" = @(
        @{
            "name" = "server1"
            "ip" = "192.168.1.101"
            "status" = "online"
        },
        @{
            "name" = "server2"
            "ip" = "192.168.1.102"
            "status" = "offline"
        }
    )
    "timestamp" = (Get-Date).ToString("o")
}


# Convert to JSON and save to file
$data | ConvertTo-Json -Depth 10 | Out-File -FilePath "data.json" -Encoding utf8
