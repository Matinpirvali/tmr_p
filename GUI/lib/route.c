#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// for linux

#ifdef __linux__
    const char* os = "Linux";
    const char* interface = "eth0";
    
    // DNS جدید را تعیین کنید
    const char* dnsServer = "8.8.8.8";
    
    char command[100];
    sprintf(command, "echo nameserver %s | sudo tee /etc/resolv.conf > /dev/null", dnsServer);

    int result = system(command);

    if (result == 0) {
        // DNS CHANGE
    } else {
        // DNS NOt CHANGe
    }

    return 0;
#elif _WIN32
    #include <windows.h>
    const char* os = "Windows";
    const char* dnsServer = "8.8.8.8";
    
    char command[100];
    sprintf(command, "netsh interface ip set dns name=\"Wi-Fi\" static %s", dnsServer);

    int result = system(command);

    if (result == 0) {
        // DNS CHANGE
    } else {
        // DNS NOt CHANGe
    }
#else
    const char* os = "Script not supoert Your OS";
#endif

int main() {
    
    return 0;
}
