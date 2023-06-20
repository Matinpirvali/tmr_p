#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// for linux

int main() {
    const char* interface = "eth0";
    
    // DNS جدید را تعیین کنید
    const char* dnsServer = "8.8.8.8";
    
    char command[100];
    sprintf(command, "echo nameserver %s | sudo tee /etc/resolv.conf > /dev/null", dnsServer);

    int result = system(command);

    if (result == 0) {
       // start
    } else {
      // exit
    }

    return 0;
}
