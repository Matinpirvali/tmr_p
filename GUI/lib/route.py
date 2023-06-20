import subprocess

def change_dns_linux(dns_servers):
    # Concatenate the DNS server addresses into a single string

    # Execute the system command to change DNS servers
    command = f'sudo sh -c "echo nameserver {dns_servers} > /etc/resolv.conf"'
    result = subprocess.run(command, shell=True)

    if result.returncode == 0:
        print("DNS servers changed successfully.")
    else:
        print("Failed to change DNS servers.")

# Specify the DNS server addresses you want to set
dns_servers = """nameserver 10.202.10.202
nameserver 10.202.10.102"""

change_dns_linux(dns_servers)
