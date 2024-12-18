import subprocess

# Function to ping a host and check if it's reachable
def check_latency(host):
    # Run the ping command with '-c 1' to send 1 ping
    response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    
    # If the ping was successful (returncode 0), it's reachable
    if response.returncode == 0:
        return f"{host} is reachable"
    else:
        return f"{host} is not reachable"

# Ask user to enter hostnames separated by commas
hosts = input("Enter hostnames (comma-separated): ").split(',')

# Check latency for each host
for host in hosts:
    print(check_latency(host.strip()))
