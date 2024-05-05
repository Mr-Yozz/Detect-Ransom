import hashlib
import os
from load import loading
import pyfiglet

global file

def read_text_file(file_path):
    """Read the content of a text file and return as a list of lines."""
    with open(file_path, 'r') as file:
        return file.readlines()
    
# Example usage:
md5_hash = 'hash.txt'  # Replace 'data.txt' with your file path
# sha256_hash = 'sha256.txt'
md5 = read_text_file(md5_hash) 
# sha256 = read_text_file(sha256_hash)
lines = md5 
data_list = [line.strip() for line in lines]
# print(data_list)

def calculate_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5  = hashlib.md5()
    # hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
            # hash_sha256.update(chunk)
    # print(hash_md5.hexdigest())
    md5 = hash_md5.hexdigest()
    # sha = hash_sha256.hexdigest()
    data = md5 
    return data
    

def scan_for_ransomware(directory, ransomware_signatures):
    """Scan the specified directory for files matching known ransomware signatures."""
    ransomware_files = []
    print(pyfiglet.print_figlet(text="RANSOMWARE SCANING",font="standard",colors="red"))
    loading()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            file_hash = calculate_hash(file_path)
            # print(ransomware_signatures)
            if file_hash in ransomware_signatures:
                print("\033[31m"f"-------------------RANSOMWARE DETECTED---------------------------:\n {file_path}")
                ransomware_files.append(file_path)
    # Pylance: ignore=unused-variable
    return ransomware_files

# def path_input():
#     directory_to_scan = input("\033[32m" "scan_for_ransomware : Enter Your Path or Directory ")
#     return directory_to_scan

def detect_ransomware(path_input):

    directory_to_scan = path_input
    
    # Perform the scan
    detected_ransomware_files = scan_for_ransomware(directory_to_scan, data_list)

    # Print the results
    if detected_ransomware_files:
        print(pyfiglet.print_figlet(text="\n SCANING PATH AND DISPLAY HASH & FILEPATH",font="short",colors="blue"))
        
        for root, dirs, files in os.walk(directory_to_scan):
            for file in files:
                file_path = os.path.join(root, file)
                print("\033[32m"+ file_path )
                file_hash = calculate_hash(file_path)
                print("\033[32m"+ file_hash)
    else:
        print(pyfiglet.print_figlet(text="NO RANSOMWARE DETECTED",font="standard",colors="blue"))
    return directory_to_scan


# if __name__ == "__main__":
#     detect_ransomware()