
import sys
sys.path.append("..")
from ClientInterface import ClientInterface

def main_menu(client_interface):
        while True:
            print("\nMain Menu")
            print("0. Exit")
            print("1. Provider Menu")
            print("2. Manager Menu")

            choice = input("\nChoose an option: ")
            if choice == '1':
                client_interface.display_menu("provider")
            elif choice == '2':
                client_interface.display_menu("manager")
            elif choice == '0':
                    print("\nExiting program.")
                    break
            else:
                    print("\nInvalid option. Please try again.")

def main():
    client_interface = ClientInterface()
    main_menu(client_interface)

if __name__ == "__main__":
    main()