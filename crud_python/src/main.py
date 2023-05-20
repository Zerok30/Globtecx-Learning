from flask import Flask, jsonify, request
from controller.connection_mysql import ConnectionController
from dto.contact import Contact
import json

conn_ctrl = ConnectionController()

conn_ctrl.connect()
conn_ctrl.create_table_contacts()

# Instanciando flask
app = Flask(__name__)


@app.route("/")
def get_all_contacts():
    contacts = conn_ctrl.get_all_contacts()
    return jsonify(contacts)


@app.route("/<int:id>")
def get_contact(id):
    contact = conn_ctrl.get_contact(id)
    return contact


@app.route("/", methods=["POST"])
def add_contact():
    json = request.json
    contact = Contact(json["name"], json["lastname"],
                      json["phone"], json["address"])
    response = conn_ctrl.insert_contact(contact)
    return {"msg": response}


@app.route("/<int:id>", methods=["PUT"])
def update_contact(id):
    contact = get_contact(id)
    data = request.json

    if data.get("id") == None:
        new_contact = {**contact, **data}
        print(new_contact)
        response = conn_ctrl.update_contact(new_contact)
        return {"msg": response}

    return {"msg": "No puede modificar el ID"}


@app.route("/<int:id>", methods=["DELETE"])
def delete_contact(id):
    reponse = conn_ctrl.delete_contact(id)
    return {"msg": reponse}


if (__name__ == "__main__"):
    app.run()
