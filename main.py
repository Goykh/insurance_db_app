#!/usr/bin/env python3


from insured import InsuredPerson
import insuredSDK
import time
import sys
import subprocess

# TODO: fool proofing the deleting


class Menu:

    def print_menu(self):
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

            response = int(input())
            print()
            # writes out the insured
            if response == 1:
                for i in insuredSDK.get_insured():
                    print(i, "\n")
            # adding an insured
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
                insuredSDK.add_insured(InsuredPerson(first_name, last_name, age, phone_number))
            # searching for an insured by first and last name
            elif response == 3:
                print("Zadejte křestní jméno: ")
                first_name = input().strip(" ").capitalize()
                print("Zadejte příjmení: ")
                last_name = input().strip(" ").capitalize()
                print()
                print(insuredSDK.get_insured_by_name(first_name, last_name))
            # deleting an insured by first and last name
            elif response == 4:
                print("Křestní jméno pojištěného?")
                first_name = input()
                print("Příjmení pojištěného?")
                last_name = input()
                print()
                print(f"Chystáte se vymazat pojištěného {first_name} {last_name}.")
                print("Jste si tímto krokem jistý/á? (stiskněte a pro potrvzení a n pro návrat do menu")
                answer = input()
                if answer == "a":
                    print(insuredSDK.delete_insured(first_name, last_name))
                elif answer == "n":
                    continue
                else:
                    print("Zadaný příkaz je neplatný.")
            # ending the app
            else:
                print("Děkujeme za použití, aplikace se teď ukončí")
                time.sleep(2)
                break

            input("Pro návrat do menu stiskněte Enter.")
            self.clear_screen()

    def clear_screen(self):
        """
        Clears the menu
        """
        if sys.platform.startswith("win"):
            subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            subprocess.call(["clear"])


if __name__ == "__main__":
    menu = Menu()
    menu.print_menu()






