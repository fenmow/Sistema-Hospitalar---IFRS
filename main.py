import os
import time
from datetime import datetime
import pymongo
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://mainUser_db_user:coCfh8CQmR2H8d7K@clusterprojeto.3avx00c.mongodb.net/?appName=ClusterProjeto"
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command("ping")
    os.system("cls" if os.name == "nt" else "clear")
    input("Pressione ENTER para acessar o menu...")
except Exception as e:
    print(e)

db = client["sistema_hospitalar"]

users = db["users"]
patients = db["patients"]
doctors = db["doctors"]
appointments = db["appointments"]
health_plans = db["health_plans"]


def get_int(msg, allow_empty=False):
    while True:
        value = input(msg)
        if allow_empty and value.strip() == "":
            return None
        try:
            number = int(value)
            if number < 0:
                print("Número não pode ser negativo.")
                continue
            return number
        except:
            print("Entrada inválida. Digite um número.")

def createHealthPlan(name, plan_type, coverage):
    return health_plans.insert_one({
        "name": name,
        "type": plan_type,
        "coverage": coverage,
        "active": True
    })


def listHealthPlans():
    plans = list(health_plans.find())
    if not plans:
        print("Nenhum plano de saúde cadastrado.")
        return

    print("\nPlanos de Saúde cadastrados:")
    for plan in plans:
        print(f"ID: {plan['_id']} | Nome: {plan['name']} | Tipo: {plan['type']} | Ativo: {plan['active']}")


def createUser(name, age, gender, tel, address, health_plan_id=None, user_type=None):
    doc = {
        "name": name,
        "age": age,
        "gender": gender,
        "tel": tel,
        "address": address,
        "health_plan_id": health_plan_id,
        "createdAt": time.time(),
        "updatedAt": time.time()
    }

    inserted = users.insert_one(doc)

    if user_type == "doctor":
        doctors.insert_one({**doc, "_id": inserted.inserted_id})
    elif user_type == "patient":
        patients.insert_one({**doc, "_id": inserted.inserted_id})
    else:
        print("Erro interno: tipo de usuário não informado.")

    return doc


def createAppointment(patientName, doctorName, date):
    return appointments.insert_one({
        "patientName": patientName,
        "doctorName": doctorName,
        "date": date
    })


def listPatients():
    lista = list(patients.find())
    print("\nPacientes cadastrados:")
    for p in lista:
        plan = health_plans.find_one({"_id": p.get("health_plan_id")})
        plan_name = plan["name"] if plan else "Particular"
        print(f"ID: {p['_id']} | Nome: {p['name']} | Idade: {p['age']} | Gênero: {p['gender']} | Plano: {plan_name}")


def listDoctors():
    lista = list(doctors.find())
    print("\nMédicos cadastrados:")
    for d in lista:
        print(f"ID: {d['_id']} | Nome: {d['name']} | Idade: {d['age']} | Gênero: {d['gender']}")


def listAppointments():
    lista = list(appointments.find())
    print("\nConsultas cadastradas:")
    for a in lista:
        print(f"ID: {a['_id']} | Paciente: {a['patientName']} | Médico: {a['doctorName']} | Data: {a['date'].strftime('%d/%m/%Y')}")


def askForInfo(type):
    os.system("cls" if os.name == "nt" else "clear")

    name = input(f"Informe o nome do {type}: ")
    age = get_int(f"Informe a idade do {type}: ")
    gender = input(f"Informe o gênero do {type}: ")
    tel = input(f"Informe o telefone do {type}: ")
    address = input(f"Informe o endereço do {type}: ")

    health_plan_id = None
    user_type = None

    if type == "paciente":
        user_type = "patient"
        listHealthPlans()
        choice = input("\nDigite o ID do plano de saúde ou ENTER para Particular: ")
        if choice.strip():
            try:
                health_plan_id = ObjectId(choice)
            except:
                print("ID inválido. Usando Particular.")

    else:
        user_type = "doctor"

    return createUser(name, age, gender, tel, address, health_plan_id, user_type
    )


def askAppointmentDate(msg="Digite a data (dd/mm/yyyy): "):
    while True:
        data = input(msg)
        try:
            return datetime.strptime(data, "%d/%m/%Y")
        except:
            print("Data inválida.")


def askForAppointmentInfo():
    os.system("cls" if os.name == "nt" else "clear")

    if patients.count_documents({}) == 0 or doctors.count_documents({}) == 0:
        print("Necessário ter pacientes e médicos cadastrados.")
        input("ENTER...")
        return

    listPatients()
    patientName = input("\nNome do paciente: ")
    if not patients.find_one({"name": patientName}):
        print("Paciente não encontrado.")
        input("ENTER...")
        return

    listDoctors()
    doctorName = input("\nNome do médico: ")
    if not doctors.find_one({"name": doctorName}):
        print("Médico não encontrado.")
        input("ENTER...")
        return

    date = askAppointmentDate()

    createAppointment(patientName, doctorName, date)

