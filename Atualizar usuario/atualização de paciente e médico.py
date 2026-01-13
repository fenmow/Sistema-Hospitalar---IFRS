import os
import time

users = []
patients = []
doctors = []
appointments = []


def createUser(name, age, gender, tel, address):
    newUser = {
        "id": len(users),
        "name": name,
        "age": age,
        "gender": gender,
        "tel": tel,
        "address": address,
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
    print("Usuários cadastrados:")
    for i, patient in enumerate(patients):
        print(
            f"{i + 1}. Nome: {patient['name']}, Idade: {patient['age']}, Gênero: {patient['gender']}"
        )


def listDoctors():
    print("Médicos cadastrados:")
    for i, doctor in enumerate(doctors):
        print(
            f"{i + 1}. Nome: {doctor['name']}, Idade: {doctor['age']}, Gênero: {doctor['gender']}"
        )


def listAppointments():
    print("Consultas cadastradas:")
    for i, appointment in enumerate(appointments):
        print(
            f"{i + 1}. Paciente: {appointment['patientName']}, Médico: {appointment['doctorName']}, Data: {appointment['date']}"
        )


def askForAppointmentInfo():
    os.system("cls" if os.name == "nt" else "clear")
    patientName = ''
    doctorName = ''

    if len(patients) == 0:
        print('Nenhum paciente cadastrado.')
        input('Digite ENTER para voltar ao menu.')
        return

    if len(doctors) == 0:
        print('Nenhum médico cadastrado.')
        input('Digite ENTER para voltar ao menu.')
        return

    listPatients()
    selectedPatient = input('Digite o nome do paciente que vai consultar: ')
    for i in patients:
        if i['name'] == selectedPatient:
            patientName = i['name']

    if not patientName:
        print('Paciente não encontrado...')
        input('Digite ENTER para voltar ao menu.')
        return

    listDoctors()
    selectedDoctor = input('Digite o nome do médico que vai realizar o atendimento da consulta: ')
    for i in doctors:
        if i['name'] == selectedDoctor:
            doctorName = i['name']

    if not doctorName:
        print('Médico não encontrado...')
        input('Digite ENTER para voltar ao menu.')
        return

    appointmentDate = input('Digite a data da consulta ( dd/mm/yyyy ): ')
    newAppointment = createAppointment(selectedPatient, selectedDoctor, appointmentDate)
    return newAppointment


def askForInfo(type):
    os.system("cls" if os.name == "nt" else "clear")
    name = input("Informe o nome do " + type + ": ")
    age = int(input("Informe a idade do " + type + ": "))
    gender = input("Informe o gênero do " + type + ": ")
    tel = input("Informe o número de telefone do " + type + ": ")
    address = input("Informe o endereço do " + type + ": ")
    newEntity = createUser(name, age, gender, tel, address)
    return newEntity


def RemoveAppointment():
    if len(appointments) == 0:
        print("Nenhuma consulta cadastrada.")
        return

    listAppointments()
    index = int(input("Informe o número da consulta que deseja excluir: ")) - 1

    if 0 <= index < len(appointments):
        removed_appointment = appointments.pop(index)
        print(
            f"Consulta do paciente {removed_appointment['patientName']} com o médico {removed_appointment['doctorName']} removida com sucesso."
        )
    else:
        print("Número inválido. Nenhuma consulta foi removida.")
    return


def RemovePatients():
    if len(patients) == 0:
        print("Nenhum usuário cadastrado.")
        return

    listPatients()
    index = int(input("Informe o número do usuário que deseja excluir: ")) - 1

    if 0 <= index < len(patients):
        removed_patients = patients.pop(index)
        print(f"Removido o usuário: {removed_patients['name']}.")
    else:
        print("Número inválido. Nenhum usuário foi removido.")
    return


def RemoveDoctor():
    if len(doctors) == 0:
        print("Nenhum médico cadastrado.")
        return

    listDoctors()
    index = int(input("Informe o número do medico que deseja excluir: ")) - 1

    if 0 <= index < len(doctors):
        removed_doctor = doctors.pop(index)
        print(f"Removido o médico {removed_doctor['name']}.")
    else:
        print("Número inválido. Nenhum médico foi removido.")
    return

###atualizar usuario###
def updateUser(userList, userType):
    if len(userList) == 0:
        print(f"Nenhum {userType} cadastrado.")
        input("Pressione ENTER para voltar...")
        return

    os.system("cls" if os.name == "nt" else "clear")
    print(f"Lista de {userType}s cadastrados:\n")

    for i, user in enumerate(userList):
        print(f"{i + 1}. Nome: {user['name']} | Idade: {user['age']} | Gênero: {user['gender']}")

    index = int(input(f"\nDigite o número do {userType} que deseja atualizar: ")) - 1

    if 0 <= index < len(userList):
        user = userList[index]

        print("\nDeixe em branco e pressione ENTER para manter o valor atual.\n")

        name = input(f"Nome ({user['name']}): ")
        age = input(f"Idade ({user['age']}): ")
        gender = input(f"Gênero ({user['gender']}): ")
        tel = input(f"Telefone ({user['tel']}): ")
        address = input(f"Endereço ({user['address']}): ")

        if name:
            user['name'] = name
        if age:
            user['age'] = int(age)
        if gender:
            user['gender'] = gender
        if tel:
            user['tel'] = tel
        if address:
            user['address'] = address

        user['updatedAt'] = time.time()
        print(f"\n{userType.capitalize()} atualizado com sucesso!")
    else:
        print("Opção inválida.")

    input("\nPressione ENTER para voltar...")


def appointmentsActionsMenu():
    op = 0
    while op != 5:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU DE CONSULTAS ======\n\n"
            "- 1 Cadastrar nova consulta\n"
            "- 2 Listar Consultas\n"
            "- 3 Atualizar Consultas\n"
            "- 4 Excluir Consulta\n"
            "- 5 Retornar ao menu principal\n"
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            newAppointment = askForAppointmentInfo()
            if newAppointment:
                appointments.append(newAppointment)
        elif op == 2:
            os.system("cls" if os.name == "nt" else "clear")
            listAppointments()
            input("Pressione ENTER para voltar... ")
        elif op == 3:
            print("Atualização de consultas ainda não implementada.")
            input("Pressione ENTER para voltar...")
        elif op == 4:
            os.system("cls" if os.name == "nt" else "clear")
            RemoveAppointment()
            input("Pressione ENTER para voltar...")
        elif op == 5:
            return


def doctorActionsMenu():
    op = ""

    while op != 5:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU DE MÉDICOS ======\n\n"
            "- 1 Cadastrar novo médico\n"
            "- 2 Listar médicos\n"
            "- 3 Atualizar médico\n"
            "- 4 Excluir médico\n"
            "- 5 Retornar ao menu principal\n"
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            newDoctor = askForInfo("médico")
            doctors.append(newDoctor)
            users.append(newDoctor)
        elif op == 2:
            os.system("cls" if os.name == "nt" else "clear")
            listDoctors()
            input("Pressione ENTER para voltar... ")
        elif op == 3:
            updateUser(doctors, "médico")
        elif op == 4:
            RemoveDoctor()
            input("Pressione ENTER para voltar...")
        elif op == 5:
            return


def pacientActionsMenu():
    op = ""

    while op != 5:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU DE PACIENTES ======\n\n"
            "- 1 Cadastrar novo paciente\n"
            "- 2 Listar pacientes\n"
            "- 3 Atualizar paciente\n"
            "- 4 Excluir paciente\n"
            "- 5 Retornar ao menu principal\n"
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            newPatient = askForInfo("paciente")
            patients.append(newPatient)
            users.append(newPatient)
        elif op == 2:
            os.system("cls" if os.name == "nt" else "clear")
            listPatients()
            input("Pressione ENTER para voltar... ")
        elif op == 3:
            updateUser(patients, "paciente")
        elif op == 4:
            RemovePatients()
            input("Pressione ENTER para voltar...")
        elif op == 5:
            return


def mainMenu():
    op = ""

    while op != 4:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU PRINCIPAL ======\n\n"
            "- 1 Ações para pacientes\n"
            "- 2 Ações para médicos\n"
            "- 3 Ações para consulta\n"
            "- 4 Sair\n"
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            pacientActionsMenu()
        elif op == 2:
            doctorActionsMenu()
        elif op == 3:
            appointmentsActionsMenu()
        elif op == 4:
            print("Saindo...")


mainMenu()