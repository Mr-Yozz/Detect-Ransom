import os
import time
import shutil
from load import loading
import pyfiglet

def check_backup_status(backup_directory):
    
    print(pyfiglet.print_figlet(text="CHECKING BACKUP STATUS",font="standard",colors="blue"))
    if os.path.exists(backup_directory):
        backup_files = os.listdir(backup_directory)
        if backup_files:
            latest_backup = max(backup_files, key=lambda f: os.path.getmtime(os.path.join(backup_directory, f)))
            backup_size = sum(os.path.getsize(os.path.join(backup_directory, f)) for f in backup_files)
            backup_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(os.path.join(backup_directory, latest_backup))))
            print("\033[1;32m"f"Latest Backup: {latest_backup}")
            print("\033[1;32m"f"Backup Size: {backup_size / (1024 * 1024):.2f} MB")
            print("\033[1;32m"f"Backup Date: {backup_date}")
        else:
            print("\033[1;31;40m No backup files found in the backup directory \033[0m")
    else:
        print("\033[1;31;40m Backup directory does not exist \033[0m")

# Example usage
# check_backup_status()

def backup_file_or_directory(source, destination):
    try:
        # Check if the source exists
        if not os.path.exists(source):
            print("\033[1;31;40m Source does not exist." "\033[0m")
            return

        # Create destination directory if it doesn't exist
        os.makedirs(destination, exist_ok=True)
        loading()
        # Check if the source is a file or directory
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print("\033[1;34m"f"File '{source}' backed up successfully to '{destination}'.")
            check_backup_status(source)
        elif os.path.isdir(source):
            shutil.copytree(source, os.path.join(destination, os.path.basename(source)))
            print("\033[1;34m"f"Directory '{source}' backed up successfully to '{destination}'.")
            check_backup_status(source)
        else:
            print("\033[1;31;40m Invalid source type. Please provide a valid file or directory. \033[0m")
    except Exception as e:
        print("\033[1;31;40m "f"Error occurred while backing up: {e}" "\033[0m")



def backup():
    
        source_path = input("\033[1;92m Enter Your Source Path: \033[0m")  # Replace with the path of the file or directory you want to backup
        destination_path = input("\033[1;92m Enter Your destination Path: \033[0m")  # Replace with the path where you want to store the backup
        backup_file_or_directory(source_path, destination_path)


