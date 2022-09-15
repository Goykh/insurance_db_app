#!/usr/bin/env python3
from insured import InsuredPerson
from database import Database
import time
import sys
import subprocess

# Makes connection to the DB
database = Database('pojistenci.db')


class Menu:

    def print_menu(self):
        """
        Prints the CMD menu and all it's options.
        """
        while True:
            # the menu layout in the console
            print("--------------------")
            print("Evidence pojištěných")
            print("--------------------")
            print("""
Vyberte si akci:
1. Vypsat všechny pojištěné
2. Přidat nového pojištěného
3. Vyhledat pojištěného
4. Smazat pojištěného
5. Ukončit aplikaci
            """)

            try:
                response = int(input())
                print()

                # Calls method to return list of all entries in DB
                if response == 1:
                    for i in database.get_insured():
                        print(i, "\n")

                # Calls method to add one entry
                elif response == 2:
                    print("Křestní jméno pojištěnce?")
                    first_name = input()
                    print("Příjmení pojištěnce?")
                    last_name = input()
                    print("Věk pojištěnce (číslem)?")
                    age = int(input())
                    print("Telefonní číslo pojištěnce?")
                    phone_number = int(input())
                    print()
                    database.add_insured(InsuredPerson(first_name, last_name, age, phone_number))

                # Calls method to search for entry by first_name and last_name
                elif response == 3:
                    print("Zadejte křestní jméno: ")
                    first_name = input().strip(" ").capitalize()
                    print("Zadejte příjmení: ")
                    last_name = input().strip(" ").capitalize()
                    print()
                    print(database.get_insured_by_name(first_name, last_name))

                # Calls method to delete entry by first_name and last_name
                elif response == 4:
                    print("Křestní jméno pojištěného?")
                    first_name = input()
                    print("Příjmení pojištěného?")
                    last_name = input()
                    print()
                    print(f"Chystáte se vymazat pojištěného {first_name} {last_name}.")
                    # Asks for verification of the deletion to avoid a mistake delete.
                    # I am sure this can be done better, but it is the best I came up with.
                    print("Jste si tímto krokem jistý/á? (stiskněte a pro potrvzení a n pro návrat do menu)")
                    answer = input()
                    if answer == "a":
                        # Deletes the entry
                        print(database.delete_insured(first_name, last_name))
                    elif answer == "n":
                        print("Proces smazání byl zrušen.")
                        # Continues the program without deleting anything
                    else:
                        # Safety net if someone managed to somehow input something wrong
                        print("Zadaný příkaz je neplatný.")

                # Prints message to end the app and waits 2 seconds before it closes
                else:
                    print("Děkujeme za použití, aplikace se teď ukončí.")
                    time.sleep(2)
                    break

                # Asks to press "Enter" to return back to the menu
                input("Pro návrat do menu stiskněte Enter.")
                # Cleans the cmd lines before it prints the menu again
                self.clear_screen()
            except ValueError:
                print("Špatný input. Napište číslo od 1 do 5.\nEnter pro návrat do menu.")
                input()

                self.clear_screen()

    def clear_screen(self):
        """
        Clears the CMD window.
        """
        if sys.platform.startswith("win"):
            subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            subprocess.call(["clear"])


if __name__ == "__main__":
    menu = Menu()
    menu.print_menu()
