#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <resolv.h>

// for linux

#ifdef __linux__
    
    res_init();
    res_state res = malloc(sizeof(struct __res_state));
    int result = res_ninit(res);

    if (result == 0) {
        // تنظیم DNS جدید
        const char *dns1 = "8.8.8.8";
        const char *dns2 = "8.8.4.4";
        res->nscount = 2;
        res->nsaddr_list[0].sin_family = AF_INET;
        res->nsaddr_list[0].sin_addr.s_addr = inet_addr(dns1);
        res->nsaddr_list[1].sin_family = AF_INET;
        res->nsaddr_list[1].sin_addr.s_addr = inet_addr(dns2);
        
        printf("DNS سیستم با موفقیت تغییر یافت.\n");
    } else {
        printf("خطا در تغییر DNS سیستم.\n");
    }
    free(res);
    



#elif _WIN32
    #include <windns.h>

    #include <windows.h>

    IP4_ARRAY dnsServers;
    dnsServers.AddrCount = 2;  // تعداد DNS سرورها

    // آدرس‌های DNS سرورها را مشخص کنید
    char* dnsServerAddresses[] = {
        "8.8.8.8",   // DNS سرور اول
        "8.8.4.4"    // DNS سرور دوم
    };

    // تخصیص حافظه برای آدرس‌های DNS سرورها
    dnsServers.Address[0].sin_family = AF_INET;
    dnsServers.Address[0].sin_addr.s_addr = inet_addr(dnsServerAddresses[0]);
    dnsServers.Address[1].sin_family = AF_INET;
    dnsServers.Address[1].sin_addr.s_addr = inet_addr(dnsServerAddresses[1]);

    // اعمال تغییرات DNS
    DWORD result = DnsAcquireContextHandle(0, NULL);
    if (result == 0)
    {
        printf("Failed to acquire DNS context handle.\n");
        return 1;
    }

    result = DnsSetDnsServerAddresses(&dnsServers, 0);
    if (result == 0)
    {
        printf("Failed to set DNS server addresses.\n");
        return 1;
    }

    printf("DNS servers changed successfully.\n");

    return 0;


#else
    const char* os = "Script not supoert Your OS";
#endif