def RemoveAppointment():
    listAppointments()
    _id = input("\nID da consulta para excluir: ")

    try:
        result = appointments.delete_one({"_id": ObjectId(_id)})
        if result.deleted_count:
            print("Consulta removida!")
        else:
            print("ID não encontrado.")
    except:
        print("ID inválido.")

    input("ENTER...")


def RemovePatients():
    listPatients()
    _id = input("\nID do paciente para excluir: ")

    try:
        users.delete_one({"_id": ObjectId(_id)})
        patients.delete_one({"_id": ObjectId(_id)})
        print("Paciente removido!")
    except:
        print("ID inválido.")

    input("ENTER...")


def RemoveDoctor():
    listDoctors()
    _id = input("\nID do médico para excluir: ")

    try:
        users.delete_one({"_id": ObjectId(_id)})
        doctors.delete_one({"_id": ObjectId(_id)})
        print("Médico removido!")
    except:
        print("ID inválido.")

    input("ENTER...")


def updateUser(collection):
    lista = list(collection.find())

    listPatients() if collection == patients else listDoctors()

    _id = input("\nID que deseja atualizar: ")
    try:
        user = collection.find_one({"_id": ObjectId(_id)})
    except:
        print("ID inválido.")
        input("ENTER...")
        return

    if not user:
        print("Usuário não encontrado.")
        input("ENTER...")
        return

    name = input(f"Nome ({user['name']}): ") or user["name"]
    age = input(f"Idade ({user['age']}): ") or user["age"]
    gender = input(f"Gênero ({user['gender']}): ") or user["gender"]
    tel = input(f"Telefone ({user['tel']}): ") or user["tel"]
    address = input(f"Endereço ({user['address']}): ") or user["address"]

    users.update_one(
        {"_id": ObjectId(_id)},
        {"$set": {
            "name": name,
            "age": int(age),
            "gender": gender,
            "tel": tel,
            "address": address,
            "updatedAt": time.time()
        }}
    )

    collection.update_one(
        {"_id": ObjectId(_id)},
        {"$set": {
            "name": name,
            "age": int(age),
            "gender": gender,
            "tel": tel,
            "address": address,
        }}
    )

    print("Atualizado!")
    input("ENTER...")

def pacientActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\nMENU PACIENTES\n"
            "1 - Cadastrar\n2 - Listar\n3 - Atualizar\n4 - Excluir\n5 - Voltar"
        )
        op = get_int("Opção: ")

        if op == 1:
            askForInfo("paciente")
        elif op == 2:
            listPatients()
            input("ENTER...")
        elif op == 3:
            updateUser(patients, "paciente")
        elif op == 4:
            RemovePatients()
        elif op == 5:
            return


def doctorActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\nMENU MÉDICOS\n"
            "1 - Cadastrar\n2 - Listar\n3 - Atualizar\n4 - Excluir\n5 - Voltar"
        )
        op = get_int("Opção: ")

        if op == 1:
            askForInfo("médico")
        elif op == 2:
            listDoctors()
            input("ENTER...")
        elif op == 3:
            updateUser(doctors, "médico")
        elif op == 4:
            RemoveDoctor()
        elif op == 5:
            return


def appointmentsActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\nMENU CONSULTAS\n"
            "1 - Cadastrar\n2 - Listar\n3 - Excluir\n4 - Voltar"
        )
        op = get_int("Opção: ")

        if op == 1:
            askForAppointmentInfo()
        elif op == 2:
            listAppointments()
            input("ENTER...")
        elif op == 3:
            RemoveAppointment()
        elif op == 4:
            return


def mainMenu():

    if health_plans.count_documents({}) == 0:
        createHealthPlan("Unimed", "Apartamento", ["Consulta", "Exames", "Cirurgia"])
        createHealthPlan("Bradesco Saúde", "Enfermaria", ["Consulta", "Exames"])
        createHealthPlan(
            "SulAmérica",
            "Empresarial",
            [
                "Consultas", "Exames", "Cirurgias",
                "Telemedicina", "Descontos em farmácias"
            ]
        )

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\nSISTEMA HOSPITALAR - IFRS\n"
            "1 - Pacientes\n2 - Médicos\n3 - Consultas\n4 - Sair"
        )
        op = get_int("Opção: ")

        if op == 1:
            pacientActionsMenu()
        elif op == 2:
            doctorActionsMenu()
        elif op == 3:
            appointmentsActionsMenu()
        elif op == 4:
            break


mainMenu()