from colorama import Fore, Back, Style, init
import tokenizer

init(autoreset=True)

def main() -> None:
    print("Dragon interpreter v1.0")

    while True:
        try:
            file_path: str = input("File path: ")
            if file_path:
                try:
                    with open(file_path, 'r') as file:
                        code: str = file.read()
                        tokenizer.tokenize(code, file_path)
                        break
                except Exception as x:
                    print(f"{Fore.RED + Style.BIRGHT + x}")
            else:
                print(f"{Fore.RED + Style.BIRGHT} Insert a file path")
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW} Keyboard interrupt. Exitting")
            exit(0)

if __name__ == "__main__":
    main()