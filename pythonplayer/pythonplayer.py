import os
import time
from playsound import playsound

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\nMenu:")
    print("1. Closing Time by Semisonic")
    print("2. Mamma Mia by ABBA")
    print("3. Doom OST - E1M1 - At Doom's Gate by Robert Prince ")
    print("4. Keybord Cat by Charlie Schmidt ")
    print("5. Exit")

def launch_music(filename, original_dir):
    try:
        os.chdir("default")  # Make sure this folder exists!
        playsound(filename)
    except FileNotFoundError:
        print("Music file or folder not found!")
    finally:
        os.chdir(original_dir)
    input("\nPress Enter to return to the menu...")
def launch_music(filename, original_dir):
    try:
        os.chdir("default")  # Make sure this folder exists!
        playsound(filename)
    except FileNotFoundError:
        print("Music file or folder not found!") 
    finally:
        os.chdir(original_dir)
    input("\nPress Enter to return to the menu...")
def launch_music(filename, original_dir):
    try:
        os.chdir("default")  # Make sure this folder exists!
        playsound(filename)
    except FileNotFoundError:
        print("Music file or folder not found!")
    finally:
        os.chdir(original_dir)
    input("\nPress Enter to return to the menu...")
def launch_music(filename, original_dir):
    try:
        os.chdir("default")  # Make sure this folder exists!
        playsound(filename)
    except FileNotFoundError:
        print("Music file or folder not found!") 
    finally:
        os.chdir(original_dir)
    input("\nPress Enter to return to the menu...")

def main():
    original_dir = os.getcwd()
    while True:
        clear()
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            print("Name: Closing Time")
            print("Artist: Semisonic")
            launch_music("Closing Time Semisonic Lyrics.mp3", original_dir)

        elif choice == "2":
            print("Name: Mamma Mia")
            print("Artist: ABBA")
            launch_music("Abba - Mamma Mia.mp3", original_dir)
        elif choice == "3":
            print("Name: Doom OST - E1M1 - At Doom's Gate")
            print("Author: Robert Prince")
            
            launch_music("Doom OST - E1M1 - At Doom's Gate.mp3", original_dir)

        elif choice == "4":
            print("Name: Keyboard Cat")
            print("Author: Charlie Schmidt")
            launch_music("Charlie Schmidt's Keyboard Cat! - THE ORIGINAL!.mp3", original_dir)
     
        elif choice == "5":  
            print("Exiting...")
            break



        else:
            print("Invalid choice or unimplemented feature. Please try again.")
            playsound('error-beep.wav')
            time.sleep(1)

if __name__ == "__main__":
    main()
