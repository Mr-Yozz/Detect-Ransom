import subprocess
import sys
import os
# Your existing script code here...

# Function to run the current script as administrator
def run_as_admin():
    try:
        if sys.platform.startswith('win'):
            # Construct the command to run the current script as administrator
            command = ["runas", "/user:Administrator", sys.executable] + sys.argv
            # Run the command
            subprocess.run(command, check=True)
        else:
            print("This functionality is only supported on Windows.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)






# Function to check file or directory permissions
def check_permissions(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    # Check read permission
    if os.access(path, os.R_OK):
        print(f"Read permission is granted for '{path}'.")
    else:
        print(f"Read permission is not granted for '{path}'.")

    # Check write permission
    if os.access(path, os.W_OK):
        print(f"Write permission is granted for '{path}'.")
    else:
        print(f"Write permission is not granted for '{path}'.")

    # Check execute permission
    if os.access(path, os.X_OK):
        print(f"Execute permission is granted for '{path}'.")
    else:
        print(f"Execute permission is not granted for '{path}'.")



    # Check permissions


# Function to provide directory permissions
def provide_directory_permissions(directory_path):
    try:
        mode = input("e.g., 0o444-to read , 0o555-to read and write , 0o777-for full permissions\n""Set Mode : ")
        # Check if the directory exists
        if not os.path.exists(directory_path):
            print(f"The directory '{directory_path}' does not exist.")
            return

        # Change directory permissions
        os.chmod(directory_path, mode)
        print(f"Permissions for '{directory_path}' have been modified successfully.")
    except OSError as e:
        print(f"Error: {e}")

# Example usage
# if __name__ == "__main__":
#     # Specify the directory path
#     directory_path = "C:\\Windows\\diagerr.xml"

#     # Specify the desired mode (e.g., 0o444 to read , 0o555 to read and write , 0o777 for full permissions)
#     mode = 0o777

#     # Provide directory permissions
#     provide_directory_permissions(directory_path, mode)
#     check_permissions(directory_path)
#     run_as_admin()
