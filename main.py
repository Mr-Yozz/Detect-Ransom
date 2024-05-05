from ascii_magic import AsciiArt
import random
from Check_information_status import *
from backup_files import *
from ransomware_process import *
from encryptdecrypt import *
from Scanhash import *
import sys
from filepermission import *

class Switch:
    def case1(self):
        Check()   

    def case2(self):
        try:
            Backup = input("\033[1;34m" "Are you sure backup files: (y/n)").lower()
            if Backup == "y" :
                backup()
            # elif Backup == "no"or"n":
            #     print("\033[1;31;40m" "Ok don't backup files: " "\033[0m")
            else:
                print("\033[1;32;40m" "Ok don't backup files" "\033[0m")        
        except KeyboardInterrupt:
            print("\033[1;31m" "Exit Program. Goodbye!" "\033[0m")

    def case3(self):
        try:
            detectransomware = input("\033[1;34m" "Are you sure Scaning Ransomware: (y/n)").lower()
            if detectransomware == "y" :
                path_input = input("\033[32m" "scan_for_ransomware : Enter Your Path or Directory ")
                detect_ransomware(path_input)
                ransom_process()
                # encrypt(path_input)
            # elif detectransomware != "y":
            #     print("\033[1;31;40m" "Ok don't scan files: " "\033[0m")
            else:
                print("\033[1;32;40m" "Ok don't scan files" "\033[0m")

        except KeyboardInterrupt:
            print("\033[1;31m" "Exit Program. Goodbye!" "\033[0m")
        try:
            data = input("\033[1;32m" "Check File Permission (y/n): ").lower()
            if data == "y" :
                directory_path = input("Enter Your File Path: ")
                # Provide directory permissions
                check_permissions(directory_path)
                provide_directory_permissions(directory_path)
                run_as_admin()
            else:  
                print("\033[1;32;40m" "Ok don't scan files" "\033[0m")  
                
        except KeyboardInterrupt:
                print("\033[1;31m""Skip Check File Permission:")


    def case4(self):
        try:
            data = input("\033[1;34m" "Any files to encrypt or derypt : (y/n)").lower()
            if data == "y":
                secure()
            else:
                print("\033[1;31;40m" "OK every think is clear:" "\033[0m")
        except KeyboardInterrupt:
            print("\033[1;31m" "Exit Program. Goodbye!" "\033[0m")

    def case5(self):
        try:
            data = input("\033[1;34m" "Are You Sure System Monitoring: (y/n)").lower()
            if data == "y":
                run()
            else:
                print("\033[1;31;40m" "OK every think is clear:" "\033[0m")
        except KeyboardInterrupt:
            print("\033[1;31m" "Exit Program. Goodbye!" "\033[0m")
    
    def case6(self):
        try:
            data = input("\033[1;34m" "Are You Scan For Hash : (y/n)" "\033[0m").lower()
            if data == "y":
                hash = input("\033[1;31m" "Enter Your Hash : ") 
                search_hash(hash)
            else:
                print("\033[1;31;40m" "OK every think is clear:" "\033[0m")
        except KeyboardInterrupt:
            print("\033[1;31m" "Exit Program. Goodbye!" "\033[0m")

    def case7(self):
        sys.exit()


    def default(self):
        print("Enter Correct Choice")

if __name__ == "__main__":
    switch = Switch()

    # from ascii_magic import AsciiArt
    # import random

    # List of image paths
    image_paths = [
        "images/image1.jpg",
        "images/image2.jpg",
        "images/image3.jpg",
        "images/image4.jpg",
        "images/image5.jpg",
        "images/image6.jpg",
        

        # Add more image paths as needed
    ]

    # Pick a random image path
    random_image_path = random.choice(image_paths)

    my_art = AsciiArt.from_image(random_image_path)
    print("\033[1;31m")
    art = my_art.to_terminal(columns=50, monochrome=True)
    print(pyfiglet.print_figlet(text="RANSOM",font="Bloody",colors="red"))

    try:
        while True:
            print("\033[1;34m \n")
            print("1 : Checking your information \n ")
            print("2 : Backup Your Files \n ")
            print("3 : Detecting Ransomware \n ")
            print("4 : Encryption & Decryption Your Files \n ")
            print("5 : Monitoring System  \n ")
            print("6 : Scan for Hash \n")
            print("7 : Exit  or Press Ctrl+C\n ")
                # Get input
            choice = int(input("Enter your choice: ")) 
            try:

                if choice == 1:
                    switch.case1()
                elif choice == 2:
                    switch.case2()
                elif choice == 3:
                    switch.case3()
                elif choice == 4:
                    switch.case4()
                elif choice == 5:
                    switch.case5()
                elif choice == 6 :
                    switch.case6()
                elif choice == 7:  
                    switch.case7()                      
                    # print("\033[1;31;40m""Error: Enter Correct Choice" "\033[0m")
                else:
                    print("\033[1;31;40m""Error: Enter Correct Choice" "\033[0m")

            except Exception  as e:
                    print("\033[1;31;40m" "Error:", e , "\033[0m")

    except KeyboardInterrupt:
        switch.case7()
        print("Exit Program. Goodbye!")

