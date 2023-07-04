#!/bin/bash

# Specify the DNS server addresses
dns_servers=("8.8.8.8" "8.8.4.4")

# Iterate over each DNS server and set it using netsh
for server in "${dns_servers[@]}"
do
    netsh interface ip set dns name="Local Area Connection" static $server primary
done
