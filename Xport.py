#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  This program is free software;
#  Author: A1andNS
from lib.copyright import *
from lib.scanonce import *


def XScan():
    ip = socket.gethostbyname(input("请输入目标IP地址或url:"))
    print("请输入你要扫描的端口范围:\n1.全部端口\n2.常用端口\n3.企业常见端口\n4.精简端口\n5.咖啡厅/酒店/机场常见端口\n6.数据库端口\n\
7.SCADA/ICS\n8.物联网\n9.Backdoor Check")
    target = input("请选择你的扫描范围:")
    if int(target) == 1:
        # 全部端口扫描
        for port in range(1, 65536):
            try:
                s = socket.socket()
                s.settimeout(3)
                s.connect((ip, port))
                print("[+]" + str(port) + "端口存在")
            except Exception:
                continue
            s.close()
    elif int(target) == 2:
        # 常用端口扫描
        scan_once(ip, "General")
    elif int(target) == 3:
        # 企业常见端口
        scan_once(ip, "Enterprise")
    elif int(target) == 4:
        # 精简端口
        scan_once(ip, "Minimal")
    elif int(target) == 5:
        # 咖啡厅/酒店/机场常见端口
        scan_once(ip, "Coffee Bar/Hotel/Airport")
    elif int(target) == 6:
        # 数据库端口
        scan_once(ip, "Database")
    elif int(target) == 7:
        # SCADA/ICS
        scan_once(ip, "SCADA/ICS")
    elif int(target) == 8:
        # 物联网
        scan_once(ip, "IoT")
    elif int(target) == 9:
        # Backdoor Check
        scan_once(ip, "Backdoor Check")
    else:
        scan_once(ip, "General")


if __name__ == "__main__":
    show_logo()
    XScan()
