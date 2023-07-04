import wmi

def change_dns(server_list):
    # Connect to the WMI interface
    c = wmi.WMI()

    # Find the network adapter configuration
    network_config = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # Iterate over each network adapter
    for config in network_config:
        # Set the DNS server list
        return_value = config.SetDNSServerSearchOrder(server_list)
        
        # Check the return value
        if return_value[0] == 0:
            print(f"DNS settings updated for interface: {config.Description}")
        else:
            print(f"Failed to update DNS settings for interface: {config.Description}")

# Specify the DNS servers you want to set
dns_servers = ["8.8.8.8", "8.8.4.4"]

# Call the function to change the DNS settings
change_dns(dns_servers)
