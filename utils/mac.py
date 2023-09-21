import psutil
import uuid
import re

def get_mac():
    # joins elements of getnode() after each 2 digits.
    print ("MAC address: ", end="")
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

def get_mac_easier():
    # joins elements of getnode() after each 2 digits.
    # using regex expression
    print ("The MAC address in formatted and less complex way is : ", end="")
    print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
    
def get_mac_devices():
    """ get the MAC addresses of all the network interfaces on the computer """
    # Iterate over all the keys in the dictionary
    for interface in psutil.net_if_addrs():
        # Check if the interface has a valid MAC address
        if psutil.net_if_addrs()[interface][0].address:
            # Print the MAC address for the interface
            print(psutil.net_if_addrs()[interface][0].address)
            break