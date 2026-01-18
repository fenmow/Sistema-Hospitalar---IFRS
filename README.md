# Sistema Hospitalar - IFRS 

Este projeto é um **sistema de gestão hospitalar em Python**, desenvolvido para simular o cadastro e gerenciamento de **pacientes, médicos e consultas** por meio de um menu interativo no terminal.

A versão atual utiliza **MongoDB** para armazenamento dos dados, aplicando conceitos de **CRUD**, **funções**, **estruturas de controle** e **integração com banco de dados NoSQL**. 

---

##  Funcionalidades

###  Pacientes
- Cadastrar paciente  
- Listar pacientes  
- Atualizar dados  
- Excluir paciente  

###  Médicos
- Cadastrar médico  
- Listar médicos  
- Atualizar dados  
- Excluir médico  

###  Consultas
- Agendar consulta entre paciente e médico  
- Listar consultas  
- Excluir consulta  

---

##  Conceitos aplicados

- Python estruturado em funções  
- Menus interativos no terminal  
- CRUD completo  
- Integração com MongoDB usando PyMongo  
- Validação básica de dados  
- Organização de coleções no banco  
- Uso de timestamps (`createdAt`, `updatedAt`)  

---

##  Tecnologias utilizadas

- Python 3.x  
- MongoDB Atlas (Banco NoSQL na nuvem)  
- PyMongo  
- Bibliotecas padrão: `os`, `time`

---

##  Pré-requisitos

- Python 3 instalado  
- Conta no MongoDB Atlas  
- Biblioteca PyMongo instalada  

Instale o PyMongo no terminal usando pip:
```
pip install pymongo
```

No código, a conexão é feita via MongoDB Atlas:
MongoClient("mongodb+srv://SEU_USUARIO:SUA_SENHA@cluster.mongodb.net/")


SEU_USUARIO do banco.
SUA_SENHA do banco.

## Como executar

1. Clone o repositório:

````
git clone https://github.com/fenmow/projeto-hospital-IFRS.git
````
2. Entre na pasta:
````
cd projeto-hospital-IFRS
````
3. Execute o programa:
```` 
python main.py
````


4.Use o menu no terminal para navegar pelo sistema.

---

## Estrutura do projeto
````
projeto-hospital-IFRS
┣ main.py
┗ README.md
````

Documentação completa disponível em /docs/Documentacao_Sistema_Hospitalar.pdf