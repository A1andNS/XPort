#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  This program is free software;
#  Author: A1andNS

import os
import re


def ttl_scan(ip):
    ttlstrmatch = re.compile(r'ttl=\d+')
    ttlnummatch = re.compile(r'\d+')
    result = os.popen("ping -c 1 " + ip)
    res = result.read()
    for line in res.splitlines():
        match_result = ttlstrmatch.findall(line)
        if match_result:
            ttl = ttlnummatch.findall(match_result[0])
            if int(ttl[0]) <= 64:
                return 1
            else:
                return 2
        else:
            pass


if __name__ == "__main__":
    ttl_scan('192.168.184.131')
