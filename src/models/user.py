class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    def validate_email(self):
        return "@" in self.email and "." in self.email

    def validate_password(self):
        return len(self.password) >= 6
