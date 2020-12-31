#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  This program is free software;
#  Author: A1andNS
import json
import socket
import time


def scan_once(ip, tmp_type):
    tmp_type = tmp_type
    f = open("./config/config.json")
    content = f.read()
    content_json = json.loads(content)
    for ports_json in content_json['ports']:
        # print(ports_json['title'])
        if ports_json['title'] == tmp_type:
            print("Start Xport 0.1#dev at "+time.strftime("%Y-%m-%d %H:%M:%S CST", time.localtime()))
            ports = ports_json['value'].split(',')
            # print(ports)
            for port in ports:
                try:
                    s = socket.socket()
                    s.settimeout(3)
                    s.connect((ip, int(port)))
                    print("[+]" + str(port) + "端口存在")
                except socket.timeout:
                    print("Host is not open")
                    break
                    # continue
                s.close()


if __name__ == "__main__":
    scan_once("127.0.0.1", "General")
