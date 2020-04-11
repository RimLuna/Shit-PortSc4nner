#!/usr/bin/python

import sys
from socket import *

def get_ip(str):

    ipstrip = str[1].strip()
    if ipstrip.find('https://') != -1 or ipstrip.find('http://') != -1:
        print("Remove http/https")
        exit(2)
    split = ipstrip.split('.')
    if len(split) == 4:
        for khra in ipstrip.split('.'):
            if not khra.isdigit():
                print('Invalid IP')
                exit(3)
        return ipstrip
    elif len(split) == 2 and not split[1].isdigit():
        return gethostbyname(ipstrip)
    elif len(split) == 3 and not split[2].isdigit():
        return gethostbyname(ipstrip)
    else:
        print('Invalid argument')
        exit(4)

def get_port(str):
    port = str[2]
    if not port.isdigit():
        print("Port format is wrong")
        exit(6)
    return int(port)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python scan.py ipaddr portrange')
        sys.exit(1)
    open_ports = []
    ipaddr = get_ip(sys.argv)
    port_range = sys.argv[2]
    ports = port_range.split('-')
    if len(ports) <= 1:
        if not ports[0].strip().isdigit():
            print('Port format is wrong')
            exit(8)
        print(f'{ipaddr} : scanning {port_range}..')
        port = int(port_range)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        if sock.connect_ex((ipaddr, port)) == 0:
            open_ports.append(port)
    else:    
        if not ports[0].strip().isdigit() or not ports[1].strip().isdigit():
            print('Port format is wrong')
            exit(8)
        start_port = int(ports[0])
        end_port = int(ports[1])
        for port in range(start_port, end_port):
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(5)
            if sock.connect_ex((ipaddr, port)) == 0:
                open_ports.append(port)
    
    print('PORT\tSTATE')
    for i in open_ports:
        print(f'{i}\topen')
