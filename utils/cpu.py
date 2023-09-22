import os
import psutil

def cpu_cores():
    # number of cores
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f'Logical processors (total CPU cores): {os.cpu_count()}')

def cpu_frequencies():
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

def cpu_usage():
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def main():
    pass

if __name__ == '__main__':
    main()