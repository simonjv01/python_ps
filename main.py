import subprocess
import json

# Method 1: Run a PowerShell command directly
def run_powershell_command(command):
    completed_process = subprocess.run(
        ["powershell", "-Command", command],
        capture_output=True,
        text=True
    )
    return completed_process.stdout

# Method 2: Run a PowerShell script file
def run_powershell_script(script_path):
    completed_process = subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
        capture_output=True,
        text=True
    )
    return completed_process.stdout

# Examples
if __name__ == "__main__":
    # Example 1: Run a simple command
    # output = run_powershell_command("Get-Process | Select-Object -First 5")
    # print(output)
    
    # Example 2: Run a script file
    script_output = run_powershell_script("C:\\Users\\user\\dev\\pythondev\\python_ps\\export_data.ps1")
    data = json.loads(script_output)
    print(data)