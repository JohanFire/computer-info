import os
import psutil

from utils import cpu, ip, mac

def main():
    try:
        os.system('cls')
    except:
        pass

    print('\n' + '=' * 50)
    print('\t\tComputer information')
    print('=' * 50)
    print('\n' + '=' * 20 + ' Main Info ' + '=' * 19)
    ip.get_ipv4_address()
    mac.get_mac()
    print('-----')
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f'Logical processors (total CPU cores): {os.cpu_count()}')
    print('-----')
    print(f'RAM memory used: {psutil.virtual_memory()[2]}% ')
    print(f'RAM used (GB): {psutil.virtual_memory()[3]/1000000000}')
    print()
    print('=' * 20 + ' CPU Info ' + '=' * 20)
    cpu.cpu_cores()
    cpu.cpu_frequencies()
    cpu.cpu_usage()

if __name__ == '__main__':
    main()