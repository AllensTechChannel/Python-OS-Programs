import sys
import os
import time
import subprocess

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen appropriately
        print("\nMain Menu:")
        print("1. Pong")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Opening Pong")
            time.sleep(1)
            if os.path.exists("games\Pong.py"):
                subprocess.run([sys.executable, "games\Pong.py"])
            else:
                print("Pong.py not found.")
            time.sleep(1)
        elif choice == "2":
            print("Returning to the Desktop!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
