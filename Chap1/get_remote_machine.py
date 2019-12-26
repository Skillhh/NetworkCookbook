#!/usr/bin/python3

import socket

def get_remote_machine():
    remote_host = 'www.python.org'
    try:
        remote_ip = socket.gethostbyname(remote_host)
        print("IP address of %s is %s" %( remote_host, remote_ip))
    except socket.gaierror as err_msg:
        print("{}: {}".format(remote_host, err_msg))

if __name__ == "__main__":
    get_remote_machine()
