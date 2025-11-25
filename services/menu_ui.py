from colorama import init, Fore, Style
init(autoreset=True)

class MenuUI:
    def header(self, title: str):
        print(Fore.CYAN + "\n" + "=" * 60)
        print(title.center(60))
        print("=" * 60 + Style.RESET_ALL)

    def option(self, key: str, text: str):
        print(Fore.YELLOW + f"[{key}] {text}" + Style.RESET_ALL)

    def prompt(self, text: str) -> str:
        return input(Fore.GREEN + text + Style.RESET_ALL)
