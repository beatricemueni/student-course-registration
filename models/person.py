class Person:

    def __init__(self, name, email, phone_number):
        if not name:
            raise ValueError("Name cannot be empty")
        
        if "@" not in email:
            raise ValueError("Invalid email")

        if not phone_number:
            raise ValueError("Phone number cannot be empty")
        self.name = name
        self.email = email
        self.phone_number = phone_number        