# main.py

import json
from services.user_service import UserService
import os
from time import sleep

def main():
    user_service = UserService('src/data/users.json')

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("                                                     ===================================")
        print("                                                       Sistema de Cadastro de Usuários")
        print("                                                     ===================================")
        sleep(2)
        print("\n                                                 Bem-vindo ao sistema de cadastro de usuários!")
        sleep(1)
        print("                                                      (Pressione Enter para continuar)")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Escolha uma opção:\n")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Sair")
        sleep(3)
        choice = input("\nEscolha uma opção: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            name = input("Nome: ")
            email = input("Email: ")
            password = input("Senha: ")
            user_service.add_user(name, email, password)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cadastrando usuário...")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Usuário cadastrado com sucesso!")
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Listando usuários...")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            users = user_service.get_users()
            if users:
                print("Usuários cadastrados:\n")
                for user in users:
                    print(f"ID: {user['id']}\nNome: {user['name']}\nEmail: {user['email']}")
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Nenhum usuário cadastrado.")
                input()
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saindo do programa...")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Tente novamente.")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
