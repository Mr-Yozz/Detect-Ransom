import psutil
import time
import os
import socket
from detection import *


def monitor_system_activity():
    # Monitor file system events

    event = psutil.disk_io_counters(perdisk=True,nowrap=True)
    for events, io in event.items():
        # Check for patterns indicating mass file encryption            
            if 'read_bytes' in io._fields:
                read_bytes = io.read_bytes
                print("\033[1;32m" f"Disk {events}: Read bytes: {read_bytes}")
            else:
                print("\033[1;31m" f"Disk {events}: No Read bytes availble")

    for events, io in event.items():
        # Check for patterns indicating mass file encryption            
            if 'write_bytes' in io._fields:
                write_bytes = io.write_bytes
                print("\033[1;32m" f"Disk {events}: Write bytes: {write_bytes}")
            else:
                print("\033[1;31m" f"Disk {events}: No write bytes availble")
    # print("Possible file encryption activity detected!")

# Monitor network activity
def network():
    net = psutil.net_connections()
    for conn in net:
        # Check for connections to known malicious domains
        print("-------------------SCANING NETWORKS---" "\033[1;31m" "STOP[CTRL+C]" "\033[0m" "------------------------")
        if conn.raddr and "https://www.urlvoid.com/scan/" in conn.raddr:
            add=conn.raddr
            remort_ip, remort_port = add
            print("\033[31m" f"Local Address: {conn.laddr}, Remort Address: {remort_ip}:{remort_port}")
            print("\033[31m""Connection to a known malicious domain detected!")
        else:
            print("\033[31m""Not Detected Malicious Domain")
            break

def run():
    try:
        while True:
            monitor_system_activity()
            network()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\033[1;31;40m" "STOP: Scaning", "\033[0m")


     

    
# if __name__ == "__main__":
#     run()
