import json

class UserService:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_user(self, name, email, password):
        # Carregar os usuários existentes
        try:
            with open(self.file_path, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []

        # Criar um novo usuário
        new_user = {
            "id": len(users) + 1,
            "name": name,
            "email": email,
            "password": password  # Em um sistema real, você deve criptografar a senha
        }

        # Adicionar o novo usuário à lista
        users.append(new_user)

        # Salvar os usuários atualizados no arquivo
        with open(self.file_path, 'w') as file:
            json.dump(users, file, indent=4)

        print("Usuário adicionado com sucesso!")

    def get_users(self):
        # Carregar os usuários do arquivo JSON
        try:
            with open(self.file_path, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []  # Retorna uma lista vazia se o arquivo não existir
        return users
