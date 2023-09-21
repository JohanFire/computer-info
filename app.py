import os
import psutil

from utils import mac, ip

print('\n' + '=' * 50)
print('\t\tComputer information')
print('=' * 50)
print('=' * 20 + ' Main Info ' + '=' * 19)
ip.get_ipv4_address()
mac.get_mac()
print('-----')
print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
print(f'Logical processors (CPU cores count): {os.cpu_count()}')
print('-----')
print(f'RAM memory used: {psutil.virtual_memory()[2]}% ')
print(f'RAM used (GB): {psutil.virtual_memory()[3]/1000000000}')
print('-----')

print('==============================================\n')