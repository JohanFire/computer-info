# Python Program to Get IP Address
import socket

def get_ipv4_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print(f"Computer Name: {hostname}")
    print(f"IPv4 Address: {IPAddr}")

    return IPAddr