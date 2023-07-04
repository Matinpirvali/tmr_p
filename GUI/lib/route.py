
## ----Linux---- ##
# import subprocess

# def change_dns_linux(dns_servers):
#     # Concatenate the DNS server addresses into a single string

#     # Execute the system command to change DNS servers
#     command = f'sudo sh -c "echo nameserver {dns_servers} > /etc/resolv.conf"'
#     result = subprocess.run(command, shell=True)

#     if result.returncode == 0:
#         print("DNS servers changed successfully.")
#     else:
#         print("Failed to change DNS servers.")

# # Specify the DNS server addresses you want to set
# dns_servers = """nameserver 10.202.10.202
# nameserver 10.202.10.102"""

# change_dns_linux(dns_servers)

## ----Windows---- ##
import win32com.shell.shell as shell
import win32com.shell.shellcon as shellcon

def set_dns_servers(dns_servers):
    # دریافت مدیریت تنظیمات شبکه
    net_shell = shell.Dispatch("NetworkConnections")
    connections = net_shell.Query("SELECT * FROM Win32_NetworkAdapter WHERE NetConnectionStatus = 2")

    for connection in connections:
        # دریافت مدیریت تنظیمات شبکه برای هر اتصال
        net_connection_id = connection.NetConnectionID
        net_connection = shell.Dispatch("HNetCfg.HNetShare.1")
        connections = net_connection.EnumEveryConnection()

        for connection in connections:
            connection = net_connection.NetConnectionProps(connection)
            if connection.Name == net_connection_id:
                # دریافت تنظیمات DNS فعلی برای اتصال
                dns_list = connection.IPv4Settings.DNSServerSearchOrder

                # تنظیم تنظیمات DNS جدید
                connection.IPv4Settings.DNSServerSearchOrder = dns_servers
                connection.Put_()

                print(f"DNS servers changed for {connection.Name}")

dns_servers = ["178.22.122.100", "185.51.200.2"]  # لیست DNS سرورهای جدید

set_dns_servers(dns_servers)
