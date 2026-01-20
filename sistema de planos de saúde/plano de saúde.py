import os
import time

users = []
patients = []
doctors = []
appointments = []
health_plans = []


# =========================
# PLANOS DE SAÚDE
# =========================
def createHealthPlan(name, plan_type, coverage):
    newPlan = {
        "id": len(health_plans),
        "name": name,
        "type": plan_type,
        "coverage": coverage,
        "active": True
    }
    health_plans.append(newPlan)
    return newPlan


def listHealthPlans():
    if len(health_plans) == 0:
        print("Nenhum plano de saúde cadastrado.")
        return

    print("\nPlanos de Saúde cadastrados:")
    for plan in health_plans:
        print(
            f"ID: {plan['id']} | Nome: {plan['name']} | Tipo: {plan['type']} | Ativo: {plan['active']}"
        )


def getHealthPlanById(plan_id):
    for plan in health_plans:
        if plan["id"] == plan_id:
            return plan
    return None


# =========================
# USUÁRIOS / PACIENTES
# =========================
def createUser(name, age, gender, tel, address, health_plan_id=None):
    newUser = {
        "id": len(users),
        "name": name,
        "age": age,
        "gender": gender,
        "tel": tel,
        "address": address,
        "health_plan_id": health_plan_id,
        "createdAt": time.time(),
        "updatedAt": time.time(),
    }
    return newUser


def createAppointment(patientName, doctorName, date):
    newAppointment = {
        "id": len(appointments),
        "patientName": patientName,
        "doctorName": doctorName,
        "date": date
    }
    return newAppointment


def listPatients():
    print("Pacientes cadastrados:")
    for i, patient in enumerate(patients):
        plan = getHealthPlanById(patient.get("health_plan_id"))
        plan_name = plan["name"] if plan else "Particular"

        print(
            f"{i + 1}. Nome: {patient['name']} | Idade: {patient['age']} | "
            f"Gênero: {patient['gender']} | Plano: {plan_name}"
        )


def listDoctors():
    print("Médicos cadastrados:")
    for i, doctor in enumerate(doctors):
        print(
            f"{i + 1}. Nome: {doctor['name']} | Idade: {doctor['age']} | Gênero: {doctor['gender']}"
        )


def listAppointments():
    print("Consultas cadastradas:")
    for i, appointment in enumerate(appointments):
        print(
            f"{i + 1}. Paciente: {appointment['patientName']} | "
            f"Médico: {appointment['doctorName']} | Data: {appointment['date']}"
        )


# =========================
# INPUTS
# =========================
def askForInfo(type):
    os.system("cls" if os.name == "nt" else "clear")

    name = input("Informe o nome do " + type + ": ")
    age = int(input("Informe a idade do " + type + ": "))
    gender = input("Informe o gênero do " + type + ": ")
    tel = input("Informe o número de telefone do " + type + ": ")
    address = input("Informe o endereço do " + type + ": ")

    health_plan_id = None
    if type == "paciente":
        listHealthPlans()
        opt = input("\nDigite o ID do plano de saúde ou pressione ENTER para Particular: ")
        if opt:
            health_plan_id = int(opt)

    newEntity = createUser(name, age, gender, tel, address, health_plan_id)
    return newEntity


def askForAppointmentInfo():
    os.system("cls" if os.name == "nt" else "clear")

    if len(patients) == 0 or len(doctors) == 0:
        print("Necessário ter pacientes e médicos cadastrados.")
        input("Pressione ENTER para voltar...")
        return

    listPatients()
    patientName = input("\nDigite o nome do paciente: ")

    listDoctors()
    doctorName = input("\nDigite o nome do médico: ")

    appointmentDate = input("Digite a data da consulta (dd/mm/yyyy): ")
    return createAppointment(patientName, doctorName, appointmentDate)


# =========================
# REMOÇÕES
# =========================
def RemoveAppointment():
    listAppointments()
    index = int(input("Informe o número da consulta que deseja excluir: ")) - 1
    if 0 <= index < len(appointments):
        appointments.pop(index)


def RemovePatients():
    listPatients()
    index = int(input("Informe o número do paciente que deseja excluir: ")) - 1
    if 0 <= index < len(patients):
        patients.pop(index)


def RemoveDoctor():
    listDoctors()
    index = int(input("Informe o número do médico que deseja excluir: ")) - 1
    if 0 <= index < len(doctors):
        doctors.pop(index)


# =========================
# UPDATE
# =========================
def updateUser(userList, userType):
    listPatients() if userType == "paciente" else listDoctors()

    index = int(input("\nDigite o número que deseja atualizar: ")) - 1
    if 0 <= index < len(userList):
        user = userList[index]

        name = input(f"Nome ({user['name']}): ") or user['name']
        age = input(f"Idade ({user['age']}): ") or user['age']
        gender = input(f"Gênero ({user['gender']}): ") or user['gender']
        tel = input(f"Telefone ({user['tel']}): ") or user['tel']
        address = input(f"Endereço ({user['address']}): ") or user['address']

        user.update({
            "name": name,
            "age": int(age),
            "gender": gender,
            "tel": tel,
            "address": address,
            "updatedAt": time.time()
        })


# =========================
# MENUS
# =========================
def pacientActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\nMENU PACIENTES\n"
            "1 - Cadastrar\n2 - Listar\n3 - Atualizar\n4 - Excluir\n5 - Voltar"
        )
        op = int(input("Opção: "))

        if op == 1:
            p = askForInfo("paciente")
            patients.append(p)
            users.append(p)
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
        op = int(input("Opção: "))

        if op == 1:
            d = askForInfo("médico")
            doctors.append(d)
            users.append(d)
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
        op = int(input("Opção: "))

        if op == 1:
            a = askForAppointmentInfo()
            if a:
                appointments.append(a)
        elif op == 2:
            listAppointments()
            input("ENTER...")
        elif op == 3:
            RemoveAppointment()
        elif op == 4:
            return
# =========================
# PLANOS DE SAÚDE
# =========================

def mainMenu():
    # Planos iniciais
    createHealthPlan(
        name="Unimed",
        plan_type="Apartamento",
        coverage=["Consulta", "Exames", "Cirurgia"]
    )

    createHealthPlan(
        name="Bradesco Saúde",
        plan_type="Enfermaria",
        coverage=["Consulta", "Exames"]
    )

    createHealthPlan(
        name="SulAmérica",
        plan_type="Empresarial",
        coverage=[
            "Consultas",
            "Exames",
            "Cirurgias",
            "Isenção de carências a partir de 10 vidas",
            "Descontos em farmácias até 70%",
            "Telemedicina",
            "Programa Saúde Integral"
        ]
    )

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\nSISTEMA HOSPITALAR - IFRS\n"
            "1 - Pacientes\n2 - Médicos\n3 - Consultas\n4 - Sair"
        )
        op = int(input("Opção: "))

        if op == 1:
            pacientActionsMenu()
        elif op == 2:
            doctorActionsMenu()
        elif op == 3:
            appointmentsActionsMenu()
        elif op == 4:
            break


mainMenu()
