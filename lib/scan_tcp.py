#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  This program is free software;
#  Author: A1andNS
import json
import os
import socket
import time
import threading


def scan_tcp(ip, tmp_type):
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
        print("Scan Type: TCP")
        fd.write("Scan Type: TCP")
        for port in range(1, 65536):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((ip, port))
                print("[+] TCP " + str(port) + "端口存在")
                fd.write("[+] TCP " + str(port) + "端口存在\n")
                s.close()
            except socket.timeout:
                print("[-]Host is not open")
                fd.write("[-]Host is not open\n")
                break
            except ConnectionRefusedError:
                continue
    else:
        f = open("./config/config.json")
        content = f.read()
        content_json = json.loads(content)
        for ports_json in content_json['ports_tcp']:
            # print(ports_json['title'])
            if ports_json['title'] == tmp_type:
                print("Start XPort 0.3#stable at " + start_time)
                fd.write("Start XPort 0.3#stable at " + start_time + "\n")
                print("XPort scan report for " + ip)
                fd.write("XPort scan report for " + ip + "\n")
                print("Scan Type: TCP")
                fd.write("Scan Type: TCP")
                ports = ports_json['value'].split(',')
                for port in ports:
                    try:
                        s = socket.socket()
                        s.settimeout(3)
                        s.connect((ip, int(port)))
                        # s.recv(1024)  #如果接收显示信息，那么有可能出现端口开放但是不会回送信息的情况，那么就有可能回报出timeout，无法清晰判断端口时候开放。
                        print("[+] " + str(port) + "端口存在")
                        fd.write("[+] " + str(port) + "端口存在\n")
                        s.close()
                    except socket.timeout:       # timeout只有在目标ip访问不了的时候才会报
                        print("[-]Host seems down")
                        fd.write("[-]Host seems down\n")
                        break
                    except ConnectionRefusedError:             # 这里使用连接被拒绝来作为端口关闭
                        continue
    time_end = time.time()
    print("The Scan is finished in {:.2f}s".format(time_end - time_start))
    fd.write("The Scan is finished in {:.2f}s".format(time_end - time_start) + "\n")
    fd.close()


if __name__ == "__main__":
    scan_tcp("127.0.0.1", "General")
