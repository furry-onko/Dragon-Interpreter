from colorama import Fore, Back, Style, init
import tokenizer
from os import system as cmd
import os

init(autoreset=True)

def main() -> None:
    cmd("cls")
    print("Dragon interpreter v1.0")

    while True:
        try:
            file_path: str = input("File path: ")
            if file_path:
                _, extension = os.path.splitext(file_path)
                if extension not in ('.dragon', '.drg'):
                    print(f"{Fore.RED + Style.BRIGHT} File extension should be .drg or .dragon, not {extension}")
                    exit(1)
                try:
                    with open(file_path, 'r', encoding='UTF-8') as file:
                        code: str = file.read()
                        try:
                            tokenizer.tokenize(code, file_path)
                            break
                        except Exception as x:
                            print(str(x))

                except Exception as x:
                    print(f"{Fore.RED + Style.BRIGHT + x}")
            else:
                print(f"{Fore.RED + Style.BRIGHT} Insert a file path")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW} Keyboard interrupt. Exitting")
            exit(0)

if __name__ == "__main__":
    main()