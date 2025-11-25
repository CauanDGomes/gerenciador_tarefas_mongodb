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

    def prompt_choice(self, text: str, valid_options: list) -> str:
        """Pede uma escolha válida até que o usuário digite uma opção válida"""
        while True:
            choice = self.prompt(text).strip()
            if choice in valid_options:
                return choice
            else:
                print(Fore.RED + f"❌ Opção inválida! Digite uma das opções: {', '.join(valid_options)}" + Style.RESET_ALL)

    def prompt_required(self, text: str) -> str:
        """Pede entrada obrigatória até que o usuário digite algo"""
        while True:
            value = self.prompt(text).strip()
            if value:
                return value
            else:
                print(Fore.RED + "❌ Campo obrigatório! Por favor, digite algo." + Style.RESET_ALL)

    def prompt_optional_or_retry(self, text: str) -> str:
        """Pede entrada opcional. Se vazio, retorna vazio. Se inválido, retorna None"""
        value = self.prompt(text).strip()
        return value if value else None

    def prompt_status(self, text: str = "Status (P/Pendente, E/Em Andamento, C/Concluído): ") -> str:
        """Pede status com validação de abreviações"""
        while True:
            value = self.prompt(text).strip().upper()
            
            # Mapear abreviações para status completo
            status_map = {
                "P": "pendente",
                "E": "em_andamento",
                "C": "concluida"
            }
            
            if value in status_map:
                return status_map[value]
            elif value in ["PENDENTE", "EM_ANDAMENTO", "CONCLUIDA"]:
                return value.lower()
            else:
                print(Fore.RED + "❌ Opção inválida! Use: P (Pendente), E (Em Andamento) ou C (Concluído)" + Style.RESET_ALL)
