import sqlite3
from insured import InsuredPerson


connection = sqlite3.connect('pojistenci.db')
c = connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS pojisteni '
          '(krestni_jmeno TEXT, prijmeni TEXT, vek INTEGER, telefonnni_cislo INTEGER)')
connection.close()


def add_insured(insured):
    # adding an insured
    connection = sqlite3.connect('pojistenci.db')
    c = connection.cursor()
    c.execute('INSERT INTO pojisteni VALUES (?, ?, ?, ?)',
              (insured.first_name, insured.last_name, insured.age, insured.phone_number))
    connection.commit()
    connection.close()
    return "Záznam byl přidán!"


def get_insured():
    # gets all insured from the DB
    connection = sqlite3.connect('pojistenci.db')
    c = connection.cursor()
    insured_lst = []
    for i in c.execute('SELECT * FROM pojisteni'):
        insured_lst.append(InsuredPerson(i[0], i[1], i[2], i[3]))
    connection.commit()
    connection.close()
    return insured_lst


def get_insured_by_name(first_name, last_name):
    # gets an insured from the DB by entering the first and last name
    # it returns all data
    connection = sqlite3.connect('pojistenci.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pojisteni WHERE krestni_jmeno=? AND prijmeni=?', (first_name, last_name))
    data = c.fetchone()
    connection.commit()
    connection.close()
    if not data:
        return "Záznam nenalezen!"

    return f"Jméno: {data[0]} {data[1]}\nVěk: {data[2]}\nTelefonní číslo: {data[3]}"


def delete_insured(first_name, last_name):
    # deleting an insured by first and last name
    # this one needs a bit of fool proofing

    connection = sqlite3.connect('pojistenci.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pojisteni WHERE krestni_jmeno=? AND prijmeni=?', (first_name, last_name))
    data = c.fetchone()
    if not data:
        return "Záznam neexistuje a nebylo možné ho smazat!"
    c.execute('DELETE FROM pojisteni WHERE krestni_jmeno=? AND prijmeni=?', (first_name, last_name))
    connection.commit()
    connection.close()
    return "Záznam vymazan!"

