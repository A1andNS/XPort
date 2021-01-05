#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  This program is free software;
#  Author: A1andNS
import json
import os
import time
from lib.is_alive import *


def scan_udp(ip, tmp_type):
    time_start = time.time()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S CST", time.localtime())
    filename = "result-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".log"
    if not os.path.exists("./log/"):
        os.mkdir("./log")
    fd = open("./log/" + filename, "w")
    if tmp_type == "All":
        print("Start XPort 0.3#stable at " + start_time)
        fd.write("Start XPort 0.3#stable at " + start_time + "\n")
        print("XPort scan report for " + ip)
        fd.write("XPort scan report for " + ip + "\n")
        print("Scan Type: UDP")
        fd.write("Scan Type: UDP\n")
        if is_alive(ip):
            for port in range(1, 65536):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.settimeout(3)
                    s.sendto(b'test', (ip, port))
                    s.recvfrom(1024)
                    print("[+] UDP " + str(port) + "端口存在")
                    fd.write("[+] UDP " + str(port) + "端口存在" + "\n")
                    s.close()
                except socket.timeout:
                    continue
        else:
            print("[-]Host seems down")
            fd.write("[-]Host seems down\n")
    else:
        f = open("./config/config.json")
        content = f.read()
        content_json = json.loads(content)
        for ports_json in content_json['ports_udp']:
            # print(ports_json['title'])
            if ports_json['title'] == tmp_type:
                print("Start XPort 0.3#stable at " + start_time)
                fd.write("Start XPort 0.3#stable at " + start_time + "\n")
                print("XPort scan report for " + ip)
                fd.write("XPort scan report for " + ip + "\n")
                print("Scan Type: UDP")
                fd.write("Scan Type: UDP\n")
                ports = ports_json['value'].split(',')
                if is_alive(ip):
                    print("[+]Host is UP")
                    fd.write("[+]Host is UP\n")
                    for port in ports:
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            s.settimeout(3)
                            s.sendto(b'test', (ip, int(port)))
                            s.recvfrom(1024)
                            print("[+] UDP " + str(port) + "端口存在")
                            fd.write("[+] UDP " + str(port) + "端口存在" + "\n")
                            s.close()
                        except socket.timeout:
                            continue
                else:
                    print("[-]Host seems down")
                    fd.write("[-]Host seems down\n")
    time_end = time.time()
    print("The Scan is finished in {:.2f}s".format(time_end - time_start))
    fd.write("The Scan is finished in {:.2f}s".format(time_end - time_start) + "\n")
    fd.close()


if __name__ == "__main__":
    scan_udp("127.0.0.1", 6000)
