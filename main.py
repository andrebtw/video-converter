import os
import colorama




def ascii_art():

    width, height = os.get_terminal_size() #get terminal size

    print("             __      _______ _____  ______ ____                   ".center(width))
    print("             \ \    / /_   _|  __ \|  ____/ __ \                  ".center(width))
    print("              \ \  / /  | | | |  | | |__ | |  | |                 ".center(width))
    print("               \ \/ /   | | | |  | |  __|| |  | |                 ".center(width))
    print("                \  /   _| |_| |__| | |___| |__| |                 ".center(width))
    print("   _____ ____  _ \/___|_____|_____/|______\____/__ ______ _____   ".center(width))
    print("  / ____/ __ \| \ | \ \    / /  ____|  __ \__   __|  ____|  __ \  ".center(width))
    print(" | |   | |  | |  \| |\ \  / /| |__  | |__) | | |  | |__  | |__) | ".center(width))
    print(" | |   | |  | | . ` | \ \/ / |  __| |  _  /  | |  |  __| |  _  /  ".center(width))
    print(" | |___| |__| | |\  |  \  /  | |____| | \ \  | |  | |____| | \ \  ".center(width))
    print("  \_____\____/|_| \_|   \/   |______|_|  \_\ |_|  |______|_|  \_\ ".center(width))


def clear_terminal():
    if os.name == "nt": #If OS is Windows
        os.system("cls")
    else:
        os.system("clear")

def line_jump(number):
    while number != 0:
        print("")
        number = number - 1
    


def file_selection():
    pass

def file_deselection():
    pass

def files_convertion():
    pass

def help():
    pass

def exit():
    clear_terminal()
    quit()

def menu():
    clear_terminal()
    ascii_art()
    line_jump(2)

    selected_files=[]
        
    ###Menu Options###
    print (f"1 - Select a file   |   Selected Files : {selected_files}")
    line_jump(1)
    print (f"2 - Deselect a file")
    line_jump(1)
    print (f"3 - Convert File(s)")
    line_jump(1)
    print (f"4 - Help")
    line_jump(1)
    print (f"5 - Exit")
    line_jump(2)

    

        #if "1" in select_menu:
        #    file_selection()

        #elif "2" in select_menu:
        #    file_deselection()

        #elif "3" in select_menu:
        #    files_convertion()
        
        #elif "4" in select_menu:
        #    help()
        
        #elif "5" in select_menu:
        #    exit()



def main ():
    menu()
    



if __name__ == "__main__":
    main()
