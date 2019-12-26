#!/usr/bin/python3

import socket

def get_remote_machine():
    remote_host = 'www.python.org'
    remote_ip = socket.gethostbyname(remote_host)
    try:
        print("IP address of %s is %s" %( remote_host, remote_ip))
    except socket.error as err_msg:
        print("%s: %s" %(remote_host, err_msg))

if __name__ == "__main__":
    get_remote_machine()
