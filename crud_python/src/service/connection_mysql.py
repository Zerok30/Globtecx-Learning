from dto.contact import Contact
from dotenv import load_dotenv
from mysql.connector import MySQLConnection, Error
import os

load_dotenv()


class ConnectionService:
    def __init__(self):
        self.__connection = MySQLConnection(
            user="root",
            password=os.getenv("MYSQL_ROOT_PASSWORD"),
            database="crud_python",
            host="localhost"
        )

    def connect(self):
        try:
            self.__connection.connect()
            print("Conectado correctamente a la base de datos")
        except Error as err:
            print(f"Ocurrio un error al conectar a la base de datos: {err}")

    def cursor(self):
        return self.__connection.cursor()

    def create_table_contacts(self):
        try:
            cursor = self.cursor()
            query = "CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), lastname VARCHAR(50), phone VARCHAR(12), address VARCHAR(50))"
            cursor.execute(query)
        except Error as err:
            print(f"Ocurrio un error: {err}")

    def insert_contact(self, contact: Contact):
        try:
            cursor = self.cursor()

            query = "INSERT INTO contacts(name,lastname,phone,address) VALUES(%s,%s,%s,%s)"
            values = (contact.name, contact.lastname,
                      contact.phone, contact.address)

            cursor.execute(query, values)
            self.__connection.commit()

            return "Datos ingresados correctamente"
        except Error as err:
            print(f"Ocurrio un error: {err}")

    def delete_contact(self, id):
        try:
            query = f"DELETE FROM contacts WHERE id={id}"
            cursor = self.cursor()
            cursor.execute(query)
            self.__connection.commit()

            return "Contacto eliminado correctamente"
        except Error as err:
            print(f"Ocurrio un error: {err}")

    def get_all_contacts(self):
        try:
            cursor = self.__connection.cursor()
            query = "SELECT * FROM contacts"
            contacts = []
            cursor.execute(query)

            for row in cursor.fetchall():
                id = row[0]
                name = row[1]
                lastname = row[2]
                phone = row[3]
                address = row[4]
                contacts.append({"name": name, "lastname": lastname,
                                "phone": phone, "address": address, "id": id})

            return contacts
        except Error as err:
            print(f"Ocurrio un error: {err}")

    def get_contact(self, id):
        try:
            cursor = self.cursor()
            query = f"SELECT * FROM contacts WHERE id = {id}"
            cursor.execute(query)
            contact = cursor.fetchall()[0]

            return {
                "id": contact[0],
                "name": contact[1],
                "lastname": contact[2],
                "phone": contact[3],
                "address": contact[4]
            }

        except Error as err:
            print(f"Ocurrio un error: {err}")

    def update_contact(self, contact):
        try:
            cursor = self.cursor()

            query_params = [f"{clave}=%s" for clave in contact.keys()]
            query = f"""UPDATE contacts SET {', '.join(query_params)} WHERE id={contact["id"]}"""
            values = list(contact.values())
            cursor.execute(query, values)
            self.__connection.commit()

            return "Usuario actualizado"
        except Error as err:
            print(f"Ocurrio un error: {err}")
