# main.py
from database.database import Database
from services.menu import Menu
from services.splash_screen import SplashScreen

def main():
    db = Database()
    splash = SplashScreen(db)
    splash.display()
    menu = Menu(db)
    menu.run()

if __name__ == "__main__":
    main()
