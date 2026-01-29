import os
import time

users = []
patients = []
doctors = []
appointments = []
health_plans = []

# ID counters (evita duplicação quando algo é removido)
health_plan_id_counter = 0
user_id_counter = 0
appointment_id_counter = 0


# =========================
# FUNÇÕES DE INPUT SEGURO
# =========================

def get_int(msg, allow_empty=False):
    while True:
        value = input(msg)
        if allow_empty and value.strip() == "":
            return None
        try:
            return int(value)
        except ValueError:
            print("Entrada inválida. Digite um número.")


# =========================
# PLANOS DE SAÚDE
# =========================
def createHealthPlan(name, plan_type, coverage):
    global health_plan_id_counter

    newPlan = {
        "id": health_plan_id_counter,
        "name": name,
        "type": plan_type,
        "coverage": coverage,
        "active": True
    }
    health_plan_id_counter += 1
    health_plans.append(newPlan)
    return newPlan


def listHealthPlans():
    if not health_plans:
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
# USUÁRIOS / PACIENTES / MÉDICOS
# =========================
def createUser(name, age, gender, tel, address, health_plan_id=None):
    global user_id_counter
    newUser = {
        "id": user_id_counter,
        "name": name,
        "age": age,
        "gender": gender,
        "tel": tel,
        "address": address,
        "health_plan_id": health_plan_id,
        "createdAt": time.time(),
        "updatedAt": time.time(),
    }
    user_id_counter += 1
    users.append(newUser)
    return newUser


def createAppointment(patientName, doctorName, date):
    global appointment_id_counter
    newAppointment = {
        "id": appointment_id_counter,
        "patientName": patientName,
        "doctorName": doctorName,
        "date": date
    }
    appointment_id_counter += 1
    appointments.append(newAppointment)
    return newAppointment


def listPatients():
    print("Pacientes cadastrados:")
    for i, patient in enumerate(patients):
        plan = getHealthPlanById(patient["health_plan_id"])
        plan_name = plan["name"] if plan else "Particular"

        print(
            f"{i + 1}. Nome: {patient['name']} | Idade: {patient['age']} | "
            f"Gênero: {patient['gender']} | Plano: {plan_name}"
        )


def listDoctors():
    print("Médicos cadastrados:")
    for i, doctor in enumerate(doctors):
        print(
            f"{i + 1}. Nome: {doctor['name']} | Idade: {doctor['age']} | "
            f"Gênero: {doctor['gender']}"
        )


def listAppointments():
    print("Consultas cadastradas:")
    for i, appointment in enumerate(appointments):
        print(
            f"{i + 1}. Paciente: {appointment['patientName']} | "
            f"Médico: {appointment['doctorName']} | Data: {appointment['date']}"
        )


# =========================
# CADASTRO INPUT
# =========================
def askForInfo(type):
    os.system("cls" if os.name == "nt" else "clear")

    name = input("Informe o nome do " + type + ": ")
    age = get_int("Informe a idade do " + type + ": ")
    gender = input("Informe o gênero do " + type + ": ")
    tel = input("Informe o número de telefone do " + type + ": ")
    address = input("Informe o endereço do " + type + ": ")

    health_plan_id = None
    if type == "paciente":
        listHealthPlans()
        choice = input("\nDigite o ID do plano de saúde ou ENTER para Particular: ")
        if choice.strip():
            try:
                pid = int(choice)
                if getHealthPlanById(pid):
                    health_plan_id = pid
                else:
                    print("Plano inválido. Usando Particular.")
            except:
                print("Entrada inválida. Usando Particular.")

    return createUser(name, age, gender, tel, address, health_plan_id)


def askForAppointmentInfo():
    os.system("cls" if os.name == "nt" else "clear")

    if not patients or not doctors:
        print("Necessário ter pacientes e médicos cadastrados.")
        input("Pressione ENTER para voltar...")
        return

    listPatients()
    patientName = input("\nDigite o nome do paciente: ")
    if not any(p["name"] == patientName for p in patients):
        print("Paciente inexistente.")
        input("ENTER...")
        return

    listDoctors()
    doctorName = input("\nDigite o nome do médico: ")
    if not any(d["name"] == doctorName for d in doctors):
        print("Médico inexistente.")
        input("ENTER...")
        return

    appointmentDate = input("Digite a data da consulta (dd/mm/yyyy): ")
    return createAppointment(patientName, doctorName, appointmentDate)


# =========================
# REMOÇÕES
# =========================
def RemoveAppointment():
    listAppointments()
    idx = get_int("Informe o número da consulta que deseja excluir: ") - 1
    if 0 <= idx < len(appointments):
        appointments.pop(idx)


def RemovePatients():
    listPatients()
    idx = get_int("Informe o número do paciente que deseja excluir: ") - 1
    if 0 <= idx < len(patients):
        patients.pop(idx)


def RemoveDoctor():
    listDoctors()
    idx = get_int("Informe o número do médico que deseja excluir: ") - 1
    if 0 <= idx < len(doctors):
        doctors.pop(idx)


# =========================
# UPDATE
# =========================
def updateUser(userList, userType):
    listPatients() if userType == "paciente" else listDoctors()

    idx = get_int("\nDigite o número que deseja atualizar: ") - 1
    if 0 <= idx < len(userList):
        user = userList[idx]

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
    else:
        op = input("Paciente não encontrado. Retornando ao menu...")
        return None


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
        op = get_int("Opção: ")

        if op == 1:
            p = askForInfo("paciente")
            patients.append(p)
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
            d = askForInfo("médico")
            doctors.append(d)
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
            a = askForAppointmentInfo()
        elif op == 2:
            listAppointments()
            input("ENTER...")
        elif op == 3:
            RemoveAppointment()
        elif op == 4:
            return


# =========================
# MAIN MENU
# =========================
def mainMenu():
    # Planos iniciais
    createHealthPlan("Unimed", "Apartamento", ["Consulta", "Exames", "Cirurgia"])
    createHealthPlan("Bradesco Saúde", "Enfermaria", ["Consulta", "Exames"])
    createHealthPlan(
        "SulAmérica",
        "Empresarial",
        [
            "Consultas", "Exames", "Cirurgias",
            "Isenção de carências a partir de 10 vidas",
            "Descontos em farmácias até 70%",
            "Telemedicina", "Programa Saúde Integral"
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