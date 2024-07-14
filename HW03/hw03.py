import os
import sys
from colorama import init, Fore

def list_directory(path, level=0):
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"{'  ' * level}{Fore.BLUE}{item}{Fore.RESET}")
                list_directory(item_path, level + 1)
            else:
                print(f"{'  ' * level}{Fore.GREEN}{item}{Fore.RESET}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
        return
    path = sys.argv[1]
    if not os.path.isdir(path):
        print("Вказаний шлях не веде до директорії.")
        return
    init(autoreset=True)
    list_directory(path)

if __name__ == "__main__":
    main()
