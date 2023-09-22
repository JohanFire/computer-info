import psutil

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def memory_info():
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Used percentage: {svmem.percent}%")
    
    result = [get_size(svmem.total), get_size(svmem.available), get_size(svmem.used), f'{svmem.percent}%']

    return 

def swap_info():
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Used percentage: {swap.percent}%")
    
    result = [get_size(swap.total), get_size(swap.free), get_size(swap.used),  f'{get_size(swap.percent)}%']
    
    return result

def main():
    pass

if __name__ == '__main__':
    main()