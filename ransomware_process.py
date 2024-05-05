from detection import *
from monitoring import *

def is_ransomware_process(process):
    # Implement logic to identify ransomware-like behavior based on process attributes
    # For demonstration, we'll assume any process with ".exe" extension is suspicious

    return ".exe" in process.name().lower()

def ransom_process():
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        
        # Check for processes exhibiting ransomware-like behavior
        if is_ransomware_process(proc):
            print(f"Potential ransomware process detected: {proc.pid} - {proc.name()} - {proc.exe()}")
            file = proc.exe()
            # print(file)
            hash = calculate_hash(file)
            # print(hash)
            
            if hash in data_list == True :
                print(f"path - {hash==data_list} - Potential ransomware process detected in C disk")
                # print(hash == sign)
        else:
            print(pyfiglet.print_figlet(text="NO RANSOMWARE DETECTED",font="standard",colors="blue"))
            print("\033[1;34m" "NO RANSOMWARE DETECTED IN YOUR FILES ")
            break

