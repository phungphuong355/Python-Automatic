#!/bin/bash

tail /var/log/syslog

tail /var/log/syslog | cut -d' ' -f5-

cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head