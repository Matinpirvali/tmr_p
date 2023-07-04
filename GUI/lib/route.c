// #include <Windows.h>
// #include <WinDNS.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if defined(_WIN32)
    const char* os = "Windows";
#elif defined(__linux__)
    const char* os = "Linux";
    const char letter = '\0';  // Null character, won't print anything
#else
    const char* os = "Unknown";
    const char letter = '\0';  // Null character, won't print anything
#endif

int main() {
    printf("Operating System: %s\n", os);
    
    if (os == 'Windows') {
        // #include <Windows.h>
        // #include <WinDNS.h>

        // Specify the DNS server addresses you want to use
        // const char* dnsServerAddress1 = "122.122.222.222";
        // const char* dnsServerAddress2 = "112.332.121.222";

        // // Set the DNS server addresses
        // DNS_ADDR dnsServers[2];
        // dnsServers[0].MaxCount = 1;
        // dnsServers[0].AddrArray[0].ipAddr.s_addr = inet_addr(dnsServerAddress1);
        // dnsServers[0].AddrArray[0].Sockaddr.sin_family = AF_INET;
        // dnsServers[0].AddrArray[0].Sockaddr.sin_port = 0;
        // dnsServers[1].MaxCount = 1;
        // dnsServers[1].AddrArray[0].ipAddr.s_addr = inet_addr(dnsServerAddress2);
        // dnsServers[1].AddrArray[0].Sockaddr.sin_family = AF_INET;
        // dnsServers[1].AddrArray[0].Sockaddr.sin_port = 0;

        // // Get the current DNS settings
        // DWORD adapterIndex = 0;  // Use 0 for the first network adapter
        // PIP4_ARRAY currentDnsServers = NULL;
        // DWORD result = DnsQueryConfig(DnsConfigDnsServerList, FALSE, NULL, NULL, NULL, &currentDnsServers);
        // if (result == ERROR_SUCCESS && currentDnsServers->AddrCount > adapterIndex) {
        //     printf("Current DNS servers:\n");
        //     for (DWORD i = 0; i < currentDnsServers->AddrCount; i++) {
        //         printf("%s\n", inet_ntoa(currentDnsServers->AddrArray[i]));
        //     }
        // }

        // // Set the new DNS servers
        // result = DnsSetPrimaryDomainName_W(NULL, NULL);
        // if (result == ERROR_SUCCESS) {
        //     result = DnsSetDnsServerConfig(dnsServers, 2);
        //     if (result == ERROR_SUCCESS) {
        //         printf("DNS servers changed successfully to:\n");
        //         printf("%s\n", dnsServerAddress1);
        //         printf("%s\n", dnsServerAddress2);
        //     }
        // }

        // // Clean up
        // if (currentDnsServers != NULL) {
        //     DnsFree(currentDnsServers);
        // }

        // return 0;

    } else if (os = "Linux") {
        #define RESOLV_CONF_PATH "/etc/resolv.conf"

        const char* dnsServers[] = {
            "122.122.222.222",
            "112.332.121.222"
        };
        const int numDnsServers = sizeof(dnsServers) / sizeof(dnsServers[0]);

        FILE* fp = fopen(RESOLV_CONF_PATH, "w");
        if (fp == NULL) {
            perror("Failed to open resolv.conf");
            return 1;
        }

        // Write the nameserver entries to resolv.conf
        for (int i = 0; i < numDnsServers; i++) {
            fprintf(fp, "nameserver %s\n", dnsServers[i]);
        }

        fclose(fp);

        printf("DNS servers changed successfully.\n");

        // Read and display the updated resolv.conf file
        fp = fopen(RESOLV_CONF_PATH, "r");
        if (fp != NULL) {
            char line[256];
            while (fgets(line, sizeof(line), fp) != NULL) {
                printf("%s", line);
            }
            fclose(fp);
        }

        // Restart the network service to apply the changes
        system("service networking restart");

        return 0;
    }
    
    
    return 0;
}
