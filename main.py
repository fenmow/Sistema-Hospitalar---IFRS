import os
import time

patients = []
doctors = []
appointments = []

def createUser(name, age, gender, tel, address):
    newUser = { 
        "name": name, 
        "age": age, 
        "gender": gender, 
        "tel": tel, 
        "address": address,
        "createdAt": time.time(),
        "updatedAt": time.time()
    }
    return newUser 

def askForInfo(type):
    name = input('Informe o nome do '+type+': ')
    age = int(input('Informe a idade do '+type+': '))
    gender = input('Informe o gênero do '+type+': ')
    tel = input('Informe o número de telefone do '+type+': ')
    address = input('Informe o endereço do '+type+': ')
    newEntity = createUser(name, age, gender, tel, address)
    return newEntity

def doctorActionsMenu():
    op = ''
    
    while (op != 5):
        print('\n\n====== SISTEMA HOSPITALAR - IFRS ======\n' \
        '====== MENU DE MÉDICOS ======\n\n' \
        '- 1 Cadastrar novo médico\n' \
        '- 2 Listar médicos\n' \
        '- 3 Atualizar médico\n' \
        '- 4 Excluir médico\n'
        '- 5 Retornar ao menu principal\n' \
        '')
        op = int(input('Selecione uma opção: '))

        if op == 1:
            newDoctor = askForInfo('médico')
            doctors.append(newDoctor)
        elif op == 2:
            #TODO
            print('')
        elif op == 3:
            #TODO
            print('')
        elif op == 4:
            #TODO
            print('')
        elif op == 5:
            return

def pacientActionsMenu():
    op = ''
    
    while (op != 5):
        print('\n\n====== SISTEMA HOSPITALAR - IFRS ======\n' \
        '====== MENU DE PACIENTES ======\n\n' \
        '- 1 Cadastrar novo paciente\n' \
        '- 2 Listar pacientes\n' \
        '- 3 Atualizar paciente\n' \
        '- 4 Excluir paciente\n'
        '- 5 Retornar ao menu principal\n' \
        '')
        op = int(input('Selecione uma opção: '))

        if op == 1:
            newPatient = askForInfo('paciente')
            patients.append(newPatient)
        elif op == 2:
            #TODO
            print('')
        elif op == 3:
            #TODO
            print('')
        elif op == 4:
            #TODO
            print('')
        elif op == 5:
            return

def mainMenu():
    op = ''
    
    while (op != 4):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\n====== SISTEMA HOSPITALAR - IFRS ======\n' \
        '====== MENU PRINCIPAL ======\n\n' \
        '- 1 Ações para pacientes\n' \
        '- 2 Ações para médicos\n' \
        '- 3 Agendar consulta\n' \
        '- 4 Sair\n' \
        '')
        op = int(input('Selecione uma opção: '))

        if op == 1:
            pacientActionsMenu()
        elif op == 2:
            doctorActionsMenu()
        elif op == 3:
            #TODO
            print('')
        elif op == 4:
            print('Saindo...')






mainMenu()