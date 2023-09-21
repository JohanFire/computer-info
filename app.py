import os
import psutil
import uuid

print('\n==============================================')
print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
print(f'Logical processors (CPU cores count): {os.cpu_count()}')
print('-----')
print(f'RAM memory used: {psutil.virtual_memory()[2]}% ')
print(f'RAM used (GB): {psutil.virtual_memory()[3]/1000000000}')
print('-----')
# printing the value of unique MAC
# address using uuid and getnode() function
print (hex(uuid.getnode()))
print('==============================================\n')