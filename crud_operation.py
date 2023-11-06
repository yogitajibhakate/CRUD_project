class CRUD:

    def is_strong_password(self, password):
        min_length = 8
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in "@$!%*?&" for char in password)

        if len(password) < min_length:
            return False, "Password is too short. It should be at least 8 characters."
        if not has_uppercase:
            return False, "Password should contain at least one uppercase letter."
        if not has_lowercase:
            return False, "Password should contain at least one lowercase letter."
        if not has_digit:
            return False, "Password should contain at least one digit."
        if not has_special:
            return False, "Password should contain at least one special character."

        return True, "Password is strong."

    def create(self, name, number, email, password):
        if not name.isalpha():
            print("Invalid name. Please enter only letters.")
            return

        if not number.isdigit():
            print("Invalid number. Please enter only numbers.")
            return

        is_strong, message = self.is_strong_password(password)

        if not is_strong:
            print("Weak password:", message)
            return

        self.name = name
        self.number = number
        self.email = email
        self.password = password

    def read(self):
        if hasattr(self, 'name'):
            print("Name:", self.name)
            print("Number:", self.number)
            print("Email:", self.email)
            print("Password:", self.password)
        else:
            print("No data available.")

    def update(self, name, number, email, password):
        if hasattr(self, 'name'):
            self.name = name
            self.number = number
            self.email = email
            self.password = password
            print("Data updated.")
        else:
            print("No data to update.")

    def delete(self):
        if hasattr(self, 'name'):
            self.name = ''
            self.number = ''
            self.email = ''
            self.password = ''
            print("Data deleted.")
        else:
            print("No data to delete.")

obj = CRUD()

print("1: sing up")
print("2: sing in")
print("3: Exit")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name1 = input("Enter name: ")
        number1 = input("Enter number: ")
        email1 = input("Enter name for email: ")
        password1 = input("Enter password: ")
        add = email1 + "@gmail.com"
        obj.create(name1, number1, add, password1)

    elif choice == 2:
        obj.read()
        update_or_delete = input("Do you want to update or delete this data? (U/D): ")
        if update_or_delete.lower() == 'u':
            name2 = input("Enter new name: ")
            number2 = input("Enter new number: ")
            email2 = input("Enter new name for email: ")
            password2 = input("Enter new password: ")
            p = email2 + "@gmail.com"
            obj.update(name2, number2, p, password2)
        elif update_or_delete.lower() == 'd':
            obj.delete()
        else:
            print("Invalid option. Please enter 'U' for update or 'D' for delete.")

    elif choice == 3:
        break

    else:
        print("Invalid choice.")

