# To change the system DNS settings using Python, you can use the pyroute2 library, which
# provides a Pythonic interface for network configuration. Here's an example of how you can change the DNS settings:

# First, make sure you have the pyroute2 library installed. You can install it using pip:
# pip install pyroute2

# Then, you can use the following code to change the system DNS settings:
from pyroute2 import IPRoute

def change_dns_servers(interface, dns_servers):
    ip = IPRoute()
    index = ip.link_lookup(ifname=interface)[0]
