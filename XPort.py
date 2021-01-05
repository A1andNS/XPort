#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  This program is free software;
#  Author: A1andNS
from lib.copyright import *
from lib.scan_tcp import *
from lib.scan_udp import *


def XScan():
    try:
        ip = socket.gethostbyname(input("请输入目标IP地址或URL:"))
        try:
            print("提供的端口扫描方式:\n1.TCP\n2.UDP")
            scan_type = input("请选择你的扫描方式:")
            if int(scan_type) == 1:
                print("提供的端口范围:\n1.全部端口\n2.常用端口\n3.企业常见端口\n4.精简端口\n5.咖啡厅/酒店/机场常见端口\n6.数据库端口\n\
7.SCADA/ICS\n8.物联网\n9.Backdoor Check")
                target = input("请选择你的扫描范围:")
                try:
                    if int(target) == 1:
                        # 全部端口扫描
                        scan_tcp(ip, "All")
                    elif int(target) == 2:
                        # 常用端口扫描
                        scan_tcp(ip, "General")
                    elif int(target) == 3:
                        # 企业常见端口
                        scan_tcp(ip, "Enterprise")
                    elif int(target) == 4:
                        # 精简端口
                        scan_tcp(ip, "Minimal")
                    elif int(target) == 5:
                        # 咖啡厅/酒店/机场常见端口
                        scan_tcp(ip, "Coffee Bar/Hotel/Airport")
                    elif int(target) == 6:
                        # 数据库端口
                        scan_tcp(ip, "Database")
                    elif int(target) == 7:
                        # SCADA/ICS
                        scan_tcp(ip, "SCADA/ICS")
                    elif int(target) == 8:
                        # 物联网
                        scan_tcp(ip, "IoT")
                    elif int(target) == 9:
                        # Backdoor Check
                        scan_tcp(ip, "Backdoor Check")
                    else:
                        # Default Port
                        print("找不到目标范围，使用默认范围")
                        scan_tcp(ip, "General")
                except ValueError:
                    print("请输入正确的序号，例如选择所有端口就输入1")
            elif int(scan_type) == 2:
                print("提供的端口范围:\n1.全部端口\n2.企业常见端口\n3.精简端口\n4.咖啡厅/酒店/机场常见端口\n5.SCADA/ICS")
                target = input("请选择你的扫描范围:")
                try:
                    if int(target) == 1:
                        # 全部端口扫描
                        scan_udp(ip, "All")
                    elif int(target) == 2:
                        # 企业常见端口
                        scan_udp(ip, "Enterprise")
                    elif int(target) == 3:
                        # 精简端口
                        scan_udp(ip, "Minimal")
                    elif int(target) == 4:
                        # 咖啡厅/酒店/机场常见端口
                        scan_udp(ip, "Coffee Bar/Hotel/Airport")
                    elif int(target) == 5:
                        # SCADA/ICS
                        scan_udp(ip, "SCADA/ICS")
                    else:
                        # Default Port
                        print("找不到目标范围，使用默认范围")
                        scan_udp(ip, "Enterprise")
                except ValueError:
                    print("请输入正确的序号，例如选择所有端口就输入1")
            else:
                print("请输入正确的序号，例如选择所有端口就输入1")
        except ValueError:
            print("请输入正确的序号，例如使用TCP方式就输入1")
    except socket.gaierror as e:
        print(e)
        print("正确输入格式为:127.0.0.1或www.baidu.com")


if __name__ == "__main__":
    show_logo()
    XScan()
