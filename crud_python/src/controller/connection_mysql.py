from service.connection_mysql import ConnectionService


class ConnectionController:

    def __init__(self):
        self.connection_ctrl = ConnectionService()

    def connect(self):
        return self.connection_ctrl.connect()

    def create_table_contacts(self):
        return self.connection_ctrl.create_table_contacts()

    def insert_contact(self, contact):
        return self.connection_ctrl.insert_contact(contact)

    def get_all_contacts(self):
        return self.connection_ctrl.get_all_contacts()

    def get_contact(self, id):
        return self.connection_ctrl.get_contact(id)

    def update_contact(self, contact):
        return self.connection_ctrl.update_contact(contact)

    def delete_contact(self, id):
        return self.connection_ctrl.delete_contact(id)
