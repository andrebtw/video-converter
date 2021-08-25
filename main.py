import os
import sys

import termios
import tty
import time
import colorama

selected_files=[]


#Getch function Code from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch



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
    clear_terminal()
    line_jump(2)
    
    selected_file = str(input("Please select the file : "))

    selected_files.append(selected_file)

    menu()

def file_deselection():
    clear_terminal()
    line_jump(2)

    #while 

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
    line_jump(1)

    menu = False

    while menu == False:
        pressed_button = getch()

        if pressed_button == "1":
            menu = True
            file_selection()
        if pressed_button == "2":
            file_deselection()
        if pressed_button == "3":
            files_convertion()
        if pressed_button == "4":
            help()
        if pressed_button == "5":
            exit()



def main ():
    menu()
    


if __name__ == "__main__":
    main()
