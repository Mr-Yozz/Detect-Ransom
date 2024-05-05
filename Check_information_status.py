import subprocess
import platform
import pyfiglet
import time
import psutil
import winreg

def check_system_information():
    print(pyfiglet.print_figlet(text="SYSTEM INFORMATION",font="standard",colors="blue"))
    print("\033[32m" "OS:", platform.system(), platform.release())
    print("\033[32m" "Hostname:", platform.node())
    print("\033[32m" "Processor:", platform.processor())

    # Get system uptime
    uptime = time.time() - psutil.boot_time()
    print("\033[32m" f"System Uptime: {uptime / 3600:.2f} hours")


    # CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    print("\033[32m" f"CPU Usage: {cpu_usage}%")
    print("\033[32m" f"Memory Usage: {memory_usage}%")

    # Disk usage
    disk_usage = psutil.disk_usage('/')
    print("\033[32m" f"Disk Usage - Total: {disk_usage.total / (1024**3):.2f} GB, "
          f"Used: {disk_usage.used / (1024**3):.2f} GB, "
          f"Free: {disk_usage.free / (1024**3):.2f} GB")

def check_firewall_status():
    print(pyfiglet.print_figlet(text="CHECKING FIREWALL STATUS",font="standard",colors="blue"))
    if platform.system() == "Windows":
        firewall_status = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
        print(firewall_status.stdout)
    elif platform.system() == "Linux":
        firewall_status = subprocess.run(["iptables", "-L"], capture_output=True, text=True)
        print(firewall_status.stdout)
    else:
        print(pyfiglet.print_figlet(text="NO FIREWALL DETECTED",font="short",colors="blue"))

def get_antivirus():
    try:
        antivirus_list = []
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
            for i in range(1024):  # Arbitrarily chosen limit
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            if "antivirus" in name.lower() or "security" in name.lower():
                                antivirus_list.append(name)
                        except FileNotFoundError:
                            continue
                except OSError:
                    break
        if antivirus_list:
            print(pyfiglet.print_figlet(text="ANTIVIRUS SOFTWARE FOUND",font="standard",colors="blue"))
            print("\033[1;34m" )
            for antivirus in antivirus_list:
                print(antivirus)
        else:
            print("\033[1;31;40m" "No antivirus software found.""\033[0m")
    except Exception as e:
        print("\033[1;31;40m""Error:", e + "\033[0m")


def Check():
    check_system_information()
    check_firewall_status()
    get_antivirus()

    
# if __name__ == "__main__":
#     main()
