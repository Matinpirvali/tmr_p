#include <Windows.h>
#include <WinDNS.h>
#include <stdio.h>

int main() {
    // Specify the DNS server addresses you want to use
    const char* dnsServerAddress1 = "122.122.222.222";
    const char* dnsServerAddress2 = "112.332.121.222";

    // Set the DNS server addresses
    DNS_ADDR dnsServers[2];
    dnsServers[0].MaxCount = 1;
    dnsServers[0].AddrArray[0].ipAddr.s_addr = inet_addr(dnsServerAddress1);
    dnsServers[0].AddrArray[0].Sockaddr.sin_family = AF_INET;
    dnsServers[0].AddrArray[0].Sockaddr.sin_port = 0;
    dnsServers[1].MaxCount = 1;
    dnsServers[1].AddrArray[0].ipAddr.s_addr = inet_addr(dnsServerAddress2);
    dnsServers[1].AddrArray[0].Sockaddr.sin_family = AF_INET;
    dnsServers[1].AddrArray[0].Sockaddr.sin_port = 0;

    // Get the current DNS settings
    DWORD adapterIndex = 0;  // Use 0 for the first network adapter
    PIP4_ARRAY currentDnsServers = NULL;
    DWORD result = DnsQueryConfig(DnsConfigDnsServerList, FALSE, NULL, NULL, NULL, &currentDnsServers);
    if (result == ERROR_SUCCESS && currentDnsServers->AddrCount > adapterIndex) {
        printf("Current DNS servers:\n");
        for (DWORD i = 0; i < currentDnsServers->AddrCount; i++) {
            printf("%s\n", inet_ntoa(currentDnsServers->AddrArray[i]));
        }
    }

    // Set the new DNS servers
    result = DnsSetPrimaryDomainName_W(NULL, NULL);
    if (result == ERROR_SUCCESS) {
        result = DnsSetDnsServerConfig(dnsServers, 2);
        if (result == ERROR_SUCCESS) {
            printf("DNS servers changed successfully to:\n");
            printf("%s\n", dnsServerAddress1);
            printf("%s\n", dnsServerAddress2);
        }
    }

    // Clean up
    if (currentDnsServers != NULL) {
        DnsFree(currentDnsServers);
    }

    return 0;
}
