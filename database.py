import sqlite3
from insured import InsuredPerson


class Database:

    def __init__(self, db):
        """
        Initialisation of the database
        Expects a db instance
        Creates the connection
        """
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS pojisteni "
                         "(krestni_jmeno TEXT, prijmeni TEXT, vek INTEGER, telefonnni_cislo INTEGER)")
        self.conn.commit()

    def add_insured(self, insured):
        """
        Adds an insured record to the DB. Expects a first_name, last_name, age and phone_number value
        returns a confirmation message
        """
        self.cur.execute('INSERT INTO pojisteni VALUES (?, ?, ?, ?)',
                         (insured.first_name, insured.last_name, insured.age, insured.phone_number))
        self.conn.commit()
        return "Záznam byl přidán!"

    def get_insured(self):
        """
        Loops through the records and returns a list with all entries
        """
        insured_lst = []
        for i in self.cur.execute('SELECT * FROM pojisteni'):
            insured_lst.append(InsuredPerson(i[0], i[1], i[2], i[3]))
        self.conn.commit()
        return insured_lst

    def get_insured_by_name(self, first_name, last_name):
        """
        Expects first_name and last_name.
        If it finds matching value in the DB, it returns the entry with all its data.
        If it can't find it, it returns a string message.
        """
        self.cur.execute('SELECT * FROM pojisteni WHERE krestni_jmeno=? AND prijmeni=?', (first_name, last_name))
        data = self.cur.fetchone()
        self.conn.commit()
        if not data:
            return "Záznam nenalezen!"

        return f"Jméno: {data[0]} {data[1]}\nVěk: {data[2]}\nTelefonní číslo: {data[3]}"

    def delete_insured(self, first_name, last_name):
        """
        Expects first_name and last_name.
        Deletes the entry if found.
        If not found, returns a string.
        """
        self.cur.execute('SELECT * FROM pojisteni WHERE krestni_jmeno=? AND prijmeni=?', (first_name, last_name))
        data = self.cur.fetchone()
        if not data:
            return "Záznam neexistuje a nebylo možné ho smazat!"
        self.cur.execute('DELETE FROM pojisteni WHERE krestni_jmeno=? AND prijmeni=?', (first_name, last_name))
        self.conn.commit()
        return "Záznam vymazan!"

    def __del__(self):
        """
        Closes the connection when the program is stopped.
        """
        self.conn.close()
