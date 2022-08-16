#!/usr/bin/env python3


from insured import InsuredPerson
import insuredSDK
import time

# TODO: fool proofing the deleting


def print_menu():
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


while True:
    # prints the menu and waits for respond
    print_menu()
    response = int(input())
    print()
    # writes out the insured
    if response == 1:
        for i in insuredSDK.get_insured():
            print(i, "\n")
    # adding an insured
    elif response == 2:
        print("První jméno pojištěnce?")
        first_name = input()
        print("Druhé jméno pojištěnce?")
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
        first_name = input()
        print("Zadejte příjmení: ")
        last_name = input()
        print()
        insuredSDK.get_insured_by_name(first_name, last_name)
    # deleting an insured by first and last name
    elif response == 4:
        print("První jméno pojištěného?")
        first_name = input()
        print("Příjmení pojištěného?")
        last_name = input()
        print()
        print(insuredSDK.delete_insured(first_name, last_name))
    # ending the app
    else:
        print("Děkujeme za použití, aplikace se teď ukončí")
        time.sleep(2)
        break
