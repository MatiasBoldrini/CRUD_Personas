from os.path import exists

class Persona:
    def __init__(self):
        self.personas = {}
        self.database_directory = (
            'valores.txt'
        )

    def add_Users(self):
        if self.check_input() and not self.is_user_in_DB(self.dni):
            with open(self.database_directory, "a") as f:
                f.write(self.dni + " " + self.nombre + " " + self.apellido)
                f.write("\n")
            return True

    def check_input(self, dni='', nombre='', apellido=''):
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese apellido: ")
        if dni == '':
            dni = input("Ingrese dni: ")
        if not (apellido and nombre and dni.isnumeric()):
            raise Exception("INCORRECT DATA")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        return True

    def refresh_Users(self):
        lines = []
        with open(self.database_directory, "r") as f:
            lines = f.readlines()
        for line in lines:
            atributos = line.split()
            self.personas[atributos[0]] = atributos

    def modify_Users(self, dni):
        if self.check_input(dni) and self.is_user_in_DB(dni):
            with open(self.database_directory, "r") as f:
                lines = f.readlines()
            with open(self.database_directory, "w") as f:
                for line in lines:
                    if dni not in line.strip("\n"):
                        f.write(line)
                    else:
                        f.write(dni + " " + self.nombre + " " + self.apellido)
                        f.write("\n")
            return True

    def delete_Users(self, dni):
        if self.is_user_in_DB(dni):
            with open(self.database_directory, "r") as f:
                lines = f.readlines()
            with open(self.database_directory, "w") as f:
                for line in lines:
                    if dni not in line.strip("\n"):
                        f.write(line)
            return True
        return False

    def is_user_in_DB(self, dni):
        self.refresh_Users()
        return dni in self.personas.keys()

    def get_User_Attributes(self, dni):
        self.refresh_Users()
        return self.personas.get(dni)


